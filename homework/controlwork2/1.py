##var 2, Leonova Elizaveta

import re
import collections

def f():
    with open('irish.xml', 'r', encoding='utf-8') as a:
        b = a.readlines()
    return b

def forfive(b): #считаю число слов и пунктуации (т.е. то, что составляет строки)
    k = 0
    for line in b:
        if line.endswith('w>\n') or line.endswith('w>') or line.endswith('c>') or line.endswith('c>\n'):
            k += 1
    k = str(k)
    with open('2.txt', 'w', encoding='utf-8') as a:
        a.write(k)
    return k

#def foreight(b): #делаю массив и по нему запускаю коллекшнс"
#    d = []
#    for line in b:
#        if line.endswith('w>\n') or line.endswith('w>'):
#            d = line.split()
#            
#    
#    return d


def main():
    a = f()
    b = forfive(a)
#    c = foreight(a)

main()
    
            
