from src.Controllers.Datasets import scores_dataset
import PySimpleGUI as sg
from src.GUI import board
from src.Controllers.Ventanas import highscores
from src.Controllers.Class.score import Score
from src.Controllers import config_theme as theme
import time

def start(array, index_matriz, button_path,user, users):
    window = loop(array, index_matriz, button_path,user, users)
    window.close()


def loop(array, index_matriz, button_path,user, users):
    ocurrencias_jugada = {}
    puntaje = Score()
    window = board.build(array.matriz, user, puntaje.score)
    start=time.time()
    tiempo=user.config['time']['hours'] *3600 + user.config['time']['minutes'] *60 + user.config['time']['seconds']
    delay = 0
    while True:
        
        event, _values = window.read(timeout= 0)
        if event in (sg.WIN_CLOSED,'-CANCEL-', '-EXIT-'):
            answer = sg.popup_yes_no('¿Está seguro de que desea abandonar la partida? El puntaje adquirido no se guardará', no_titlebar= True)
            if answer != 'No':
                scores_dataset.fin_partida_abandono(user)
                break           
        if event in index_matriz:
            row, col = event
            elem = array.matriz[row][col]
            window[event].update(image_filename= list(elem.items())[0][1], image_size= (110, 110))
            if not list(elem.items())[0][0] in ocurrencias_jugada.keys():
                ocurrencias_jugada[list(elem.items())[0][0]] = [1, [(row, col)]]
            elif not event in ocurrencias_jugada[list(elem.items())[0][0]][1]:
                new_pos = ocurrencias_jugada[list(elem.items())[0][0]][1]
                new_pos.append((row, col))
                ocurrencias_jugada[list(elem.items())[0][0]] = [ocurrencias_jugada[list(elem.items())[0][0]][0] + 1, new_pos]
            if sum(map(lambda x : x[0], ocurrencias_jugada.values())) == array.coincidences:
                if len(ocurrencias_jugada.keys()) == 1:
                    scores_dataset.un_acierto(user,list(elem.keys())[0])
                    array.set_correcta(list(elem.items())[0][0])
                    if array.fin_partida():
                        user.update_score(puntaje.score, user.config['level'])
                        if (len(user.config['msg']['win']) > 0):
                            sg.popup(user.config['msg']['win'], background_color= theme.PRIMARY_COLOR, font= [theme.FONT, 15], no_titlebar= True, line_width = 15)
                        sg.popup(f'Puntaje obtenido: {puntaje.score}', background_color= theme.PRIMARY_COLOR, font= [theme.FONT, 15], no_titlebar= True, line_width = 30)
                        scores_dataset.fin_partida_win(user,list(elem.keys())[0])  
                        window.hide()
                        users.update_users(user)
                        highscores.start(users)
                        break
                else:
                    scores_dataset.un_fallo(user,list(elem.keys())[0])  
                    if puntaje.score > 0:
                        puntaje.subtract_point()
                        window['-SCORE-'].update(f'Puntaje: {puntaje.score}')
                    button_color = window[(0,0)].ButtonColor
                    for elem in ocurrencias_jugada:
                        for i in range(0, ocurrencias_jugada[elem][0]):
                            window[ocurrencias_jugada[elem][1][i]].update(button_color= 'red')
                    window.refresh()
                    delay += 2
                    time.sleep(2)
                    for elem in ocurrencias_jugada:
                        for i in range(0, ocurrencias_jugada[elem][0]):
                            window[ocurrencias_jugada[elem][1][i]].update('', button_color= button_color, image_filename= button_path)
                ocurrencias_jugada = {}
                
        if event == '-CLUE-':
            button_color = window[(0,0)].ButtonColor
            pos = array.get_clue()
            for elem in pos:
                window[elem].update(button_color= 'green')
            window.refresh()
            delay += 2
            time.sleep(2)
            for elem in pos:
                window[elem].update(button_color= button_color)
            window['-CLUE-'].update(disabled= True)
        ti = tiempo + delay - time.time() + start
        if (round(ti) == 30 and len(user.config['msg']['time']) > 0):
            sg.popup_auto_close(user.config['msg']['time'], auto_close_duration= 1, background_color= theme.PRIMARY_COLOR, font= [theme.FONT, 15], no_titlebar= True, 
            line_width = 15)
        elif (ti <= 0):
            if (len(user.config['msg']['lose']) > 0):
                sg.popup(user.config['msg']['lose'], font= [theme.FONT, 15], no_titlebar= True, background_color= theme.PRIMARY_COLOR, line_width = 15)
            scores_dataset.fin_partida_timeout(user,list(elem.keys())[0])  
            window.hide()
            highscores.start()
            break
        window['-TIMER-'].update("Tiempo restante: " + f"{round(ti//3600):02d}:{round(ti//60):02d}:{round(ti%60):02d}")
        
    return window