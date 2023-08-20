from compiler.lexer import Lexer


def test_lexer_should_return_the_correct_number_of_tokens():
    lexer = Lexer("x = 3 + y;")
    tokens = lexer.tokenize().get_tokens()
    assert len(tokens) == 6

def test_lexer_should_read_variable_declaration():
    lexer = Lexer("var batata = 123;")
    tokens = lexer.tokenize().get_tokens()
    assert len(tokens) == 5
