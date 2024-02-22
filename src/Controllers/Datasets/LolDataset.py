import csv

from src.Controllers.Datasets.Datasets import lol_path

"""
Todo lo relacionado al control del dataset del lol va aca
"""


def champions_in_csv():
    """Trae los campeones del archivo y los devuelve en formato de lista"""
    datos = []
    with open(lol_path(), encoding='utf-8') as file_lol:
        champions = csv.reader(file_lol, delimiter=';')
        next(champions)
        for elem in champions:
            datos.append(elem)
    return datos


def sort_campeones_por_nombre():
    """Campeones por alfabeto"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=False, key=lambda x: x[0])))


def sort_por_rango():
    """Campeones con mas rango"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=True, key=lambda x: int(x[35]))))


def sort_por_precio_rp():
    """Campeones mas baratos"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=False, key=lambda x: int(x[7]))))


def sort_por_clase():
    """Campeones por clase"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=False, key=lambda x: x[2])))


def sort_por_gamestyle():
    """Sorteados alfabeticamente por estilo de juego"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=False, key=lambda x: x[3])))


def sort_por_dano():
    """Champions que mas daño hacen en lvl 18"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=True, key=lambda x: x[23])))


def sort_por_mana():
    """Champions que mas mana tienen en lvl 18"""
    return list(map(lambda x: x[0], sorted(champions_in_csv(), reverse=True, key=lambda x: x[17])))


def lol_dataset(dia_de_juego):
    """Viene un dia para jugar por parametro y segun lo que surja se devuelve los datos sorteados de X forma"""
    if dia_de_juego == 0:
        return sort_campeones_por_nombre()
    if dia_de_juego == 1:
        return sort_por_rango()
    if dia_de_juego == 2:
        return sort_por_precio_rp()
    if dia_de_juego == 3:
        return sort_por_clase()
    if dia_de_juego == 4:
        return sort_por_gamestyle()
    if dia_de_juego == 5:
        return sort_por_dano()
    if dia_de_juego == 6:
        return sort_por_mana()
