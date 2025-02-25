import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    takes a path as argument, writes the dimensions
    of the data set and returns it.
    returns:
    - tuple: DataFrame dimensions
    - None: if file doesn't exist or format error
    """
    try:
        df = pd.read_csv(path)

        if df.empty:
            print("Error: The dataset is empty.")
            return None

        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or corrupted.")
    except pd.errors.ParserError:
        print("Error: The file is not a valid CSV format.")
    except Exception as e:
        print(f"Unexpected error:: {e}")
