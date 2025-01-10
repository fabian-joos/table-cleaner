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
        self.root.geometry(f"{int(0.6*self.root.winfo_screenwidth())}x{int(0.8*self.root.winfo_screenheight())}") #default window size when restored
        self.root.state('zoomed')

    def init_widgets(self):
        # main frames
        self.view_frame = ttk.Frame(self.root)
        self.control_frame = ttk.Frame(self.root, height=30)
        self.control_frame2 = ttk.Frame(self.root, height=30)
        self.file_handling_frame = ttk.Frame(self.root, height=30)

        # treeview frame
        self.treeview = ttk.Treeview(self.view_frame, show="headings")

        # control frame
        self.lookup_column_label = ttk.Label(self.control_frame, text="If ")
        self.lookup_column_combobox = ttk.Combobox(self.control_frame, state="readonly")
        self.lookup_expression_label = ttk.Label(self.control_frame, text=" contains ")
        self.lookup_expression_entry = ttk.Entry(self.control_frame)

        self.replace_instruction_combobox = ttk.Combobox(self.control_frame, state="readonly")
        self.replace_instruction_combobox_values = ("replace text with", "replace cell with")
        self.replace_instruction_combobox["values"] = self.replace_instruction_combobox_values
        self.replace_instruction_combobox.set(self.replace_instruction_combobox_values[0])

        self.replace_expression_label = ttk.Label(self.control_frame, text=" replace text with ")
        self.replace_expression_entry = ttk.Entry(self.control_frame)
        self.replace_button = ttk.Button(self.control_frame, text="Replace")

        # control frame 2
        self.placeholder_label = ttk.Label(self.control_frame2, text="placeholder")

        # file handling frame
        self.load_file_entry = ttk.Entry(self.file_handling_frame, width=120)
        self.load_file_button = ttk.Button(self.file_handling_frame, text="Load file", width=20)
        self.save_file_button = ttk.Button(self.file_handling_frame, text="Save file", width=20)

        # status bar
        self.status_bar = ttk.Label(self.root, text="Status bar")

    def pack_widgets(self):
        self.view_frame.pack(side="top", fill="both", expand=True)
        self.view_frame.pack_propagate(False)

        self.control_frame.pack(side="top", fill="x", pady=5)
        self.control_frame.pack_propagate(False)

        #self.control_frame2.pack(side="top", fill="x", pady=5)
        #self.control_frame2.pack_propagate(False)

        self.file_handling_frame.pack(side="top", fill="x", pady=5)
        self.file_handling_frame.pack_propagate(False)

        # treeview frame
        self.treeview.pack(side="top", fill="both", expand=True)

        # control frame
        self.lookup_column_label.pack(side="left", fill="x", padx=10)
        self.lookup_column_combobox.pack(side="left", fill="x", padx=10)
        self.lookup_expression_label.pack(side="left", fill="x", padx=10)
        self.lookup_expression_entry.pack(side="left", fill="x", padx=10)

        self.replace_instruction_combobox.pack(side="left", fill="x", padx=10)
        self.replace_expression_entry.pack(side="left", fill="x", padx=10, expand=True)
        self.replace_button.pack(side="left", fill="x", padx=10)

        # control frame 2
        self.placeholder_label.pack(side="left")

        # fine handling frame
        self.save_file_button.pack(side="right", fill="x", padx=10, pady=2)
        self.load_file_button.pack(side="right", fill="x", padx=10, pady=2)
        self.load_file_entry.pack(side="right", fill="x", padx=11, pady=2)

        # status bar
        self.status_bar.pack(side="left", padx=5, pady=5)

    def dev_default(self):
        self.lookup_expression_entry.delete(0, "end")
        self.lookup_expression_entry.insert(0, "FindMe")
        self.replace_expression_entry.delete(0, "end")
        self.replace_expression_entry.insert(0, "NewStuff")