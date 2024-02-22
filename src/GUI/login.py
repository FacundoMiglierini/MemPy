import PySimpleGUI as sg
from src.Controllers import config_theme as theme

"""
Todo lo dedicado al apartado grafico del Login va aca
"""


def build():
    """
    Ventana del login
    """

    theme.cargar_tema()

    layout = [[sg.Text("Ingrese nombre", font=[theme.FONT, 10])],
              [sg.Input(key="-USERNAME-", font=[theme.FONT, 10])],
              [sg.Button("Ingresar", k='-OK-', font=[theme.FONT, 10]),
               sg.Button("Salir", k='-CANCEL-', font=[theme.FONT, 10])],
              [sg.Button("Crear cuenta nueva", k='-REGISTER-', font=[theme.FONT, 10],
                         button_color=('White', theme.SECONDARY_COLOR_VARIANT))]]

    window = sg.Window('Login', layout, margins=(50, 30), no_titlebar=True)

    return window
