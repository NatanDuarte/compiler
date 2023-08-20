
class Token:
    def __init__(self, value, kind):
        self.value = value
        self.kind = kind

    def __str__(self):
        return f"Token({self.kind}, {self.value})"
