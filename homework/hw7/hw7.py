import collections

def choice():
    fn = input('Название файла без расширения: ') + '.txt'
    return fn

def wordlist(fn): #читает файл
    with open(fn, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace(",",".").replace(".","!").replace("!","?").replace("?","")
    t = t.lower()
    w = t.split()
    return w

def words1(w): #находит все -ed слова
    w1 = []
    for i,c in enumerate(w):
        if c.endswith('ed'):
            w1.append(c)
    return w1

def words2(w1): #находит все слова, образованные от глаголов на -y; лучше заморочиться и дать более "чистый" список
    w2 = []
    for i,c in enumerate(w1):
        if c.endswith('ied'):
            w2.append(c)
    return w2

def main():
    fn = choice()
    w = wordlist(fn)
    w1 = words1(w)
    w2 = words2(w1)
    d = collections.Counter(w1)
    o = collections.Counter(w2)
    print("Слова на '-ed': ", d)
    print("Глаголы, образованные от основ на '-y': ",o)


k = main()