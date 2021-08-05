import pandas as pd


def get_live_data():
    return pd.read_csv('dataset.csv')
