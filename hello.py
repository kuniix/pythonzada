#!/usr/bin/env python3
"""
    Hello world multi linguas    

Dependendo da lingua configurada no ambiente o programa exibe a correspondente

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_br

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Lucas Norato"
__license__ = "Unlicense"

import os.getenv("LANG")[:5]

current_language = "en_Us"

msg = "Hello, World!"

if current_language == "pt-BR" :
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Cyao, Mondo!"

print(msg)