from tkinter import ttk

class TcView():
    def __init__(self, root):
        self.root = root
        self.setup_gui()
        self.dev_default()

    def setup_gui(self):
        self.setup_window()
        self.init_widgets()
        self.pack_widgets()

    def setup_window(self):
        self.root.title("Frooter Table Cleaner - v0.1")
        self.root.geometry("400x300")

    def init_widgets(self):
        self.label = ttk.Label(self.root, text="Hello!")
        self.load_file_button = ttk.Button(self.root, text="Load file")
        self.load_file_entry = ttk.Entry(self.root)
        self.load_file_status = ttk.Label(self.root, text="No file loaded")
        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.lookup_column_label = ttk.Label(self.root, text="Select lookup column:")
        self.lookup_column_combobox = ttk.Combobox(self.root, state='readonly')
        self.lookup_expression_label = ttk.Label(self.root, text="Enter lookup expression:")
        self.lookup_expression_entry = ttk.Entry(self.root)

    def pack_widgets(self):
        self.label.pack(side="top")
        self.load_file_button.pack(side="top", fill="x", padx=10)
        self.load_file_entry.pack(side="top", fill="x", padx=10)
        self.load_file_status.pack(side="top", fill="x", padx=10)
        self.separator.pack(side="top", fill="x", padx=10, pady=10)
        self.lookup_column_label.pack(side="top", fill="x", padx=10)
        self.lookup_column_combobox.pack(side="top", fill="x", padx=10)
        self.lookup_expression_label.pack(side="top", fill="x", padx=10)
        self.lookup_expression_entry.pack(side="top", fill="x", padx=10)

    def dev_default(self):
        self.lookup_expression_entry.delete(0, "end")
        self.lookup_expression_entry.insert(0, "Enter expression here")