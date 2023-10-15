class Parser:
    def __init__(self, tokens):
        self.is_error = False
        self.tokens = tokens
        self.current_token = None
        self.index = 0
        self.token_count = len(tokens)

        self.token_handlers = {
            "init": self.parse_init,
            "var": self.parse_var,
            "write": self.parse_write,
            "identifier": self.parse_identifier,
            "data_type": self.parse_data_type,
            "attribution": self.parse_attribution,
            "integer": self.parse_integer,
            "float": self.parse_float,
            "operator": self.parse_operator,
            "end_statement": self.parse_end_statement,
            "end": self.parse_end,
        }

    def parse(self):
        self.advance()
        self.program()
        return self.current_token["kind"] == "end" and not self.is_error

    def advance(self):
        if self.index < self.token_count:
            self.current_token = self.tokens[self.index]
            self.index += 1

    def program(self):
        self.expect("init")
        self.commands()
        self.expect("end")

    def commands(self):
        while self.current_token["kind"] in ["var", "identifier", "write", "attribution"]:
            if self.is_error:
                break
            if self.current_token["kind"] == "var":
                self.parse_var()
            elif self.current_token["kind"] == "write":
                self.parse_write()
            elif self.current_token["kind"] == "identifier":
                self.advance()
                self.parse_assignment()
            else:
                self.token_handlers[self.current_token["kind"]]()

    def parse_init(self):
        self.advance()

    def parse_var(self):
        self.advance()
        self.expect("identifier")
        self.expect("data_type")
        self.expect("attribution")
        self.expression()
        self.expect("end_statement")

    def parse_write(self):
        self.advance()
        self.expect("left_parenthesis")
        self.expression()
        self.expect("right_parenthesis")
        self.expect("end_statement")

    def parse_identifier(self):
        self.advance()

    def parse_data_type(self):
        self.advance()

    def parse_attribution(self):
        self.expression()

    def parse_integer(self):
        self.advance()

    def parse_float(self):
        self.advance()

    def parse_operator(self):
        self.advance()

    def parse_end_statement(self):
        self.advance()

    def parse_assignment(self):
        self.advance()
        self.expression()
        self.expect("end_statement")

    def parse_end(self):
        self.advance()

    def expression(self):
        self.term()
        while self.current_token["kind"] != "end_statement" and not self.is_error:
            if self.current_token["kind"] == "right_parenthesis":
                break
            if self.current_token["kind"] == "operator":
                self.advance()
                self.term()
            else:
                self.error('invalid expression')

    def term(self):
        if self.current_token["kind"] in ["integer", "float", "identifier"]:
            self.advance()
        else:
            self.error("Invalid term")

    def expect(self, expected_kind):
        if self.current_token["kind"] == expected_kind:
            self.advance()
        else:
            self.error(f"Got '{self.current_token['value']}', Expected '{expected_kind}'")

    def error(self, message):
        print(f"ERROR: Parser error at line: {message}")
        self.is_error = True
