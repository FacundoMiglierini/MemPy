import PySimpleGUI as sg 
from src.Controllers import config_theme as theme


def build():

    layout=[
        [sg.Text('Estadísticas', font= ['Roboto Thin', 60], background_color=theme.PRIMARY_COLOR, pad= (0, 53))],
        [sg.Button('Top 10 primeras palabras encontradas', key= '-TOP_TEN-', size= (55, 1), font= [theme.FONT, 15], pad= (55, 10))],
        [sg.Button('Porcentaje de partidas por estado', key= '-STATE-', size= (55, 1), font= [theme.FONT, 15], pad= (55, 10))],
        [sg.Button('Porcentaje de partidas finalizadas según género', key= '-GENDER-', size= (55, 1), font= [theme.FONT, 15], pad= (55, 10))],
        [sg.Button('Porcentaje de partidas que se juegan para cada día de la semana', key= '-WEEK_DAY-', size= (55, 1), font= [theme.FONT, 15], pad= (55, 10))],
        [sg.Button('Promedio de tiempo de partidas finalizadas por nivel', key= '-TIME_LVL-', size= (55, 1), font= [theme.FONT, 15], pad= (55, 10))],
        [sg.Button('Volver al menú principal', k= '-EXIT-', font= [theme.FONT, 12], pad= (55,(55, 20))) ] 
        ]

    return sg.Window('Stats', layout, no_titlebar= True, grab_anywhere= True, element_justification= 'center')