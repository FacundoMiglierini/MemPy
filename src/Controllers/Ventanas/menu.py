import PySimpleGUI as sg
from src.GUI import menu
from src.Controllers import config_theme as theme
from src.Controllers.Ventanas import settings, estadisticas, highscores
from src.Controllers.Ventanas.Board import board

"""Archivo con la logica del menu"""


def start(users, logged_user):
    window = loop(users, logged_user)
    window.close()


def loop(users, logged_user):
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """

    theme.cargar_tema(logged_user.config['theme'])
    window = menu.build()
    while True:
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
        if event == "-play-":
            window.hide()
            board.start(users, logged_user)
            window.un_hide()
        if event == "-settings-":
            window.hide()
            settings.start(users, logged_user)
            window.close()
            theme.cargar_tema(logged_user.config['theme'])
            window = menu.build()
        if event == "-score-":
            window.hide()
            highscores.start(users)
            window.un_hide()
        if event == '-stats-':
            window.hide()
            estadisticas.start()
            window.un_hide()

    return window
