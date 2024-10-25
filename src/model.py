import pandas as pd
from tkinter import filedialog

class TcModel():
    def __init__(self):
        self.model = None
        self.df = None

    def load_file(self):
        self.load_file_filename = filedialog.askopenfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")]
        )
        if self.load_file_filename:
            self.df = pd.read_csv(self.load_file_filename, sep=";", encoding="utf-8")
            print(f"model.df.shape: {self.df.shape}")