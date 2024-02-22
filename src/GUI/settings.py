import PySimpleGUI as sg

from src.Controllers import config_theme as theme

"""Construccion de la ventana de settings"""


def mensajes_a_mostrar(msg):
    """ Seccion Mensajes de victoria/derrota/y el tiempo a poner"""

    win = True if msg['win'] != '' else False
    lose = True if msg['lose'] != '' else False
    time = True if msg['time'] != '' else False

    layout = [
        sg.Text('Mensajes a mostrar:', font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Checkbox('Victoria', default=win, k='-WIN_MSG-', font=[theme.FONT, 12],
                    background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Checkbox('Derrota', default=lose, k='-LOSE_MSG-', font=[theme.FONT, 12],
                    background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Checkbox('Tiempo restante', default=time, k='-TIME_MSG-', font=[theme.FONT, 12],
                    background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6))
    ]
    return layout


def casillas_tablero(level):
    """ Seccion tamaño tablero"""
    values = ('3x6', '4x6', '5x6')

    layout = [
        sg.Text('Casillas del tablero: ', font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT,
                pad=(5, 6)),
        sg.Combo(values, default_value=level, font=[theme.FONT, 12], key='-LEVEL-', pad=(5, 6))
    ]

    return layout


def coincidencias_elemento(coincidences):
    """ Seccion con cuantas fichas jugar"""
    values = [x for x in range(2, 100)]

    layout = [
        sg.Text('Coincidencias por elemento: ', font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT,
                pad=(5, 6)),
        sg.Spin(values, initial_value=coincidences, key='-COINCIDENCES-', font=[theme.FONT, 12], pad=(5, 6))
    ]

    return layout


def tipo_elementos(type):
    """ Seccion jugar con imagenes y/o texto"""

    words = True if type == 'words' else False
    images = True if type == 'words and images' else False

    layout = [
        sg.Text('Tipos de elementos de las casillas: ', font=[theme.FONT, 12],
                background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Radio('Palabras', '-ELEMENTS-', words, key='-WORDS-', font=[theme.FONT, 12],
                 background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6)),
        sg.Radio('Imágenes y palabras', '-ELEMENTS-', images, key='-IMAGES-', font=[theme.FONT, 12],
                 background_color=theme.PRIMARY_COLOR_VARIANT, pad=(5, 6))
    ]

    return layout


def mostrar_pistas(help):
    """ Seccion mostrar pistas para jugar"""

    hints_yes = False
    hints_no = False

    if help.startswith('y'):
        hints_yes = True
    else:
        hints_no = True

    layout = [
        sg.Text('Pistas: ', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Radio('Sí', '-HELP-', default=hints_yes, key='-CLUES_YES-', background_color=theme.PRIMARY_COLOR_VARIANT,
                 font=[theme.FONT, 12], pad=(5, 6)),
        sg.Radio('No', '-HELP-', default=hints_no, key='-CLUES_NO-', background_color=theme.PRIMARY_COLOR_VARIANT,
                 font=[theme.FONT, 12],
                 pad=(5, 6))
    ]

    return layout


def tiempo_partida(time):
    """ Seccion tiempo de la partida"""
    horas = [x for x in range(0, 100)]
    min_seg = [x for x in range(0, 60)]

    layout = [
        sg.Text('Tiempo total de la partida:', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12],
                pad=(5, 6)),
        sg.Spin(horas, initial_value=time['hours'], key='-HOURS-', font=[theme.FONT, 12], pad=(5, 6)),
        sg.Text(':', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Spin(min_seg, initial_value=time['minutes'], key='-MINUTES-', font=[theme.FONT, 12], pad=(5, 6)),
        sg.Text(':', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Spin(min_seg, initial_value=time['seconds'], key='-SECONDS-', font=[theme.FONT, 12], pad=(5, 6))
    ]

    return layout


def seleccionar_tema(appearance):
    """ Theme a elegir para el programa"""
    values = ('Light Green', 'Light Red', 'Light Blue', 'Dark Green', 'Dark Red', 'Dark Blue')

    layout = [
        sg.Text('Tema: ', background_color=theme.PRIMARY_COLOR_VARIANT, font=[theme.FONT, 12], pad=(5, 6)),
        sg.Combo(values, default_value=appearance, key='-THEME-', font=[theme.FONT, 12], pad=(5, 6))
    ]

    return layout


def build(data):
    """Construccion final de la ventana"""
    settings_dificultad = [
        casillas_tablero(data['level']),
        coincidencias_elemento(data['coincidences']),
        mostrar_pistas(data['help']),
        tiempo_partida(data['time']),
    ]

    settings_otros = [
        mensajes_a_mostrar(data['msg']),
        tipo_elementos(data['elements']),
        seleccionar_tema(data['theme'].replace('MemPy ', ''))
    ]

    tab_dificultad = sg.Tab('Dificultad', settings_dificultad, font=[theme.FONT, 12],
                            background_color=theme.PRIMARY_COLOR_VARIANT, title_color='Black',
                            element_justification='c')
    tab_otros = sg.Tab('Otros', settings_otros, font=[theme.FONT, 12], background_color=theme.PRIMARY_COLOR_VARIANT,
                       title_color='White', element_justification='c')
    layout_tabs = [[tab_dificultad, tab_otros]]

    layout = [
        [sg.Text('Configuración', background_color=theme.PRIMARY_COLOR, font=['Roboto Thin', 30], pad=(90, 5))],
        [sg.TabGroup(layout_tabs, 'top', background_color=theme.PRIMARY_COLOR, font=[theme.FONT, 15],
                     title_color='Black', tab_background_color=theme.PRIMARY_COLOR_VARIANT,
                     selected_background_color=theme.PRIMARY_COLOR, pad=((100, 50), 0))],
        [sg.Button('Restaurar a valores por defecto', key="-RESTORE_DEFAULT_CFG-", font=[theme.FONT, 12], pad=(0, 10))],
        [sg.Button('Cancelar', key='-CANCEL_SETTINGS-', font=[theme.FONT, 15], pad=((0, 5), 10)),
         sg.Button('Aplicar cambios', key='-APPLY_SETTINGS-', font=[theme.FONT, 15], pad=((5, 0), 10)), ]

    ]

    return sg.Window('Configuración', margins=(0, 0), no_titlebar=True, background_color=theme.PRIMARY_COLOR,
                     element_justification='c', finalize=True, grab_anywhere=True).Layout(layout)
