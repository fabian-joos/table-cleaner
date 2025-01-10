import pandas as pd
from tkinter import filedialog

class TcModel():
    def __init__(self):
        self.model = None
        self.loaded_file_filename = ""
        self.df = pd.DataFrame()
        self.df_columns = []

    def load_file(self):
        '''Load CSV file to DataFrame and update df_columns'''
        loaded_file_filename_current = str(self.loaded_file_filename)
        self.loaded_file_filename = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if self.loaded_file_filename:
            self.df = pd.read_csv(self.loaded_file_filename, sep=";", encoding="utf-8")
            self.df_columns = list(self.df.columns)
        else:
            self.loaded_file_filename = loaded_file_filename_current

    def save_file(self):
        '''Save DataFrame to CSV file'''
        save_file_filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if save_file_filename:
            self.df.to_csv(save_file_filename, sep=";", encoding="utf-8", index=False)

    def replace_action(self, lookup_column, lookup_expression, replace_expression, replace_instruction):
        '''Replace lookup_expression with replace_expression in lookup_column of DataFrame df'''
        if lookup_column in self.df_columns:
            if replace_instruction == "replace text with":
                self.df[lookup_column] = self.df[lookup_column].str.replace(lookup_expression, replace_expression)
            elif replace_instruction == "replace cell with":
                self.df[lookup_column] = self.df[lookup_column].apply(lambda x: replace_expression if lookup_expression in x else x)