from lexer import Lexer


tokens = Lexer("var carla = karla;").tokenize().get_tokens()

for token in tokens:
    print(token)