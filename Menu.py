class Menu:
    def __init__(self, title, options, display):
        self.title = title
        self.options = options

        self.display = display

    def display_this_menu(self):
        for x in self.options:
            self.display.print(x)
