import PySimpleGUI as sg
import os

from VariablesEntorno import GRAPHICS_PATH

"""
Todo lo dedicado al apartado grafico del menu principal va aca
"""


def build():
    """
    Construye la ventana del menú del juego
    """

    path_buttons = os.path.join(os.getcwd(), GRAPHICS_PATH, 'Menu', 'Buttons', sg.theme())
    title_file = sg.theme().split()[1].lower() + '_title.png'
    pad_buttons = (116, 116)

    layout = [
        [sg.Image(filename=os.path.join(os.getcwd(), GRAPHICS_PATH, 'Menu', 'Background', title_file),
                  background_color=sg.theme_background_color(),
                  pad=((90, 90), 53))],
        [sg.Button(image_filename=os.path.join(path_buttons, 'play.png'),
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                   pad=(pad_buttons, 7), key="-play-", image_size=(300, 54))],
        [sg.Button(image_filename=os.path.join(path_buttons, 'settings.png'),
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                   pad=(pad_buttons, 7), key="-settings-", image_size=(300, 54))],
        [sg.Button(image_filename=os.path.join(path_buttons, 'scores.png'),
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                   pad=(pad_buttons, 7), key="-score-", image_size=(300, 54))],
        [sg.Button(image_filename=os.path.join(path_buttons, 'stats.png'),
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                   pad=(pad_buttons, 7), key='-stats-', image_size=(300, 54))],
        [sg.Button(image_filename=os.path.join(path_buttons, 'exit.png'),
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                   pad=((473, 0), (77, 6)), key='-exit-', image_size=(54, 54))]
    ]

    menu = sg.Window('Juego Memoria', size=(533, 600), margins=(0, 0), grab_anywhere=True, no_titlebar=True).Layout(
        layout)

    return menu
