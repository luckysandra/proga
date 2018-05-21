with open('text.txt', 'r', encoding='utf-8') as a:
    text = a.read()
    text = text.split()
b = []
for word in text:
    word = word.strip(',.!?-')
    if word != '':
        b.append(word)
a = [word.lower() for word in b]
for i,c in enumerate(a):
    print('{:<2}. {}'.format(i,c))
    
    
