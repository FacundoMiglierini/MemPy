import PySimpleGUI as sg
from src.Controllers.Class import matriz
from src.Controllers.Ventanas.Board import board_words, board_images
from src.Controllers.Datasets import scores_dataset
import os

def start(users, user):
    array = matriz.Matriz(*user.config['level'].split('x'), user.config['coincidences'], user.config['elements'])
    elements = array.cargar_matriz()
    scores_dataset.inicio_juego(user)
    index_matriz = [(i, j) for j in range(0, array.cols) for i in range(0, array.rows)]
    button_path = os.path.join(os.getcwd(), 'src', 'Entities', 'Graphics', 'Board', sg.theme() + '_question_mark.png')
    if elements == 'words':
        board_words.start(array, index_matriz, button_path, user, users)
    else:
        board_images.start(array, index_matriz, button_path, user, users)
    users.update_users(user)