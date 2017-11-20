# var = 4
b = 0
i = 0
with open("text.txt", encoding="utf-8") as a:
    text = a.read()
    splited_text = text.split()
for line in text:
    if line.endswith(",") or line.endswith("."):
        b += 1
print(b)
for i,c in enumerate(splited_text):
    i += 1
print(i)
i = b/i*100
print("Процент слов с прилипшими знаками препинания в тексте: ",i,"%")
