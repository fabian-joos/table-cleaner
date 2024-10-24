from tkinter import ttk

class TcView():
    def __init__(self, root):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.setup_window()
        self.init_widgets()
        self.place_widgets()

    def setup_window(self):
        self.root.title("Title - TcView v0.1")
        self.root.geometry("800x600")

    def init_widgets(self):
        self.label = ttk.Label(self.root, text="Hello, Tkinter!")
        self.load_file_button = ttk.Button(self.root, text="Load file")
        self.load_file_entry = ttk.Entry(self.root)

    def place_widgets(self):
        self.label.pack(side="top")
        self.load_file_button.pack(side="top", fill="x", padx=10)
        self.load_file_entry.pack(side="top", fill="x", padx=10)