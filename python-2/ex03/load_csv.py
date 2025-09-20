import pandas as pd


def load(path: str):
    """
    args (path: str) path of the file to open
    Load and return dataset
    """
    try:
        df = pd.read_csv(path)
    except Exception as error:
        print(error)
        return None

    df = pd.read_csv(path)
    return df
