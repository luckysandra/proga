#Второй вариант

#Задание первое: прочесть файл и вывести словарные статьи для слов, длина
#которых больше или равна 20
w = []
a = ""
k = 0
d = 0
g = 0
j = 0
with open("Ozhegov.txt","r",encoding="utf-8") as f:
    b = f.read() 
    b_1 = b.split("\n")
for i,c in enumerate(b_1):
    print(c)
    print(i)
for i,c in enumerate(b_1):
    for s in c:
        if s == "|":
            break
        else:
            a += s
            k += 1
    if k >= 20:
        w.append(b_1[i])
    k = 0
    a = ""
if w != []:
    print('Слова, состоящие из двадцати и более букв')
    for i,c in enumerate(w):
        print(c)
else:
    print('Нет слов, состоящих из 20 и более букв')
            
        
#Задание второе: найти, у скольких слов представлены антонимы
#притом, что есть массив w, в котором уже есть словарные строки
for i,c in enumerate(b_1):
    for s in c:
        j += 1
        if k == 2:
            a += s
        elif s == "|":
            k += 1
    if a!="":
        d += 1
    k = 0
    a = ""
print(d)
##Troubleshooting: надо поправить вывод при ||, ибо оно его тоже учитывает
       
