from data_loader import DataLoader
from data_cleaner import DataCleaner

if __name__ == "__main__":
    filepath = input("Enter the path to your CSV or Excel file: ")
    loader = DataLoader(filepath=filepath)
    data = loader.load_data()

    if not data.empty:
        cleaner = DataCleaner(drop_threshold=0.5)

        # First, drop columns with high missing values
        data = cleaner.drop_by_threshold(data)

        # Ask user for imputation method for each column
        data = cleaner.interactive_imputation(data)

        # Show the final cleaned data
        print("\nFinal Processed Data:")
        print(data.head())
