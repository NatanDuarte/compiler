class TextBuffer:
    def __init__(self, text):
        self.text = text
        self.position = 0

    def peek(self, n=1):
        end_position = self.position + n
        return self.text[self.position:end_position]

    def consume(self, n=1):
        value = self.peek(n)
        self.position += n
        return value

    def has_next(self):
        return self.position < len(self.text)
