class TcController():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.setup()

    def setup(self):
        self.view.load_file_button.config(command=self.load_file_button_click)

    def load_file_button_click(self):
        self.model.load_file()
        self.view.load_file_entry.delete(0, "end")
        self.view.load_file_entry.insert(0, self.model.load_file_filename)
        self.view.load_file_status.config(text=f"File loaded, shape: {self.model.df.shape}")
        self.view.lookup_column_combobox.config(values=self.model.df_columns)