import datetime
from collections import Counter
from matplotlib import pyplot as plt

from src.Controllers.Estadisticas.piechart_helper import levantar_eventos

"""Este archivo se encarga de filtrar y crear el piechart de las partidas que se juega por dia"""

DIAS_SEMANA = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']


def filtrar():
    """Arma el dataframe, dropea las filas que no necesito y devuelve una lista de tiempos validos"""
    df = levantar_eventos()
    return df[(df['estado'] == 'ok') | (df['estado'] == 'error')]['tiempo'].tolist()


def lista_a_dias():
    """Con la lista de la funcion anterior transforma los timestamps en una lista de dias en
    formato escrito: Lunes, Martes, etc"""
    lista_dias = filtrar()
    for i in range(0, len(lista_dias)):
        lista_dias[i] = datetime.datetime.fromtimestamp(lista_dias[i])
        lista_dias[i] = lista_dias[i].weekday()
        lista_dias[i] = DIAS_SEMANA[lista_dias[i]]  # i.e: Lunes,Martes, etc...
        i += 1
    return lista_dias


def dias_de_partidas():
    """Con los datos ya filtrados y acomodados crea el piechart"""
    temp_var = Counter(lista_a_dias())

    plt.pie(temp_var.values(), labels=temp_var.keys(), autopct='%1.2f%%')
    plt.show()
