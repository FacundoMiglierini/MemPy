import PySimpleGUI as sg
from src.Controllers.Class import user
from src.GUI import settings
from src.Controllers import config_theme as theme

"""Configuraciones de la ventana de configuracion"""

def check_lvl(level, coincidences):
    if len(level) == 3:
        chars = list(level)
        if not(chars[0].isnumeric() and chars[2].isnumeric() and chars[1].lower() == 'x'):
            sg.popup_error('Error: formato de casillas no válido (Filas x Columnas). La longitud de las filas y columnas no puede exceder el valor de 9.',
            no_titlebar=True, font=[theme.FONT, 12])
            return False
        if str(coincidences).isdigit():
            if (int(coincidences) == 1):
                sg.popup_error('Error: la cantidad de coincidencias debe ser mayor a 1.', no_titlebar=True, font=[theme.FONT, 12])
                return False
            if not(int(coincidences) < (int(chars[0]) * int(chars[2]))):
                sg.popup_error('Error: la cantidad de coincidencias por elemento no puede ser igual a la cantidad de casillas del tablero.',
                no_titlebar=True, font=[theme.FONT, 12])
                return False
        else:
            sg.popup_error('Error: la cantidad de coincidencias debe ser un valor numérico.',  no_titlebar=True, font=[theme.FONT, 12])
            return False
    else:
        sg.popup_error('Error: formato de casillas no válido (Filas x Columnas). La longitud de las filas y columnas no puede exceder el valor de 9.',
        no_titlebar=True, font=[theme.FONT, 12])
        return False
    if int(chars[0]) * int(chars[2]) % int(coincidences) != 0:
        sg.popup_error(f'Error: la cantidad de casillas seleccionada no puede implementarse con {coincidences} coincidencias',
        no_titlebar=True, font=[theme.FONT, 12])
        return False
    
    return True

def check_time(hours, minutes, seconds):
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    if (hours.isdigit() and minutes.isdigit() and seconds.isdigit()):
        if not(len(hours) <= 2 and len(minutes) <= 2 and len (seconds) <= 2):
            sg.popup_error('Error: se excedió el tiempo máximo de partida, no se pueden superar los 2 dígitos.', no_titlebar=True, font=[theme.FONT, 12])
            return False
    else:
        sg.popup_error('Error: el tiempo de partida debe estar formado por dígitos.', no_titlebar=True, font=[theme.FONT, 12])
        return False
        
    return True

def start(users, logged_user):
    window = loop(users, logged_user)
    window.close()


def loop(users, logged_user):
    window = settings.build(logged_user.config)
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'EXIT', '-CANCEL_SETTINGS-'):
            break

        if event == '-APPLY_SETTINGS-':
            if (check_lvl(values['-LEVEL-'], values['-COINCIDENCES-']) and check_time(values['-HOURS-'], values['-MINUTES-'], values['-SECONDS-'])):
                window.hide()
                cfg = logged_user.config
                cfg["msg"] = {'win': '' if values['-WIN_MSG-'] == False else user.CFG_DEFAULT['msg']['win'],
                            'lose': '' if values['-LOSE_MSG-'] == False else user.CFG_DEFAULT['msg']['lose'],
                            'time': '' if values['-TIME_MSG-'] == False else user.CFG_DEFAULT['msg']['time']}
                cfg["level"] = values['-LEVEL-']
                cfg["coincidences"] = values['-COINCIDENCES-']
                cfg["help"] = 'yes' if values['-CLUES_YES-'] else 'no'
                cfg["elements"] = 'words' if values['-WORDS-'] else 'words and images'
                cfg["theme"] = 'MemPy ' + values['-THEME-']
                cfg["time"] = {'hours': values['-HOURS-'], 'minutes': values['-MINUTES-'], 'seconds': values['-SECONDS-']}
                logged_user.config = cfg
                users.update_users(logged_user)
                break

        if event == '-RESTORE_DEFAULT_CFG-':
            if (sg.popup_yes_no('¿Está seguro que desea volver a la configuración por defecto?',
                                background_color=theme.PRIMARY_COLOR_VARIANT, no_titlebar=True,
                                font=[theme.FONT, 12]).startswith('Y')):
                logged_user.restore_cfg_default()
                users.update_users(logged_user)
                break

    return window
