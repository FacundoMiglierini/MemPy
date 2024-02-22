import PySimpleGUI as sg
from src.Controllers.Estadisticas import piechart_por_dia, piechart_por_estado_finalizacion, piechart_por_genero, \
    piechart_tiempo_por_nivel, piechart_top_ten_primeras_palabras
from src.GUI import estadisticas


def start():
    window = loop()
    window.close()


def loop():
    window = estadisticas.build()
    while True:

        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-', '-EXIT-'):
            break
        if event == "-TOP_TEN-":
            window.hide()
            piechart_top_ten_primeras_palabras.top_ten()
            window.un_hide()
        if event == '-STATE-':
            window.hide()
            piechart_por_estado_finalizacion.partidas_por_estado()
            window.un_hide()
        if event == '-GENDER-':
            window.hide()
            piechart_por_genero.partidas_por_genero()
            window.un_hide()
        if event == '-WEEK_DAY-':
            window.hide()
            piechart_por_dia.dias_de_partidas()
            window.un_hide()
        if event == '-TIME_LVL-':
            window.hide()
            piechart_tiempo_por_nivel.mostrar_chart()
            window.un_hide()

    return window
