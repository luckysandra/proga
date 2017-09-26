
####print(s[1])
####i = 2
####print(s[i])
##
##i = 0
##s1=""
##
####if "ov" in s:
####    print('ov')
####elif "o" in s:
####    print('o')
##
####for c in s:
####    if c == "o":
####        continue
####    print(c)
####    i += 1
####    if c == "i":
####        break
####    s1 += c
####print(s1)
####    
####    print(s)
####print(i)
##
####l = len(s)
####i = 0
####
####while i < l:
####    print(s[i])
####    i += 1
##
####
####for i,c in enumerate(s):
####    if i == 5:
####        print(c)
##        
##for i in range(len(s)):
##    print(s[i])

a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
s = input()
w = ''
##while s != "": ##Альтернативное решение первой задачи
##    print(s)
##    s = input('Введите слово: ')

while True:
    if s != "":
        break
    print(s)
    ## Моя цель - внутренний цикл, который смотрит на букву,
    ## ищет ей соответствие в i, ставит ей в соответствие
    ## следующий по индексу элемент и выводит новую строку.
    s = input('Введите слово: ')
    

