from core.tokenizer import Tokenizer


class Compiler:
    @staticmethod
    def compile(program:str) -> str:
        tokens = Tokenizer().tokenize(program)
        return tokens
