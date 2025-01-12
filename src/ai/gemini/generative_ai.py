# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module::  src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
"""
import re
import asyncio
import time
import json
from io import IOBase
from pathlib import Path
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, field
import base64

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError

import header
from header import __root__
from src.logger.logger import logger
from src import gs

from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_dumps
from src.utils.image import get_image_bytes
from src.utils.printer import pprint as print

timeout_check = TimeoutCheck()

def remove_html_blocks(text: str) -> str:
    """
    Удаляет блоки текста, которые начинаются с '```html' и заканчиваются на '```' или '```\n'.

    Args:
        text (str): Входной текст.

    Returns:
        str: Текст без блоков '```html'.
    """
    return re.sub(r'```html.*?```', '', text, flags=re.DOTALL)


@dataclass
class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    api_key: str
    model_name: str = field(default="gemini-2.0-flash-exp")
    generation_config: Dict = field(default_factory=lambda: {"response_mime_type": "text/plain"})
    system_instruction: Optional[str] = None
    dialogue_log_path: Path = field(init=False)
    dialogue_txt_path: Path = field(init=False)
    history_dir: Path = field(init=False)
    history_txt_file: Path = field(init=False)
    history_json_file: Path = field(init=False)
    chat_history: List[Dict] = field(default_factory=list, init=False)
    model: Any = field(init=False)
    _chat: Any = field(init=False)

    MODELS: List[str] = field(default_factory=lambda: [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b",
        "gemini-2.0-flash-exp",
    ], init=False)

    def __post_init__(self):
        """Инициализация модели GoogleGenerativeAI с дополнительными настройками."""
        self.dialogue_log_path = Path(__root__, gs.path.external_storage, "gemini_data", "log")
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{gs.now}.txt"
        self.history_dir = Path(__root__, gs.path.external_storage, "gemini_data", "history")
        self.history_txt_file = self.history_dir / f"gemini_{gs.now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{gs.now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name, 
            generation_config=self.generation_config,
            system_instruction=self.system_instruction
        )
        self._chat = self._start_chat()

    @property
    def config(self):
        """Получаю конфигурацию из файла настроек"""
        return j_loads(gs.path.src / "ai" / "gemini" / "config.json")

    def _start_chat(self):
        """"""
        if self.system_instruction:
             return self.model.start_chat(history=[{"role": "user", "parts": [self.system_instruction]}])
        else:
            return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохранить диалог в JSON файл.
        """
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode="+a")

    async def _save_chat_history(self):
        """Сохраняет всю историю чата в JSON файл"""
        if self.chat_history:
            j_dumps(data=self.chat_history, file_path=self.history_json_file, mode="w")

    async def _load_chat_history(self):
        """Загружает историю чата из JSON файла"""
        try:
            if self.history_json_file.exists():
                self.chat_history = j_loads(self.history_json_file)
                self._chat = self._start_chat()
                for entry in self.chat_history:
                    self._chat.history.append(entry)
                logger.debug("История чата загружена из файла.", None, False)
        except Exception as ex:
            logger.error(f"Ошибка загрузки истории чата: ", ex, False)

    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        Метод отправляет текстовый запрос модели и возвращает ответ.
        """
        for attempt in range(attempts):
            try:
                response = await self.model.generate_content_async(q)
               
                if not response.text:
                    logger.debug(
                        f"No response from the model. Attempt: {attempt}\nSleeping for {2 ** attempt}",
                        None,
                        False
                    )
                    time.sleep(2**attempt)
                    continue  # Повторить попытку

                response_text = remove_html_blocks(response.text)
                messages = [
                    {"role": "user", "content": q},
                    {"role": "model", "content": response_text},
                ]

                self._save_dialogue([messages])
                return response_text

            except requests.exceptions.RequestException as ex:
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(
                    f"Network error. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    False,
                )
                time.sleep(1200)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, False)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2**attempt + 10)
                continue
            except ResourceExhausted as ex:
                logger.debug(
                    f"Quota exceeded. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    False,
                )
                time.sleep(10800)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:", ex, False)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(
                    f"Invalid input: Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",
                    ex,
                    None,
                )
                time.sleep(timeout)
                continue
            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:", ex, False)
                return
            except Exception as ex:
                logger.error("Unexpected error:", ex, False)
                return

        return

    async def chat(self, q: str) -> Optional[str]:
        """"""
        response = None
        try:
            await self._load_chat_history()
            content = { 'text': q }
            response = await self._chat.send_message_async (q)
            #response = await response.resolve()
            if response and response.text:
                response_text = remove_html_blocks(response.text)
                self.chat_history.append({"role": "user", "parts": [q]})
                self.chat_history.append({"role": "model", "parts": [response_text]})
                self._save_dialogue(self.chat_history)
                return response_text
            else:
                logger.error("Empty response in chat", None, False)
                return
        except Exception as ex:
            logger.error(f"Ошибка чата:\n {response=}", ex, False)
            return
        finally:
            await self._save_chat_history()


    async def describe_image(
        self, image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = ''
    ) -> Optional[str]:
        """
        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

        Args:
            image: Путь к файлу изображения или байты изображения

        Returns:
            str: Текстовое описание изображения.
            None: Если произошла ошибка.
        """
        try:
            # Подготовка контента для запроса
            if isinstance(image, Path):
                image = get_image_bytes(image)

            content = \
                [
                    {
                        "role": "user",
                        "parts": {
                            "inlineData": [
                                {
                                    "mimeType": mime_type,
                                    "data": image,
                                }
                            ]
                        }
                    }
                ]


            # Отправка запроса и получение ответа
            response = self.model.generate_content(
                str(
                    {
                        'text': prompt,
                        'data': image
                    }
                ))
           
            if response.text:
                return response.text
            else:
                print("Модель вернула пустой ответ.")
                return None

        except Exception as ex:
            print(f"Произошла ошибка: ", ex)
            ...
            return None

    async def upload_file(
        self, file: str | Path | IOBase, file_name: Optional[str] = None
    ) -> bool:
        """
        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
        response (file_types.File)
        """

        response = None
        try:
            response = await genai.upload_file_async(
                path=file,
                mime_type=None,
                name=file_name,
                display_name=file_name,
                resumable=True,
            )
            logger.debug(f"Файл {file_name} записан", None, False)
            return response
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                response = await genai.delete_file_async(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                await self.upload_file(file, file_name)
            except Exception as ex:
                logger.error(f"Общая ошибка модели: ", ex, False)
                ...
                return


async def main():
    # Замените на свой ключ API

    system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
    ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

    # Пример вызова describe_image с промптом
    image_path = Path(r"test.jpg")  # Замените на путь к вашему изображению

    if not image_path.is_file():
        print(
            f"Файл {image_path} не существует. Поместите в корневую папку с программой файл с названием test.jpg"
        )
    else:
        prompt = """Проанализируй это изображение. Выдай ответ в формате JSON,
        где ключом будет имя объекта, а значением его описание.
         Если есть люди, опиши их действия."""

        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (с JSON форматом):")
            print(description)
            try:
                parsed_description = j_loads(description)

            except Exception as ex:
                print("Не удалось распарсить JSON. Получен текст:")
                print(description)

        else:
            print("Не удалось получить описание изображения.")

        # Пример без JSON вывода
        prompt = "Проанализируй это изображение. Перечисли все объекты, которые ты можешь распознать."
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (без JSON формата):")
            print(description)

    file_path = Path('test.txt')
    with open(file_path, "w") as f:
        f.write("Hello, Gemini!")

    file_upload = await ai.upload_file(file_path, 'test_file.txt')
    print(file_upload)

    # Пример чата
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            break
        ai_message = await ai.chat(user_message)
        if ai_message:
            print(f"Gemini: {ai_message}")
        else:
            print("Gemini: Ошибка получения ответа")


if __name__ == "__main__":
    asyncio.run(main())