import PySimpleGUI as sg
from src.GUI import highscores


def start(users):
    window = loop(users)
    window.close()


def loop(users):
    window = highscores.build(users.top_ten_scores())
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-RETURN-'):
            break
    return window
