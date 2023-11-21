from json import dumps
from core.compiler import Compiler

def process_interactive_mode():
    print("Modo Interativo - Digite 'exit' para sair.")
    while True:
        program = input(">> ")
        if program.lower() == "exit":
            break
        if (program.strip() == ''):
            print("Can't compile empty code or null")
            continue
        recognized = Compiler().compile(program)
        print('------------------------------')
        print(f'Recognized: {recognized}')

def process_file_mode(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            recognized = Compiler().compile(file_content)
            print('------------------------------')
            print(f'Recognized: {recognized}')

    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {str(e)}")
