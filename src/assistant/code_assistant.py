import asyncio
import argparse
import sys, os
from pathlib import Path
from typing import Iterator, List, Optional
from types import SimpleNamespace
import signal
import time
import re
import fnmatch
from dotenv import load_dotenv

import header
from header import __root__
from src import gs

from src.ai.gemini import GoogleGenerativeAI

from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint as print
from src.logger.logger import logger

load_dotenv()

def get_relative_path(full_path: str, relative_from: str) -> Optional[str]:
    """
    Возвращает часть пути начиная с указанного сегмента и до конца.
    Args:
        full_path (str): Полный путь.
        relative_from (str): Сегмент пути, с которого нужно начать извлечение.
    Returns:
        Optional[str]: Относительный путь начиная с `relative_from`, или None, если сегмент не найден.
    """
    try:
        path = Path(full_path)
        parts = path.parts
        if relative_from in parts:
            start_index = parts.index(relative_from)
            relative_path = Path(*parts[start_index:])
            return relative_path.as_posix()
        return None
    except Exception as e:
        logger.error(f"Ошибка в get_relative_path: {e}")
        return None


BASE_PATH: Path =  Path(__root__ , 'src', 'assistant')

class CodeAssistant:
    """ 
    .. :class:`CodeAssistant`
        :synopsis: Класс для работы ассистента программиста с моделями ИИ
    """

    role: str
    lang: str
    gemini_model: GoogleGenerativeAI
    config:SimpleNamespace = j_loads_ns(BASE_PATH / 'code_assistant.json')
    system_instruction:str
    code_instruction:str
    translations:SimpleNamespace

    def __init__(self, 
                 role:Optional[str] = 'doc_writer_md', 
                 lang: Optional[str] = 'en', 
                 models: Optional[list[str,str] | str] = ["gemini"], 
                 **kwargs):
        """Инициализация ассистента с заданными параметрами."""
        try:
            self.role = role 
            self.lang = lang
            self.models_list = kwargs.get("model", ["gemini"])
            self.config.docs_dir = self.config.docs_dir.replace('<lang>',self.lang)
            self.translations = j_loads_ns(  BASE_PATH / 'translations'  / 'translations.json' )
            self.system_instruction = Path( BASE_PATH / 'instructions' / f'CODE_RULES.{self.lang}.MD').read_text(encoding="UTF-8")
            self.code_instruction = Path( BASE_PATH / 'instructions' / f'{self.role}.{self.lang}.md').read_text(encoding="UTF-8")
            self._initialize_models(**kwargs)
        except Exception as e:
            logger.error(f"Ошибка при инициализации CodeAssistant: {e}")
            sys.exit(1)

    def _initialize_models(self, **kwargs):
        """Инициализация моделей на основе заданных параметров."""
        try:
            if "gemini" in self.models_list:
                self.gemini_model = GoogleGenerativeAI(
                    model_name = self.config.gemini.model_name,
                    api_key = os.getenv('GEMINI_API') ,
                    system_instruction = self.system_instruction,
                    **kwargs,
                )
        except Exception as e:
             logger.error(f"Ошибка при инициализации моделей: {e}")
             sys.exit(1)

    def remove_outer_quotes(self, response: str) -> str:
        """Удаляет внешние кавычки в начале и в конце строки, если они присутствуют."""
        try:
            response = response.strip()
        except Exception as ex:
            logger.error(f"Exception in `remove_outer_quotes()`: {ex}")
            return ''
        # if response.startswith(('```python', '```mermaid')):
        #     return response
        for prefix in self.config.remove_prefixes:
            if response.lower().startswith(prefix.lower()):
                return response.removeprefix(prefix).removesuffix("```").strip()
        return response

    async def process_files(self, 
                            start_dir:Optional[str | Path | list[str,str] | list[str,Path]] = None, 
                            docs_dir:Optional[str | Path] = None, ) -> bool:
        """компиляция, отправка запроса и сохранение результата."""
        flag = 'read_and_start_new'
        try:
            if not start_dir:
                start_dir = self.config.start_dir
            if not start_dir:
                logger.error("Ошибка иницаилизации стартовой директории")
                return False
            if not docs_dir:
                docs_dir = self.config.docs_dir
            if not docs_dir:
                logger.error("Ошибка иницаилизации конечной директории")
                return False

            start_dirs = start_dir if isinstance(start_dir,list) else [start_dir] 
            for process_driectory in start_dirs:
                logger.info(f"Start {process_driectory=}")
                for i, (file_path, content) in enumerate(self._yield_files_content(process_driectory)):
                    if not any((file_path, content)):
                        continue
                    if file_path and content:
                        try:
                            chat_data_folder = f'{self.config.docs_dir}/{self.role}/chat_history'
                            content_request = self._create_request(file_path, content)
                            
                            response = await self.gemini_model.chat(content_request, chat_data_folder, flag = flag)
                            flag = 'save_chat'
                        except Exception as e:
                             logger.error(f"Ошибка при запросе к модели: {e}")
                             continue
                        if response:
                            response = self.remove_outer_quotes(response)
                            if not await self._save_response(file_path, response, "gemini"):
                                logger.error(f"Файл {file_path} \n НЕ сохранился")
                                continue
                            print(f"Processed file number: {i + 1}", text_color="yellow")
                        else:
                            logger.error("Ошибка ответа модели")
                            continue
                    await asyncio.sleep(20) # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG (change timeout)
            return True
        except Exception as e:
            logger.error(f"Ошибка в process_files: {e}")
            return False

    async def send_file(self, file_path: Path) -> bool:
        """Отправка файла в модель."""
        try:
            if file_path.name in  ('__init__.py','header.py'):
                logger.info(f'Пропущен файл: {file_path}')
                return False
            if 'src' in file_path.parts:
                index = file_path.parts.index('src')
                relative_path = Path(*file_path.parts[index:])
                file_name = f'{self.config.start_dir}--' + '--'.join(relative_path.parts[1:-1]) + '--' + relative_path.stem
            else:
                file_name = file_path.stem
            response = await self.gemini_model.upload_file(file_path)
            if response and hasattr(response, 'url'):
                print(response, text_color='light_gray')
                return response.url
            return False
        except Exception as ex:
            logger.error(f'Ошибка при отправке файла: {ex}')
            return False

    def _create_request(self, file_path: str, content: str) -> str:
        """Создание запроса с учетом роли и языка."""
        try:
            roles_translations = getattr(self.translations.roles, self.role, 'doc_writer_md')
            role_description_translated = getattr(roles_translations, self.lang, 'Your specialization is documentation creation in the `MD` format')
            file_location_translated = getattr(self.translations.file_location_translated, self.lang, 'Path to file: ')
            content_request = {
                "role": f"{role_description_translated}",
                "output_language": self.lang,
                f"{file_location_translated}": get_relative_path(file_path, "hypotez"),
                "instruction": self.code_instruction or '',
                "input_code": f"```{content}```",
            }
            return str(content_request)
        except Exception as ex:
             logger.error(f"Ошибка в _create_request: {ex}")
             return ''
    
    def _yield_files_content(self, process_driectory: str| Path) -> Iterator[tuple[Path, str]]:
        """Генерирует пути файлов и их содержимое по указанным шаблонам."""
        try:
            exclude_file_patterns = [re.compile(pattern) for pattern in self.config.exclude_file_patterns]
        except Exception as e:
            logger.error(f"Не удалось скомпилировать регулярки из списка:{self.config.exclude_file_patterns} \n{e}")
            return
        include_file_patterns = self.config.include_files
        process_driectory = Path(process_driectory) if isinstance(process_driectory, str) else process_driectory
        for file_path in process_driectory.rglob("*"):
            if not any(fnmatch.fnmatch(file_path.name, pattern) for pattern in include_file_patterns):
                continue
            if any(exclude_dir in file_path.parts for exclude_dir in self.config.exclude_dirs):
                continue
            if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                continue
            if str(file_path) in self.config.exclude_files:
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
                yield file_path, content
            except Exception as ex:
                logger.error(f"Ошибка при чтении файла: {file_path}\n{ex}")
                yield None, None
   
    async def _save_response(self, file_path: Path, response: str, model_name: str) -> None:
        """Сохранение ответа модели в файл с добавлением суффикса."""
        try:
            file_path = str(file_path).replace(str(self.config.start_dir), f'{self.config.docs_dir}/{self.role}')

            suffix =  '.md'  # По умолчанию используется .md
            export_path = Path(f"{file_path}{suffix}") if self.config.save_as_md else Path(file_path)
            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_text(response, encoding='utf-8')
            print(f'Ответ модели сохранен в: {export_path}', text_color='green')
            return True
        except Exception as ex:
            logger.critical(f'Ошибка сохранения файла: {file_path}\n{ex}')
            ...
            return False
        
    def run(self):
        """Запуск процесса обработки файлов."""
        signal.signal(
            signal.SIGINT, signal_handler
        )  # Обработка прерывания (Ctrl+C)
        asyncio.run(self.process_files())

