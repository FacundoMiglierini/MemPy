import PySimpleGUI as sg

from VariablesEntorno import GRAPHICS_PATH
from src.Controllers import config_theme as theme
import os


def frame_info(level, username, time, help, score):
    if level == '3x6':
        dif = 'Fácil'
    elif level == '4x6':
        dif = 'Media'
    else:
        dif = 'Difícil'

    clues = [sg.Button('Obtener pista', key='-CLUE-', font=[theme.FONT, 15], pad=(0, 30))] if help.startswith(
        'y') else []
    layout = [
        clues,
        [sg.Text(f'Puntaje: {score}', key= '-SCORE-', font=[theme.FONT, 12])],
        [sg.Text('Nombre de usuario: ' + username, font=[theme.FONT, 12])],
        [sg.Text(f'Dificultad: {dif} ({level} casillas)', font=[theme.FONT, 12])],
        [sg.Text(f'Tiempo restante: {time["hours"]:02d}:{time["minutes"]:02d}:{time["seconds"]:02d}', key="-TIMER-",
                 size=(26, 1), justification='right', font=[theme.FONT, 12])],
        [sg.Button('Salir del juego', key='-EXIT-', font=[theme.FONT, 12])]
    ]

    return sg.Column(layout, element_justification='Right', vertical_alignment='b', pad=((30, 10), 10))


def frame_tablero(matriz):
    button_path = os.path.join(os.getcwd(), GRAPHICS_PATH, 'Board', sg.theme() + '_question_mark.png')

    layout = [
        [sg.Button(image_filename=button_path, button_color=('white', theme.PRIMARY_COLOR_VARIANT), key=(row, col),
                   pad=(5, 5), border_width=0,
                   size=(9, 2), auto_size_button= True, font=[theme.FONT, 10]) for col in range(len(matriz[0]))] for row
        in range(len(matriz))
    ]
    return sg.Frame('', layout, pad=(5, 5), border_width=3, background_color=theme.PRIMARY_COLOR_VARIANT)


def build(matriz, user, score):
    layout = [
        [frame_tablero(matriz),
         frame_info(user.config['level'], user.username, user.config['time'], user.config['help'], score)]
    ]

    Window = sg.Window('', layout, no_titlebar=True, grab_anywhere=True)
    return Window
