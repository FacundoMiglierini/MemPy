from collections import Counter
from matplotlib import pyplot as plt

from src.Controllers.Estadisticas.piechart_helper import levantar_eventos

"""Este Archivo se encarga del top 10 de primeras palabras encontradas"""


def top_ten():
    df = levantar_eventos()
    condicion = df[(df['estado'] != 'ok')].index
    df = df.drop(condicion)
    df = df.groupby('partida').first()
    x = df['palabra'].tolist()
    temp_var = Counter(x)
    plt.bar(temp_var.keys(), temp_var.values())
    plt.xlabel('Palabras')
    plt.ylabel('Veces Encontradas')
    plt.title("Top 10 palabras mas encontradas")
    plt.show()