def signal_handler(signal, frame):
    """Обработка прерывания выполнения."""
    print("Процесс был прерван", text_color="red")
    sys.exit(0)

def parse_args():
    """Разбор аргументов командной строки."""
    parser = argparse.ArgumentParser(description="Ассистент для программистов")
    parser.add_argument(
        "--role",
        type=str,
        default="code_checker",
        help="Роль для выполнения задачи",
    )
    parser.add_argument("--lang", type=str, default="ru", help="Язык выполнения")
    parser.add_argument(
        "--model",
        nargs="+",
        type=str,
        default=["gemini"],
        help="Список моделей для инициализации",
    )
    parser.add_argument(
        "--start-dirs",
        nargs="+",
        type=str,
        default=[],
        help="Список директорий для обработки",
    )
    return vars(parser.parse_args())


def main():
    """Основная функция для запуска."""
    args = parse_args()
    assistant = CodeAssistant(**args)
    assistant.run()


if __name__ == "__main__":
    """
    Код запускает бесконечный цикл, в котором выполняется обработка файлов с учетом ролей и языков, указанных в конфигурации.
    Конфигурация обновляется в каждом цикле, что позволяет динамически изменять настройки во время работы программы.
    Для каждой комбинации языка и роли создается экземпляр класса :class:`CodeAssistant`, который обрабатывает файлы, используя заданную модель ИИ.
    """
    config_path = BASE_PATH / "code_assistant.json"
    while True:
        try:
            config = j_loads_ns(config_path)
        except Exception as e:
            logger.error(f"Ошибка при загрузке конфигурации: {e}")
            sys.exit(1)
        for lang in config.languages:
            for role in config.roles:
                logger.debug(f"Start role: {role}, lang: {lang}")
                try:
                    assistant = CodeAssistant(
                        role=role,
                        lang=lang,
                        model=["gemini"],
                    )
                    asyncio.run(assistant.process_files(start_dir=config.start_dirs))
                except Exception as e:
                    logger.error(f"Ошибка при выполнении process_files: {e}")
        try:
            config = j_loads_ns(config_path)
        except Exception as e:
            logger.error(f"Ошибка при обновлении конфигурации: {e}")
            sys.exit(1)