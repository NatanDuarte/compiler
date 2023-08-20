from model.token import Token


class Lexer:
    def __init__(self, input_text:str):
        self.input_text = input_text
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.input_text):
            current_char = self.input_text[self.position]

            if current_char.isspace():
                self.position += 1
                continue

            if current_char.isalpha():
                token_value = ""
                while self.position < len(self.input_text) \
                    and self.input_text[self.position].isalpha():
                    token_value += self.input_text[self.position]
                    self.position += 1
                self.tokens.append(Token(token_value, "IDENTIFIER"))

            elif current_char.isdigit():
                token_value = ""
                while self.position < len(self.input_text) \
                    and self.input_text[self.position].isdigit():
                    token_value += self.input_text[self.position]
                    self.position += 1
                self.tokens.append(Token(token_value, "INTEGER"))

            elif current_char == "(":
                self.tokens.append(Token(current_char, "LPAREN"))
                self.position += 1

            elif current_char == ")":
                self.tokens.append(Token(current_char, "RPAREN"))
                self.position += 1

            elif current_char == ";":
                self.tokens.append(Token(current_char, "SEMICOLON"))
                self.position += 1

            elif current_char == "+":
                self.tokens.append(Token(current_char, "PLUS"))
                self.position += 1

            elif current_char == "-":
                self.tokens.append(Token(current_char, "MINUS"))
                self.position += 1

            elif current_char == "=":
                self.tokens.append(Token(current_char, "EQUALS"))
                self.position += 1
            else:
                self.position += 1
        
        return self

    def get_tokens(self):
        return self.tokens
