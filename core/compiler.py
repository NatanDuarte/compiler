from core.tokenizer import Tokenizer
from core.parser import Parser


class Compiler:
    @staticmethod
    def compile(program:str) -> str:
        tokens = Tokenizer().tokenize(program)
        for token in tokens:
            print(token)
        print()

        print('------------------------------')
        print()
        parser = Parser(tokens)
        return parser.parse()
