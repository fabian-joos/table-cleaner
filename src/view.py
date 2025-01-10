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

        self.main_frame = ttk.Frame(self.root)

        self.control_frame = ttk.Frame(self.main_frame, width=350)
        self.view_frame = ttk.Frame(self.main_frame)


        # Control Frame BEGIN
        self.load_file_button = ttk.Button(self.control_frame, text="Load file")
        self.load_file_entry = ttk.Entry(self.control_frame)
        self.load_file_separator = ttk.Separator(self.control_frame, orient='horizontal')

        self.lookup_column_label = ttk.Label(self.control_frame, text="Select lookup column:")
        self.lookup_column_combobox = ttk.Combobox(self.control_frame, state='readonly')
        self.lookup_expression_label = ttk.Label(self.control_frame, text="Enter lookup expression:")
        self.lookup_expression_entry = ttk.Entry(self.control_frame)
        self.lookup_expression_check = ttk.Button(self.control_frame, text="Check")
        self.lookup_separator = ttk.Separator(self.control_frame, orient='horizontal')

        self.replace_expression_label = ttk.Label(self.control_frame, text="Enter replace expression:")
        self.replace_expression_entry = ttk.Entry(self.control_frame)
        self.replace_button = ttk.Button(self.control_frame, text="Replace")
        self.replace_separator = ttk.Separator(self.control_frame, orient='horizontal')

        self.save_file_button = ttk.Button(self.control_frame, text="Save file")
        # Control Frame END


        # Treeview Frame BEGIN
        self.treeview = ttk.Treeview(self.view_frame, show="headings")
        # Treeview Frame END


        # Status Bar BEGIN
        self.status_bar = ttk.Label(self.root, text="Status bar")
        # Status Bar END

    def pack_widgets(self):
        self.main_frame.pack(side="top", fill="both", expand=True)
        self.main_frame.pack_propagate(False)

        self.control_frame.pack(side="left", fill="y")
        self.control_frame.pack_propagate(False)

        self.view_frame.pack(side="left", fill="both", expand=True)
        self.view_frame.pack_propagate(False)


        # Control Frame BEGIN
        self.load_file_button.pack(side="top", fill="x", padx=10)
        self.load_file_entry.pack(side="top", fill="x", padx=10)
        self.load_file_separator.pack(side="top", fill="x", padx=10, pady=10)

        self.lookup_column_label.pack(side="top", fill="x", padx=10)
        self.lookup_column_combobox.pack(side="top", fill="x", padx=10)
        self.lookup_expression_label.pack(side="top", fill="x", padx=10)
        self.lookup_expression_entry.pack(side="top", fill="x", padx=10)
        self.lookup_expression_check.pack(side="top", fill="x", padx=10)
        self.lookup_separator.pack(side="top", fill="x", padx=10, pady=10)

        self.replace_expression_label.pack(side="top", fill="x", padx=10)
        self.replace_expression_entry.pack(side="top", fill="x", padx=10)
        self.replace_button.pack(side="top", fill="x", padx=10)
        self.replace_separator.pack(side="top", fill="x", padx=10, pady=10)

        self.save_file_button.pack(side="top", fill="x", padx=10)
        # Control Frame END


        # Treeview Frame BEGIN
        self.treeview.pack(side="top", fill="both", expand=True)
        # Treeview Frame END


        # Status Bar BEGIN
        self.status_bar.pack(side="left", padx=5)
        # Status Bar END

    def dev_default(self):
        self.lookup_expression_entry.delete(0, "end")
        self.lookup_expression_entry.insert(0, "FindMe")
        self.replace_expression_entry.delete(0, "end")
        self.replace_expression_entry.insert(0, "NewStuff")