import random
def nouns():
    with open("word1.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
    words = []
    for line in a:
        if line.endswith("\n"):
            line = line[:-1]
            words.append(line)
    return random.choice(words)

def adj():
    with open("word2.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
    words = []
    for line in a:
        if line.endswith("\n"):
            line = line[:-1]
            words.append(line)
    return random.choice(words)

def zwei():
    with open("word3.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
    words = []
    for line in a:
        if line.endswith("\n"):
            line = line[:-1]
            words.append(line)
    return random.choice(words)

def begend():
    a = nouns() + ' ' + 'ist' + ' ' + adj() + '.'
    print(a)
    
def middle():
    a = nouns() + ' ' + 'ist' + ' ' + adj() + ' ' + 'und' + ' ' + zwei() + '.'
    print(a)

def poem():
    begend()
    middle()
    begend()
        
f = poem()


