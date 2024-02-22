import PySimpleGUI as sg
from src.Controllers import config_theme as theme

"""
Muestra de los HIGHSCORES
"""


def generar_layout_scores(data):
    headings = ['Nick del jugador', 'Puntaje']
    col_widths = [25, 20]

    layout = [[sg.Table(values=data, headings=headings, col_widths=col_widths, num_rows=10, font=[theme.FONT, 15],
                        justification='c', hide_vertical_scroll=True,
                        header_font=[theme.FONT, 18], selected_row_colors=('White', theme.PRIMARY_COLOR_VARIANT))]]

    return layout


def build(data):
    tab_hard = sg.Tab('Difícil', generar_layout_scores(data[2]), font=[theme.FONT, 15], background_color=theme.PRIMARY_COLOR_VARIANT, element_justification='c')
    tab_medium = sg.Tab('Medio', generar_layout_scores(data[1]), font=[theme.FONT, 15], background_color=theme.PRIMARY_COLOR_VARIANT, element_justification='c')
    tab_easy = sg.Tab('Fácil', generar_layout_scores(data[0]), font=[theme.FONT, 15], background_color=theme.PRIMARY_COLOR_VARIANT, element_justification='c')

    layout_tabs = [[tab_easy, tab_medium, tab_hard]]

    layout = [
        [sg.Text('Puntajes', font=['Roboto Thin', 50], pad=(90, 20))],
        [sg.TabGroup(layout_tabs, 'top', background_color=theme.PRIMARY_COLOR, font=[theme.FONT, 15],
                     title_color='Black', tab_background_color=theme.PRIMARY_COLOR_VARIANT,
                     selected_background_color=theme.PRIMARY_COLOR, pad=((100, 50), 0))],
        [sg.Button('Volver al menú principal', key='-RETURN-', font=[theme.FONT, 12], pad=(0, (30, 10)))]
    ]

    return sg.Window('Highscores', layout, no_titlebar=True, grab_anywhere=True, element_justification='center')
