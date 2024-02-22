from matplotlib import pyplot as plt
from src.Controllers.Estadisticas.piechart_helper import levantar_eventos

"""Este archivo se encarga de filtrar y crear el piechart de las partidas por sus 3 estados de finalizacion"""


def partidas_por_estado():
    """Carga el csv, cuenta los 3 estados de finalizacion de una partida (timeout,finalizada,cancelada)
    y con eso arma el piechart"""
    df = levantar_eventos()

    y = df['estado'].tolist()
    temp_1 = y.count('cancelada')
    temp_2 = y.count('finalizada')
    temp_3 = y.count('timeout')

    y = ['Cancelada', 'Finalizado', 'Timeout']

    vals = [temp_1, temp_2, temp_3]

    plt.pie(vals, labels=y, autopct='%1.2f%%')
    plt.show()
