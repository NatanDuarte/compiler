from core.tokenizer import Tokenizer
from core.parser import Parser


class Compiler:
    @staticmethod
    def compile(program:str) -> str:
        tokens = Tokenizer().tokenize(program)
        parser = Parser(tokens)
        return tokens, parser.parse()
