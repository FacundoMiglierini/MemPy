import json
import os

from VariablesEntorno import ENTITIES_PATH
from src.Controllers.Class.user import User

FILE_NAME = 'users.json'
PATH_FILE = os.path.join(os.getcwd(), ENTITIES_PATH, FILE_NAME)


class Users():
    data = {}

    def __init__(self) -> None:
        with open(PATH_FILE, 'r') as file:
            self.data = json.load(file)

    def get_usernames(self) -> list:
        return self.data.keys()

    def save_users(self) -> None:
        with open(PATH_FILE, 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_users(self, user) -> None:
        self.data[user.username] = user.data
        self.save_users()

    def get_user(self, username) -> User:
        try:
            data_user = self.data[username]
            return User(username, data_user['config'], data_user['age'], data_user['gender'], data_user['puntaje'])
        except KeyError:
            print('Error: usuario no encontrado en el archivo.')

    def top_ten_scores(self) -> list:
        easy = []
        medium = []
        hard = []

        for elem in self.get_usernames():
            easy.append([elem, self.get_user(elem).data['puntaje']['3x6']])
            medium.append([elem, self.get_user(elem).data['puntaje']['4x6']])
            hard.append([elem, self.get_user(elem).data['puntaje']['5x6']])

        easy.sort(reverse=True, key=lambda x: x[1])
        medium.sort(reverse=True, key=lambda x: x[1])
        hard.sort(reverse=True, key=lambda x: x[1])

        return [easy, medium, hard]
