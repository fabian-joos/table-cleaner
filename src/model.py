import pandas as pd

class TcModel():
    def __init__(self):
        self.model = None
        self.loaded_filename = ""
        self.df = pd.DataFrame()
        self.df_columns = []


    def load_file_to_dataframe(self, filename, sep=";", encoding="utf-8"):
        """Load CSV file to DataFrame, update instance attributes df_columns and loaded_filename"""
        self.df = pd.read_csv(filename, sep=sep, encoding=encoding)
        self.df_columns = list(self.df.columns)
        self.loaded_filename = filename


    def save_dataframe_to_file(self, filename, sep=";", encoding="utf-8"):
        """Save DataFrame to CSV file"""
        self.df.to_csv(filename, sep=sep, encoding=encoding, index=False)
        self.loaded_filename = filename


    def replace_action(self,
                       lookup_column,
                       lookup_expression,
                       replace_expression,
                       replace_instruction):
        """Replace lookup_expression with replace_expression in lookup_column of DataFrame df"""
        if lookup_column in self.df_columns:
            if replace_instruction == "replace text with":
                self.df[lookup_column] = self.df[lookup_column] \
                    .str.replace(lookup_expression, replace_expression)
            elif replace_instruction == "replace cell with":
                self.df[lookup_column] = self.df[lookup_column] \
                    .apply(lambda x: replace_expression if lookup_expression in x else x)
