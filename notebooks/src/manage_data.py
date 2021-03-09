import pandas as pd


def carga_data():
    data = pd.read_csv('data/kamino_aloj_final.csv')
    #rest = pd.read_csv('data/kamino_rest_final.csv')
    #patr = pd.read_csv('data/kamino_patr_final.csv')
    return data #rest, patr

def lista_localidades():
    data = carga_data()
    return list(data.LOCALIDAD.unique())


    