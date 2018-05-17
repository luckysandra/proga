import os
import collections

def main():
    w = []
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        w.append(dirs) 
    l = []
    for i,c in enumerate(w):
        c = w[i]
        for k,j in enumerate(c):
            l.append(j[0])
    counter = collections.Counter(l)
    print(counter)

main()
