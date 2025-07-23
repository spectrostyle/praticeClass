class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        for x in self.options:
            print(x)
        pass

