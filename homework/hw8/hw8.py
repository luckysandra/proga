import random

def make_dict(filename):
    d = {}
    with open(filename, encoding="utf-8") as f:
        a = f.readlines()
    for line in a:
        if line.endswith('\n'):
            line = line[:-1]
        w = line.split(',')
        d[w[1]] = w[0]
    return d

def randomizer(filename):
    a = make_dict(filename)
    keys = list(a.keys())
    return random.choice(keys)

def riddle():
    k = ''
    c = ''
    d = make_dict('1.csv')
    a = randomizer('1.csv')
    for keys,value in d.items():
        if keys == a:
            k = keys
            for i in range(len(a)):
                c += '.'
            print(value,' ',c)
        else:
            continue
    return k

def answer():
    a = riddle()
    b = input('Ваш ответ: ')
    while True:
        if b == a:
            print('Победа!')
            break
        else:
            print('Попробуйте ещё раз')
            b = input('Ваш ответ: ')


a = answer()