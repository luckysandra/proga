import re

def f(filename):
    with open(filename, 'r', encoding='utf-8') as a:
        b = a.read()
    return b

def res(b):
    w = []
    res_praes = re.findall('[Пп]рограммиру[а-я]*[^\s,.!?:;]', b)
    res_perf = re.findall('[Пп]рограммировал[^н\s,.!?:;]*', b)
    res_misc = re.findall('[Пп]рограммировав[^н\s,.!?:;]*', b)
    w = res_praes + res_perf + res_misc
    return w

def forms(w):
    d = []
    for i,c in enumerate(w):
        if c in d[:i]:
            continue
        else:
            d.append(c)
    return d

def main():
    b = f(input('Введите файла с расширением: '))
    w = res(b)
    d = forms(w)
    b = print("Встретившиеся в тексте формы глагола 'программировать': ")
    for i in d:
        print(i)



main()