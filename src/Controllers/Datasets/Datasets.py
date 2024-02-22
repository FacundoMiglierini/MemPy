import os
from VariablesEntorno import DATASETS_PATH

"""Este archivo se ocupa de que las rutas de los datasets queden bien definidas y listas para trabajar,
no importa el sistema operativo"""


def countries_path():
    """path de los paises"""
    return [os.path.join(DATASETS_PATH, 'countries_of_the_world.csv'), os.path.join(DATASETS_PATH, 'CountryFlags')]


def cars_path():
    """path de los autos"""
    return [os.path.join(DATASETS_PATH, 'cars.csv'), os.path.join(DATASETS_PATH, 'CarLogos')]


def lol_path():
    """path de los campeones del lol"""
    return os.path.join(DATASETS_PATH, 'LOL_champions_stats.csv')


def datos_path():
    """path de los datos de prueba"""
    return os.path.join(DATASETS_PATH, 'datos_de_prueba.csv')
