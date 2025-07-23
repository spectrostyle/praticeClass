class Menu:
    def __init__(self, title, options, display, navigatable):
        self.title = title
        self.options = options
        self.navigatable = navigatable
        self.index = 0

        self.display = display

    def display_this_menu(self):

        if self.navigatable is True:

            self.display.root.bind("<Down>", self.main_key_press)
            self.display.root.bind("<Up>", self.main_key_press)
            #self.display.root.bind("<Return>", main_selection)

            for i, option in enumerate(self.options):
                if i == self.index:
                    self.display.print(f"> {option}\n")
                else:
                    self.display.print(f"  {option}\n")

    def main_key_press(self, key):
        if key.keysym == "Down":
            self.index = (self.index + 1) % len(self.options)
        elif key.keysym == "Up":
            self.index = (self.index - 1) % len(self.options)

        self.display.clear()
        self.display_this_menu()

