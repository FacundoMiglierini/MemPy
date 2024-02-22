import PySimpleGUI as sg
from src.Controllers import config_theme as theme

"""
Todo lo dedicado al apartado grafico del registro va aca
"""


def build():
    """Construccion de la ventana del registro"""
    user_field = [[sg.Text("Ingrese Nombre", pad=(0, (20, 10)), font=[theme.FONT, 10])],
                  [sg.Input(k="-USERNAME-", enable_events=True, pad=(0, (0, 10)), font=[theme.FONT, 10])],
                  [sg.Text("Ingrese Edad", pad=(0, (0, 0)), font=[theme.FONT, 10])],
                  [sg.Slider(key="-AGE-", range=(1, 100), default_value=18, size=(35, 15), orientation='horizontal',
                             pad=(0, (0, 10)), font=[theme.FONT, 10])],
                  [sg.Text("Ingrese su genero", pad=(0, (0, 10)), font=[theme.FONT, 10])],
                  [sg.Input(k="-GENDER-", pad=(0, (0, 10)), font=[theme.FONT, 10])],
                  [sg.Button('Registrarse', k="-OK-", visible=False, font=[theme.FONT, 10])],
                  [sg.Text(
                      "Usuario ocupado, ingrese otro por favor . En caso de ya tener un usuario creado, presione Iniciar Sesión ",
                      k="-ERROR-", visible=False, font=[theme.FONT, 10])],
                  [[sg.Button('Salir', k='-CANCEL-'),
                    sg.Button('Iniciar Sesión', k="-LOGIN-", visible=False, font=[theme.FONT, 10])]]
                  ]

    window = sg.Window("Registro", user_field, size=(700, 340), element_justification='c', no_titlebar=True)
    return window
