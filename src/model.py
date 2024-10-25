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