class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def example():
    # Computer 2 + 3 * 0.1
    code = [
            ('const', 2),
            ('const', 3),
            ('const', 0.1),
            ('mul',),
            ('add',),
            ]
    m = Machine()
