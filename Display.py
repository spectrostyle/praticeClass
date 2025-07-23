import tkinter as tk


class Display:
    def __init__(self, width=640, height=640):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")

        self.text = tk.Text(self.root, height=10, width=30, font=("Courier", 12))
        self.text.pack(expand=True, fill='both')

    def run(self):
        self.root.mainloop()

    def print(self, text):
        self.text.insert('end', text + '\n')
        self.text.see('end')

    def clear(self):
        self.text.delete(1.0, 'end')
