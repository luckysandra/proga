def splitter(text):
    k = 0
    d = []
    for i,line in enumerate(text):
        if line.endswith('.') or line.endswith('!') or line.endswith('?'):
           line = text[k:i+1]
           d.append(line)
           k = i+2
    return d

def sayOG(filename):
    with open(filename, 'r', encoding='utf-8') as a:
        text = a.read()
    w = splitter(text)
    k = 0
    d = {}
    d1 = {}
    for i,line in enumerate(w):
        line = line.split()
        for i,word in enumerate(line):
            word = word.strip()
            k = len(word)
            d[word] = k
        d1[line] = d
        print(d)
        d = {}
sayOG('1.txt')
