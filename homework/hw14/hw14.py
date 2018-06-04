def splitter(text):
    k = 0
    d = []
    for i,line in enumerate(text):
        if line.endswith('.') or line.endswith('!') or line.endswith('?'):
           line = text[k:i+1]
           d.append(line)
           k = i+2
    return d

def stripp(word):
    word = word.strip('.')
    word = word.strip('!')
    word = word.strip('?')
    word = word.strip(',')
    word = word.strip(':')
    word = word.strip(';')
    word = word.strip(' - ')
    word = word.strip('-')
    return word

def dd(w):
    lin = ''
    d = {}
    d1 = {}
    for i, line in enumerate(w):
        line = stripp(line)
        lin = line
        line = line.split()
        for i, word in enumerate(line):
            d = {stripp(word): len(stripp(word)) for word in line if len(stripp(word)) > 0}
        d1[lin] = d
        d = {}
    return d1

def printt(d):
    answer = input("Вывести словарь на экран? (да/нет): ")
    if answer == "да":
        for i in d:
            print('{}: {}'.format(i, d[i]))

def main(filename):
    with open(filename, 'r', encoding='utf-8') as a:
        text = a.read()
    w = splitter(text)
    d = dd(w)
    printt(d)

main('1.txt')
