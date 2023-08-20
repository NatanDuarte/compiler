class WordAutomato:
    def __init__(self):
        self.state = 'q0'
        self.word = ''

    def _proccess_char(self, char):
        transitions = {
            'q0': {
                'letra': 'q1'
            },
            'q1': {
                'letra': 'q1',
                'digito': 'q1',
                '_': 'q1',
                'outro': 'q2'
            }
        }

        if char.isalpha():
            proximo_state = transitions[self.state]['letra']
        elif char.isdigit():
            proximo_state = transitions[self.state]['digito']
        elif char == '_':
            proximo_state = transitions[self.state]['_']
        else:
            proximo_state = transitions[self.state]['outro']

        self.state = proximo_state

        if self.state != 'q2':
            self.word += char

    def processar_cadeia(self, cadeia):
        for char in cadeia:
            self._proccess_char(char)

    def reset(self):
        self.state = 'q0'
        self.word = ''

    def verificar_word(self):
        return self.state == 'q2' 

    def obter_word_concatenada(self):
        return self.word