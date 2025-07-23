class Menu:
    def __init__(self, title, options, display, navigable, when_selected=None):
        self.title = title
        self.options = options
        self.navigable = navigable
        self.index = 0

        self.display = display

        self.when_selected = when_selected

    def display_this_menu(self):

        if self.navigable is True:

            self.display.root.bind("<Down>", self.key_press)
            self.display.root.bind("<Up>", self.key_press)
            self.display.root.bind("<Return>", self.key_press)

            for i, option in enumerate(self.options):
                if i == self.index:
                    self.display.print(f"> {option}\n")
                else:
                    self.display.print(f"  {option}\n")

    def key_press(self, key):
        if key.keysym == "Down":
            self.index = (self.index + 1) % len(self.options)
        elif key.keysym == "Up":
            self.index = (self.index - 1) % len(self.options)

        self.display.clear()
        self.display_this_menu()

        if key.keysym == "Return":
            self.display.clear()
            if self.when_selected:
                transition_scene = self.options[self.index]
                self.when_selected(transition_scene)

        else:
            pass
