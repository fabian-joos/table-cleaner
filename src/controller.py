class TcController():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.setup()

    def setup(self):
        self.view.load_file_button.config(command=self.load_file_button_click)
        self.view.save_file_button.config(command=self.save_file_button_click)
        self.view.lookup_column_combobox.config(values=self.model.df_columns)
        self.view.lookup_expression_check.config(command=self.lookup_expression_check_click)
        self.view.replace_button.config(command=self.replace_button_click)

    def load_file_button_click(self):
        self.model.load_file()
        self.view.load_file_entry.delete(0, "end")
        self.view.load_file_entry.insert(0, self.model.load_file_filename)
        self.view.load_file_status.config(text=f"File loaded, shape: {self.model.df.shape}")
        self.view.lookup_column_combobox.config(values=self.model.df_columns)

    def save_file_button_click(self):
        self.model.save_file()
        self.view.save_file_status.config(text="File saved")
    
    def replace_button_click(self):
        lookup_column = self.view.lookup_column_combobox.get()
        lookup_expression = self.view.lookup_expression_entry.get()
        replace_expression = self.view.replace_expression_entry.get()
        self.model.replace(lookup_column, lookup_expression, replace_expression)
        self.view.replace_status.config(text="Replacements made")

    def lookup_expression_check_click(self):
        lookup_column = self.view.lookup_column_combobox.get()
        lookup_expression = self.view.lookup_expression_entry.get()
        lookup_result = self.model.df[lookup_column].str.contains(lookup_expression)
        self.view.lookup_expression_status.config(text=f"Lookup expression found in {lookup_result.sum()} rows")