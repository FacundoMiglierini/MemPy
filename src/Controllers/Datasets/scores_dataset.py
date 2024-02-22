import pandas as pd
import time
from src.Controllers.Datasets.Datasets import datos_path

PATH_CSV = datos_path()


def users_in_csv():
    """Trae los eventos del juego  y los devuelve en un dataframe"""
    data = pd.read_csv(PATH_CSV, index_col=False)
    return data

def level (user):
    if user.config['level'] == '3x6':
        nivel = 'facil'
    elif user.config['level'] == '4x6':
        nivel = 'intermedio'
    elif user.config['level'] == '5x6':
        nivel = 'dificil'
    else:
        nivel = 'personalizado'
    return nivel    
    
def guardar(inicio,datos):
    fila = pd.Series(inicio)
    datos = datos.append(fila, ignore_index=True)
    datos.to_csv(PATH_CSV, index=False)

def inicio_juego(user):
    datos = users_in_csv()
    nivel=level(user)
    inicio = {
        'tiempo': round(time.time()),
        'partida': int(datos['partida'].tail(1) + 1),
        'coincidencias': user.config['coincidences'],
        'nombre_evento': "inicio_partida",
        'usuario_nick': user.username,
        'usuario_genero': user.genero,
        'usuario_edad': round(user.edad),
        'estado': '',
        'palabra': '',
        'nivel': nivel
    }
    guardar(inicio,datos)


def un_fallo(user, palabra):
    datos = users_in_csv()
    nivel=level(user)
    inicio = {
        'tiempo': round(time.time()),
        'partida': int(datos['partida'].tail(1)),
        'coincidencias': user.config['coincidences'],
        'nombre_evento': 'Intento',
        'usuario_nick': user.username,
        'usuario_genero': user.genero,
        'usuario_edad': round(user.edad),
        'estado': 'error',
        'palabra': palabra,
        'nivel': nivel
    }
    fila = pd.Series(inicio)
    datos = datos.append(fila, ignore_index=True)
    datos.to_csv(PATH_CSV, index=False)


def un_acierto(user, palabra):
    datos = users_in_csv()
    nivel=level(user)
    inicio = {
        'tiempo': round(time.time()),
        'partida': int(datos['partida'].tail(1)),
        'coincidencias': user.config['coincidences'],
        'nombre_evento': 'intento',
        'usuario_nick': user.username,
        'usuario_genero': user.genero,
        'usuario_edad': round(user.edad),
        'estado': 'ok',
        'palabra': palabra,
        'nivel': nivel}
    guardar(inicio,datos)


def fin_partida_timeout(user, palabra):
    datos = users_in_csv()
    nivel=level(user)
    inicio = {
        'tiempo': round(time.time()),
        'partida': '',
        'coincidencias': user.config['coincidences'],
        'nombre_evento': 'fin',
        'usuario_nick': user.username,
        'usuario_genero': user.genero,
        'usuario_edad': round(user.edad),
        'estado': 'timeout',
        'palabra': palabra,
        'nivel': nivel}
    guardar(inicio,datos)


def fin_partida_win(user, palabra):
    datos = users_in_csv()
    nivel=level(user)
    inicio = {
        'tiempo': round(time.time()),
        'partida': int(datos['partida'].tail(1)),
        'coincidencias': user.config['coincidences'],
        'nombre_evento': 'fin',
        'usuario_nick': user.username,
        'usuario_genero': user.genero,
        'usuario_edad': round(user.edad),
        'estado': 'finalizada',
        'palabra': palabra,
        'nivel': nivel}
    guardar(inicio,datos)


def fin_partida_abandono(user):
    datos = users_in_csv()
    nivel=level(user)
    inicio = {
        'tiempo': round(time.time()),
        'partida': int(datos['partida'].tail(1)),
        'coincidencias': user.config['coincidences'],
        'nombre_evento': 'fin',
        'usuario_nick': user.username,
        'usuario_genero': user.genero,
        'usuario_edad': round(user.edad),
        'estado': 'cancelada',
        'palabra': ' ',
        'nivel': nivel}
    guardar(inicio,datos)