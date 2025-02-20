from tkinter import filedialog

class TcController():
    """
    TcController is a controller class that manages the
    interaction between the view and the model in an MVC architecture.
    It handles user inputs from the view, updates the model, and refreshes the view accordingly.

    """

    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.filetypes = [("CSV files", "*.csv"),
                          ("TXT files", "*.txt")]

        self.setup()

    def setup(self):
        """
        Setup event handlers

        """

        self.view.load_file_button.config(command=self.load_file_button_click)
        self.view.save_as_button.config(command=self.save_as_button_click)
        self.view.replace_button.config(command=self.replace_button_click)



    def load_file_button_click(self):
        """
        Load file button click event handler.
        Call model load_file method and update view

        """

        dialog_filename = self.dialog_open_filename()
        if dialog_filename:
            self.model.load_file_to_dataframe(dialog_filename)
            self.update_view()
            self.view.status_bar.config(text=f"File loaded, shape: {self.model.df.shape}")


    def save_as_button_click(self):
        """
        Save file button click event handler.
        Call model save_file method and update view

        """

        dialog_filename = self.dialog_save_filename()
        if dialog_filename:
            self.model.save_dataframe_to_file(dialog_filename)
            self.update_load_file_entry(dialog_filename)
            self.view.status_bar.config(text="File saved")



    def dialog_open_filename(self):
        """
        Opens an open file dialog and returns the selected filename.
        The dialog allows the user to select a file for opening.
        The default file extension is set to ".csv", and the available file
        types are specified by the `self.filetypes` attribute.
        Returns:
            str: The selected filename, including the path.

        """

        filename = filedialog.askopenfilename(
            defaultextension=".csv",
            filetypes=self.filetypes)
        return filename


    def dialog_save_filename(self):
        """
        Opens a save file dialog and returns the selected filename.
        The dialog allows the user to specify a filename for saving a file.
        The default file extension is set to ".csv", and the available file
        types are specified by the `self.filetypes` attribute.
        Returns:
            str: The selected filename, including the path.

        """

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=self.filetypes)
        return filename



    def lookup_expression_check_click(self):
        """
        Lookup expression check button click event handler.
        Checks if lookup expression is found in lookup column and updates view with status

        """

        lookup_column = self.view.lookup_column_combobox.get()
        lookup_expression = self.view.lookup_expression_entry.get()
        lookup_result = self.model.df[lookup_column].str.contains(lookup_expression)
        self.view.status_bar.config(
            text=f"Lookup expression found in {lookup_result.sum()} rows")


    def replace_button_click(self):
        """
        Replace button click event handler.
        Call model replace method and update view.

        """

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
        """
        Updates the view by refreshing the treeview data, updating the column combobox,
        and setting the load file entry with the loaded filename from the model.

        """

        self.insert_treeview_data()
        self.update_column_combobox()
        self.update_load_file_entry(self.model.loaded_filename)


    def insert_treeview_data(self):
        """
        Inserts data into the treeview widget.
        This method sets up the columns of the treeview widget based on the 
        dataframe columns from the model. It then updates the treeview with 
        the current data from the model.

        """

        self.view.treeview["columns"] = self.model.df_columns
        for column in self.model.df_columns:
            self.view.treeview.heading(column, text=column)
        self.update_treeview_data()


    def update_treeview_data(self):
        """
        Updates the view's treeview widget with data from the model's dataframe.
        This method first clears all existing entries in the treeview widget.
        Then, it iterates over the rows of the dataframe in the model and inserts
        each row as a new entry in the treeview.

        """

        # delete all existing entries
        for item in self.view.treeview.get_children():
            self.view.treeview.delete(item)
        # insert entries from dataframe
        for i in range(0, self.model.df.shape[0]):
            self.view.treeview.insert(
                parent="", index=i, values=list(self.model.df.iloc[i, :]))


    def update_column_combobox(self):
        """
        Updates the values of the lookup column combobox in the view with the 
        column names from the model's dataframe. 
        Sets the combobox to the first column name by default.

        """

        self.view.lookup_column_combobox.config(values=self.model.df_columns)
        self.view.lookup_column_combobox.set(self.model.df_columns[0])


    def update_load_file_entry(self, filename=None):
        """
        Update the load file entry with the given filename or the model's loaded file filename

        """

        if filename is None:
            filename = self.model.loaded_filename
        self.view.load_file_entry.delete(0, "end")
        self.view.load_file_entry.insert(0, filename)
