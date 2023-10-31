from core.util import is_number, is_letter


reserved_words = [
    'awakeHero', 'sealDarkness', 'takeThis', 'heyListen'
]

data_types = [
    'rupees', 'zoras'
]

class Tokenizer:
    @staticmethod
    def tokenize(string:str) -> list:
        string += '\n'
        current = 0
        position = 0
        line = 1
        tokens = []

        while current < len(string):
            char = string[current]

            if char == "-":
                tokens.append({
                    'kind': 'operator',
                    'value': '-',
                    'position': position,
                    'line': line
                })

                current += 1
                position += 1
                continue

            if char == ";":
                tokens.append({
                    'kind': 'end_statement',
                    'value': ';',
                    'position': position,
                    'line': line
                })

                current += 1
                position += 1
                continue

            if char == "+":
                tokens.append({
                    'kind': 'operator',
                    'value': '+',
                    'position': position,
                    'line': line
                })

                current += 1
                continue

            if char == "=":
                tokens.append({
                    'kind': 'attribution',
                    'value': '=',
                    'position': position,
                    'line': line
                })

                current += 1
                position += 1
                continue

            if char == " ":
                current += 1
                position += 1
                continue

            if char == "\n" or char == "\r":
                position = 0
                current += 1
                line += 1
                continue

            if is_number(char):
                value = ''

                while is_number(char):
                    value += char
                    current += 1
                    position += 1
                    char = string[current]

                if char == '.':
                    value += char
                    current += 1
                    position += 1
                    char = string[current]

                    while is_number(char):
                        value += char
                        current += 1
                        position += 1
                        char = string[current]

                    tokens.append({
                        'kind': 'zoras',
                        'value': value,
                        'position': position,
                        'line': line
                    })

                    continue

                tokens.append({
                    'kind': 'rupees',
                    'value': value,
                    'position': position,
                    'line': line
                })
                continue

            if is_letter(char):
                value = ''

                while is_letter(char):
                    value += char
                    current += 1
                    position += 1
                    char = string[current]

                if value in reserved_words:
                    tokens.append({
                        "kind": value,
                        'value': value,
                        'position': position,
                        'line': line
                    })
                elif value in data_types:
                    tokens.append({
                        'kind': 'data_type',
                        'value': value,
                        'position': position,
                        'line': line
                    })
                else:
                    tokens.append({
                        'kind': 'identifier',
                        'value': value,
                        'position': current,
                        'line': line
                    })

                if char == ";":
                    tokens.append({
                        'kind': 'end_statement',
                        'value': ';',
                        'position': position,
                        'line': line
                    })

                    current += 1
                    position += 1
                    continue

                if char == "(":
                    tokens.append({
                        'kind': 'left_parenthesis',
                        'value': '(',
                        'position': position,
                        'line': line
                    })

                    current += 1
                    position += 1
                    continue

                if char == ")":
                    tokens.append({
                        'kind': 'right_parenthesis',
                        'value': ')',
                        'position': position,
                        'line': line
                    })

                    current += 1
                    position += 1
                    continue

                current += 1
                continue

            if char == '#':
                current += 1
                position += 1
                line -= 1
                char = string[current]
                while char != "#":
                    current += 1
                    position += 1
                    char = string[current]

                    if char == "\n" or char == "\r":
                        line -= 1

                current += 1
                position += 1
                continue

            raise SyntaxError(f'Invalid character: {char}')
        return tokens
