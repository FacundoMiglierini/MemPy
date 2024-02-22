from matplotlib import pyplot as plt
from src.Controllers.Estadisticas.piechart_helper import levantar_eventos

df = levantar_eventos()
condicion = df[(df['nombre_evento'] != 'inicio_partida') & (df['nombre_evento'] != 'fin')].index
df = df.drop(condicion)

df['estado'].fillna('', inplace=True)
df = df.drop(df[(df['estado'] != 'finalizada') & (df['estado'] != '')].index)
df = df[df.duplicated(subset='partida', keep=False)]

facil = df[df['nivel'] == 'facil']['tiempo'].tolist()
medio = df[df['nivel'] == 'medio']['tiempo'].tolist()
dificil = df[df['nivel'] == 'dificil']['tiempo'].tolist()


def calculo_promedios(lista_tiempos):
    if len(lista_tiempos) == 0:
        return 0.0
    cont = 0
    for i in range(0, len(lista_tiempos) - 1):
        cont = cont + lista_tiempos[i + 1] - lista_tiempos[i]
        i += 2
    return float(cont / (len(lista_tiempos) / 2))


def mostrar_chart():
    promedios = [calculo_promedios(facil), calculo_promedios(medio), calculo_promedios(dificil)]
    dificultades = ['facil', 'medio', 'dificil']
    plt.pie(promedios, labels=dificultades, autopct='%1.2f%%')
    plt.show()
