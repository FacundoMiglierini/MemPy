import PySimpleGUI as sg
from src.GUI import login
from src.Controllers.Class.users import Users
from src.Controllers.Ventanas import menu, registro
from src.Controllers import config_theme as theme

"""Toda la logica del login va aca"""


def start():
    window = loop()
    window.close()


def loop():
    users = Users()
    nicknames = users.get_usernames()
    window = login.build()
    while True:

        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
        if event == "-OK-":
            if values["-USERNAME-"].lower() in nicknames:
                window.hide()
                menu.start(users, users.get_user(values["-USERNAME-"].lower()))
                break
            else:
                sg.popup_auto_close("Nombre de usuario inexistente", auto_close_duration=2,
                                    background_color=theme.PRIMARY_COLOR_VARIANT, no_titlebar=True,
                                    font=[theme.FONT, 12])
        if event == '-REGISTER-':
            window.hide()
            registro.start(nicknames, users)
            break

    return window
