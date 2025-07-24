from scenes import sceneManager


class Menu:
    def __init__(self, title, options, mainWindow, navigable):
        self.title = title
        self.options = options
        self.navigable = navigable
        self.mainWindow = mainWindow

        self.selected_option = None
        self.index = 0


    def display_this_menu(self):

        if self.navigable is True or self.navigable is False:
            self.mainWindow.root.bind("<Down>", self.key_press)
            self.mainWindow.root.bind("<Up>", self.key_press)
            self.mainWindow.root.bind("<Return>", self.key_press)

            for i, option in enumerate(self.options):
                if i == self.index:
                    self.mainWindow.print(f"> {option}\n")
                else:
                    self.mainWindow.print(f"  {option}\n")


    def key_press(self, key):

        if key.keysym == "Down":
            self.index = (self.index + 1) % len(self.options)
        elif key.keysym == "Up":
            self.index = (self.index - 1) % len(self.options)
        self.mainWindow.clear()
        self.display_this_menu()

        if key.keysym == "Return":
            self.selected_option = self.options[self.index].lower().replace(" ", "_")
            self.handle_selected_option()


    def handle_selected_option(self):
        sceneManager.switch_scenes(self.selected_option, self.mainWindow)
