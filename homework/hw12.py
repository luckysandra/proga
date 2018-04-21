import os
import re

#Сколько найдено файлов, название которых состоит только из латинских символов.

def poisk():
    file_list = os.listdir()
    w = []
    for i,c in enumerate(file_list):
        res = re.match('[^а-яА-Я0-9]+[.][^а-яА-Я]*', c)
        if res:
            a = res.group()
            w.append(a)
        else:
            continue
    return w

def nineten(w):
    d = []
    for i,c in enumerate(w):
        if c in d[:i]:
            continue
        else:
            d.append(c)
    return d

def main():
    w = poisk()
    print('Все найденные файлы: ')
    for i in w:
        print(i) #пишет все сразу
    print('Файлы без повторов: ')
    d = nineten(w)
    for i in d:
        print(i) #пишет без повторов

#Мне кажется, что рациональнее делать одну выдачу, потому что
#файлы с одним названием не могут быть в одной папке, а папки
#программа не ищет, но меня смутила фраза "кроме этого", и я
#сделала две выдачи. 
        
main()
    
