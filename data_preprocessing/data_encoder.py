class DataEncoder:
    def encode_categorical(self, data):
        """Encodes categorical columns into numerical values."""
        categorical_columns = data.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            data[column] = data[column].astype('category').cat.codes
            print(f"Encoded column: {column}")
        return data
