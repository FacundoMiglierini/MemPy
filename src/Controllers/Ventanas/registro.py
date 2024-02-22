import PySimpleGUI as sg
from src.GUI import registro
from src.Controllers.Class.user import User
from src.Controllers.Ventanas import login, menu

"""La logica del registro va aca"""


def start(nicknames, users):
    window = loop(nicknames, users)
    window.close()


def loop(nicknames, users):
    window = registro.build()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
        if event == "-USERNAME-":
            username = values.get('-USERNAME-')
            if username.lower() in nicknames or len(username) == 0:
                window["-OK-"].update(visible=False)
                window["-LOGIN-"].update(visible=True)
                window["-ERROR-"].update(visible=True)
            else:
                window["-OK-"].update(visible=True)
                window["-LOGIN-"].update(visible=False)
                window["-ERROR-"].update(visible=False)
        if event == '-OK-':
            new_user = User(username, age=values['-AGE-'], gender=values['-GENDER-'].lower())
            users.update_users(new_user)
            window.hide()
            menu.start(users, new_user)
            break
        if event == '-LOGIN-':
            window.hide()
            login.start()
            break

    return window
