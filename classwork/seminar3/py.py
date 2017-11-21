with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
    text2 = text.split(".")
    print(text2)
