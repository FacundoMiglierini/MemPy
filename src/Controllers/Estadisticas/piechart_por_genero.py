from collections import Counter
from matplotlib import pyplot as plt

from src.Controllers.Estadisticas.piechart_helper import levantar_eventos

"""Este archivo se ocupa del piechart de las partidas finalizadas correctamente segun el genero"""


def partidas_por_genero():
    """Crea el dataframe, filtra por partidas finalizadas y despues se guarda los generos en una lista
    con eso arma el piechart"""
    df = levantar_eventos()

    y = df.loc[df['estado'] == 'finalizada']

    y = y.usuario_genero.tolist()

    y = Counter(y)

    plt.pie(y.values(), labels=y.keys(), autopct='%1.2f%%')
    plt.show()
