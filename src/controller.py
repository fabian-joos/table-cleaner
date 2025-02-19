from tkinter import filedialog

class TcController():
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.setup()

        self.filetypes = [("CSV files", "*.csv"),
                          ("TXT files", "*.txt")]

    def setup(self):
        '''Setup event handlers'''
        self.view.load_file_button.config(command=self.load_file_button_click)
        self.view.save_as_button.config(command=self.save_as_button_click)
        self.view.replace_button.config(command=self.replace_button_click)



    def load_file_button_click(self):
        '''Load file button click event handler.
        Call model load_file method and update view'''
        dialog_filename = self.dialog_open_filename()
        if dialog_filename:
            self.model.load_file_to_dataframe(dialog_filename)
            self.update_view()
            self.view.status_bar.config(text=f"File loaded, shape: {self.model.df.shape}")


    def save_as_button_click(self):
        '''Save file button click event handler.
        Call model save_file method and update view'''
        dialog_filename = self.dialog_save_filename()
        if dialog_filename:
            self.model.save_dataframe_to_file(dialog_filename)
            self.update_load_file_entry(dialog_filename)
            self.view.status_bar.config(text="File saved")



    def dialog_open_filename(self):
        filename = filedialog.askopenfilename(
            defaultextension=".csv",
            filetypes=self.filetypes)
        return filename


    def dialog_save_filename(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=self.filetypes)
        return filename



    def lookup_expression_check_click(self):
        '''Lookup expression check button click event handler.
        Checks if lookup expression is found in lookup column and updates view with status'''
        lookup_column = self.view.lookup_column_combobox.get()
        lookup_expression = self.view.lookup_expression_entry.get()
        lookup_result = self.model.df[lookup_column].str.contains(lookup_expression)
        self.view.status_bar.config(
            text=f"Lookup expression found in {lookup_result.sum()} rows")


    def replace_button_click(self):
        '''Replace button click event handler.
        Call model replace method and update view'''
        lookup_column = self.view.lookup_column_combobox.get()
        lookup_expression = self.view.lookup_expression_entry.get()
        replace_expression = self.view.replace_expression_entry.get()
        replace_instruction = self.view.replace_instruction_combobox.get()
        self.model.replace_action(lookup_column,
                                  lookup_expression,
                                  replace_expression,
                                  replace_instruction)
        self.view.status_bar.config(text="Replacements made")
        self.update_treeview_data()



    def update_view(self):
        self.insert_treeview_data()
        self.update_column_combobox()
        self.update_load_file_entry(self.model.loaded_filename)


    def insert_treeview_data(self):
        self.view.treeview['columns'] = self.model.df_columns
        for column in self.model.df_columns:
            self.view.treeview.heading(column, text=column)
        self.update_treeview_data()


    def update_treeview_data(self):
        # delete all existing entries
        for item in self.view.treeview.get_children():
            self.view.treeview.delete(item)
        # insert entries from dataframe
        for i in range(0, self.model.df.shape[0]):
            self.view.treeview.insert(
                parent="", index=i, values=list(self.model.df.iloc[i, :]))


    def update_column_combobox(self):
        self.view.lookup_column_combobox.config(values=self.model.df_columns)
        self.view.lookup_column_combobox.set(self.model.df_columns[0])


    def update_load_file_entry(self, filename=None):
        '''Update the load file entry with the given filename or the model's loaded file filename'''
        if filename is None:
            filename = self.model.loaded_filename
        self.view.load_file_entry.delete(0, "end")
        self.view.load_file_entry.insert(0, filename)
