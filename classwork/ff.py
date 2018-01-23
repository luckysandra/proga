import random
def f1():
    with open("text.txt","r",encoding="utf-8") as a:
        text = a.read()
        text.strip(",.:;")
        splited_text = text.split() #split list
    with open("word.csv","w",encoding="utf-8") as d:
        for i,c in enumerate(splited_text):
            k = 0
            d.write(c)
            d.write("\t")
            c = c.lower()
            while k <= 2:
                s = list(c)
                random.shuffle(s)
                c = "".join(s)
                d.write(c)
                d.write("\t")
                k += 1
            d.write("\n")
f1()
        



