import pandas as pd


def carga_data():
    data = pd.read_csv('data/kamino_aloj_final.csv')
    return data
