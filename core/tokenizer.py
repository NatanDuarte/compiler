from core.util import is_number, is_letter

reserved_words = [
    'init', 'end', 'var'
]

data_types = [
    'int', 'float'
]

functions = {
    'write': lambda x: print(x)
}

class Tokenizer:
    @staticmethod
    def tokenize(string:str) -> list:
        string += '\n'
        current = 0
        line = 1
        tokens = []

        while current < len(string):
            char = string[current]

            if char == "-":
                tokens.append({
                    'kind': 'operator',
                    'value': '+',
                    'position': current,
                    'line': line
                })

                current += 1
                continue

            if char == ";":
                tokens.append({
                    'kind': 'end_statement',
                    'value': ';',
                    'position': current,
                    'line': line
                })

                current += 1
                continue

            if char == "+":
                tokens.append({
                    'kind': 'operator',
                    'value': '+',
                    'position': current,
                    'line': line
                })

                current += 1
                continue

            if char == "=":
                tokens.append({
                    'kind': 'attribution',
                    'value': '=',
                    'position': current,
                    'line': line
                })

                current += 1
                continue

            if char == "(":
                tokens.append({
                    'kind': 'left_parenthesis',
                    'value': '(',
                    'position': current,
                    'line': line
                })
                
                current += 1
                continue

            if char == ")":
                tokens.append({
                    'kind': 'right_parenthesis',
                    'value': ')',
                    'position': current,
                    'line': line
                })

                current += 1
                continue

            if char == " ":
                current += 1
                continue

            if char == "\n" or char == "\r":
                current += 1
                line += 1
                continue

            if is_number(char):
                value = ''

                while is_number(char):
                    value += char
                    current += 1
                    char = string[current]

                if char == '.':
                    value += char
                    current += 1
                    char = string[current]

                    while is_number(char):
                        value += char
                        current += 1
                        char = string[current]

                    tokens.append({
                        'kind': 'float',
                        'value': value,
                        'position': current,
                        'line': line
                    })

                    continue

                tokens.append({
                    'kind': 'integer',
                    'value': value,
                    'position': current,
                    'line': line
                })
                continue

            if is_letter(char):
                value = ''

                while is_letter(char):
                    value += char
                    current += 1
                    char = string[current]

                if value in reserved_words:
                    tokens.append({
                        "kind": value,
                        'value': value,
                        'position': current,
                        'line': line
                    })
                    pass
                elif value in data_types:
                    tokens.append({
                        'kind': 'data_type',
                        'value': value,
                        'position': current,
                        'line': line
                    })
                else:
                    tokens.append({
                        'kind': 'identifier',
                        'value': value,
                        'position': current,
                        'line': line
                    })

                current += 1
                continue

            if char == '#':
                current += 1
                char = string[current]
                while char != "#":
                    current += 1
                    char = string[current]

                current += 1
                continue

            raise SyntaxError(f'Invalid character: {char}')
        return tokens
