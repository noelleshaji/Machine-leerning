import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        try:
            if self.filepath.endswith(".csv"):
                self.data = pd.read_csv(self.filepath)
            elif self.filepath.endswith((".xls", ".xlsx")):
                self.data = pd.read_excel(self.filepath)
            else:
                raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

            print(f"Data loaded successfully with {self.data.shape[0]} rows and {self.data.shape[1]} columns.")
            print("\nInitial Missing Values per Column:")
            print(self.data.isnull().sum())
            return self.data
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error
