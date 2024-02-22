import random
from src.Controllers.Datasets.ManejoHorarios import con_que_se_juega


class Matriz():

    def __init__(self, i, j, coincidences, elements):
        self.rows = int(i)
        self.cols = int(j)
        self.coincidences = coincidences
        self.elements = elements

    def cargar_matriz(self):
        datos, self.current_elements = con_que_se_juega(self.elements)
        random.shuffle(datos)
        if self.current_elements != 'words':
            self.counter_ocurrencias = dict.fromkeys(
                set().union(*(elem.keys() for elem in datos[:(self.rows * self.cols) // self.coincidences])), False)
        else:
            self.counter_ocurrencias = dict.fromkeys(datos[:(self.rows * self.cols) // self.coincidences], False)
        datos = datos[:(self.rows * self.cols) // self.coincidences] * self.coincidences
        random.shuffle(datos)
        self.matriz = [datos[i:i + self.cols] for i in range(0, len(datos), self.cols)]
        return self.current_elements

    def set_correcta(self, word):
        self.counter_ocurrencias[word] = True

    def get_clue(self):
        array = []
        array_disp = []
        if self.current_elements == 'words':
            array = [self.matriz[i][j] for i in range(0, self.rows) for j in range(0, self.cols)]
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    if not self.counter_ocurrencias[self.matriz[i][j]]:
                        array_disp.append(self.matriz[i][j])
        else:
            array = [list(self.matriz[i][j].keys())[0] for i in range(0, self.rows) for j in range(0, self.cols)]
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    word = list(self.matriz[i][j].keys())[0]
                    if not self.counter_ocurrencias[word]:
                        array_disp.append(word)
        elem = random.choice(tuple(set(array_disp)))
        pos = []
        start_at = -1
        for i in range(0, self.coincidences):
            index = array.index(elem, start_at + 1)
            pos.append((index // self.cols, index % self.cols))
            start_at = index
        return pos

    def fin_partida(self):
        return all(elem for elem in self.counter_ocurrencias.values())
