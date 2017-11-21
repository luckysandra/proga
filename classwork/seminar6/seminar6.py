#with open(" ","r",encoding="utf-8") as f:
# r = прочесть файл
#with open(" ","w",encoding="utf-8") as f:
# w = перезапись
# если файла не было, то теперь он будет создан
# если существовал, полностью перезапишется весь файл (безвозвратно)
#with open(" ","a",encoding="utf-8") as f:
# a = дополнение

with open("котлован.txt","r",encoding="utf-8") as f:
    text = f.read()
lines = text.splitlines()
for i,line in enumerate(lines):
    line = lines[i]
    for k,word in range(len(line)):
        
        
    
with open("stats.tsv","w",encoding="utf-8") as a:

#для каждой строчки из исходного файла tsv
#сколько в строчке в файле слов и какое первое слово
