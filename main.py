from __future__ import annotations
## \file main.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: header
	:platform: Windows, Unix
	:synopsys: Модуль автодoкументации на основе модели gemini
"""

import header
from header import __root__

from src.assistant import CodeAssistant
from src.utils.jjson import j_loads_ns

role = 'doc_writer'
lang = 'en'


config = j_loads_ns(__root__ / 'src' / 'assistant' / 'code_assistant.json')

for lang in config.languages:
	for role in config.roles:
		a = CodeAssistant(role = role, lang = lang)
		a.run()

# for role in config.roles:
# 	a = CodeAssistant(role = role, lang = 'he')
# 	a.run()