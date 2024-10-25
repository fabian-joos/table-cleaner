import pandas as pd
from tkinter import filedialog

class TcModel():
    def __init__(self):
        self.model = None
        self.load_file_filename = ""
        self.df = pd.DataFrame()
        self.df_columns = []

    def load_file(self):
        self.load_file_filename = filedialog.askopenfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")])
        if self.load_file_filename:
            self.df = pd.read_csv(self.load_file_filename, sep=";", encoding="utf-8")
            self.df_columns = list(self.df.columns)

    def save_file(self):
        save_file_filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")])
        self.df.to_csv(save_file_filename, sep=";", encoding="utf-8", index=False)

    def replace(self, lookup_column, lookup_expression, replace_expression):
        if lookup_column in self.df_columns:
            self.df[lookup_column] = self.df[lookup_column].str.replace(lookup_expression, replace_expression)