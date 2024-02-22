import os
import pandas as pd
from VariablesEntorno import DATASETS_PATH

"""Archivo helper (todo lo comun a los piechart va aca)"""


def levantar_eventos():
    return pd.read_csv(os.path.join(DATASETS_PATH, 'datos_de_prueba.csv'), encoding='utf-8')
