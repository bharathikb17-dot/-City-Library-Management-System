import pandas as pd
import os

def read_data(file):
    if not os.path.exists(file):
        return pd.DataFrame()
    return pd.read_csv(file)

def write_data(file, df):
    df.to_csv(file, index=False)