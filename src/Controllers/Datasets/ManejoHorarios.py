import datetime

from src.Controllers.Datasets.CarsDataset import sort_cars_by_rating
from src.Controllers.Datasets.CountriesDataset import countries_dataset
from src.Controllers.Datasets.LolDataset import lol_dataset

"""
Modulo que se encarga de obtener las fichas para el tablero dividido en 3 rangos horarios:
En las madrugadas (00:00 AM - 07:59 AM) se juega con autos
En las mañanas-despues de almorzar (08:00 AM - 15:59 PM) se juega con los paises
En la tarde-noche (16:00 PM - 23:59 PM) se juega con los campeones del lol
"""

HORA_MADRUGADA = [0, 9]
HORA_MANANA = [8, 17]
HORA_NOCHE = [17, 24]

momento_de_juego = datetime.datetime.now()

dia_de_juego = int(momento_de_juego.strftime("%w"))
hora_de_juego = int(momento_de_juego.strftime("%H"))


def con_que_se_juega(elements):
    """Selector de horarios, se llama a los modulos respectivos de cada dataset"""
    if es_madrugada():
        return [sort_cars_by_rating(elements), elements]
    elif es_manana():
        return [countries_dataset(dia_de_juego, elements), elements]
    elif es_noche():
        return [lol_dataset(dia_de_juego), 'words']


def es_madrugada():
    return hora_de_juego in range(HORA_MADRUGADA[0], HORA_MADRUGADA[1])


def es_manana():
    return hora_de_juego in range(HORA_MANANA[0], HORA_MANANA[1])


def es_noche():
    return hora_de_juego in range(HORA_NOCHE[0], HORA_NOCHE[1])
