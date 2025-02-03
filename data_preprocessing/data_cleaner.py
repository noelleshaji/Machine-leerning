import pandas as pd

class DataCleaner:
    def __init__(self, drop_threshold=0.5):
        self.drop_threshold = drop_threshold

    def drop_by_threshold(self, df):
        """Drops columns where the percentage of missing values is greater than the threshold."""
        missing_percentage = df.isnull().mean()
        columns_to_drop = missing_percentage[missing_percentage > self.drop_threshold].index
        print(f"Dropping columns with >{self.drop_threshold * 100}% missing values: {list(columns_to_drop)}")
        df = df.drop(columns=columns_to_drop)
        return df

    def fill_missing_mean(self, df, column):
        """Fills missing values in a specific column using the mean."""
        df[column] = df[column].fillna(df[column].mean())
        print(f"Filled missing values in '{column}' using mean.")
        return df

    def fill_missing_median(self, df, column):
        """Fills missing values in a specific column using the median."""
        df[column] = df[column].fillna(df[column].median())
        print(f"Filled missing values in '{column}' using median.")
        return df

    def fill_missing_ffill(self, df, column):
        """Fills missing values in a specific column using forward fill."""
        df[column] = df[column].fillna(method='ffill')
        print(f"Filled missing values in '{column}' using forward fill.")
        return df

    def fill_missing_bfill(self, df, column):
        """Fills missing values in a specific column using backward fill."""
        df[column] = df[column].fillna(method='bfill')
        print(f"Filled missing values in '{column}' using backward fill.")
        return df

    def interactive_imputation(self, df):
        """Asks user which columns to impute and which method to use."""
        missing_columns = df.columns[df.isnull().any()]
        if not missing_columns.any():
            print("No missing values to fill.")
            return df

        print("\nColumns with missing values:", list(missing_columns))

        for column in missing_columns:
            print(f"\nChoose an imputation method for '{column}':")
            print("1 - Mean")
            print("2 - Median")
            print("3 - Forward Fill")
            print("4 - Backward Fill")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                df = self.fill_missing_mean(df, column)
            elif choice == "2":
                df = self.fill_missing_median(df, column)
            elif choice == "3":
                df = self.fill_missing_ffill(df, column)
            elif choice == "4":
                df = self.fill_missing_bfill(df, column)
            else:
                print(f"Invalid choice. Skipping column '{column}'.")
        
        return df
