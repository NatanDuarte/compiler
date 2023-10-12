import os

from json import dumps
from core.compiler import Compiler

def process_interactive_mode():
    print("Modo Interativo - Digite 'exit' para sair.")
    while True:
        program = input(">> ")
        if program.lower() == "exit":
            break
        out = Compiler().compile(program)
        print(f"{dumps(out, indent=2)}")

def process_file_mode(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            out = Compiler().compile(file_content)
            print(f"{dumps(out, indent=2)}")

    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {str(e)}")
