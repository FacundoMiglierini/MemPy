import csv

from src.Controllers.Datasets.Datasets import cars_path
import os

"""
Todo lo relacionado al control del dataset de los autos va aca
"""

PATH_CSV = cars_path()[0]
PATH_IMAGES = cars_path()[1]


def cars_in_csv():
    """Trae los autos del archivo y los devuelve en formato de lista"""
    datos = []
    with open(PATH_CSV) as file_cars:
        cars = csv.reader(file_cars, delimiter=',')
        next(cars)
        for elem in cars:
            datos.append(elem)
    return datos


def sort_cars_by_rating(elements):
    """hace un sort de la lista por ranking de autos"""

    if elements == 'words':
        return list(map(lambda x: x[3].lstrip(), sorted(cars_in_csv(), key=lambda x: int(x[0]))))
    else:
        return list(map(lambda x: {
            f'{x[3].lstrip()}': os.path.join(PATH_IMAGES, x[3].lstrip().lower().replace(' ', '-') + '.png')},
                        sorted(cars_in_csv(), key=lambda x: int(x[0]))))
