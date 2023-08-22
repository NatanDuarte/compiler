import os

from lexer import Lexer


def init():
    while True:
        chain = input("Interactive Mode ('exit' to close) > ")
        if chain.lower() == 'exit':
            break
        elif chain.lower() == 'cls':
            clear_screen()
        else:
            lexer = Lexer(chain)
            lexer.tokenize()
            tokens = lexer.get_tokens()

            for token in tokens:
                print(token)

def clear_screen():
    system = os.name
    if system == 'posix':
        os.system('clear')
    elif system == 'nt':
        os.system('cls')
