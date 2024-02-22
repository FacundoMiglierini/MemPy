CFG_DEFAULT = {
    "level": "3x6",
    "coincidences": 2,
    "help": "no",
    "elements": "words",
    "msg": {
        "win": "Ganaste!!",
        "lose": "Perdiste!!",
        "time": "Quedan 30 segundos para que finalice la partida"
    },
    "time": {
        "hours": 0,
        "minutes": 10,
        "seconds": 0
    },
    "theme": "MemPy Light Green"
}

PTS_DEFAULT = {
    "3x6": 0,
    "4x6": 0,
    "5x6": 0
}


class User():

    def __init__(self, username, config=CFG_DEFAULT, age=0, gender=0, puntaje=PTS_DEFAULT) -> None:
        self._username = ''
        self._data = {}
        self._data['age'] = age
        self._data['gender'] = gender
        self._data['config'] = config
        self._data['puntaje'] = puntaje
        self._username = username

    @property
    def edad(self):
        return self._data['age']

    @edad.setter
    def edad(self, age) -> None:
        self._data['age'] = age

    @property
    def genero(self):
        return self._data['gender']

    @genero.setter
    def genero(self, gender) -> None:
        self._data['gender'] = gender

    @property
    def data(self) -> dict:
        return self._data

    @property
    def username(self) -> str:
        return self._username

    @property
    def config(self) -> dict:
        return self._data['config']

    @config.setter
    def config(self, cfg) -> None:
        self._data['config'] = cfg

    def update_score(self, puntaje, lvl) -> None:
        lvl = list(lvl)
        boxes = int(lvl[0]) * int(lvl[2])
        defaults = PTS_DEFAULT.keys()
        for elem in defaults:
            total = list(elem)
            if (int(total[0]) * int(total[2]) > boxes):
                self._data['puntaje'][elem] += puntaje
                break

    def restore_cfg_default(self) -> None:
        self.config = CFG_DEFAULT
