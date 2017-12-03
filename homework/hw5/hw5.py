#var = 4

w = []
a = input('Введите слово: ')
while a != "":
    b = list(a)
    c = "".join(b[-2:])
    if c == 're' or c == 'ri':
        w.append(a)
    a = input('Введите слово: ')
with open('hw5.txt', 'w', encoding='utf-8') as f:
    for i,c in enumerate(w):
        f.write(c)
        f.write('\n')