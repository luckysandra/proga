import os
import re

#def pw():
#    path_way = '.'
#    a = []
#    for root, dirs, files in os.walk(path_way):
#        a = files

#for c in a:
#    with open(c, 'r', encoding='') as f:
#        text = f.readlines()
with open('_itartass1.xhtml', 'r', encoding='windows-1251') as f:
    text = f.readlines()
    for line in text:
        res = re.match('<meta content',line)
        if res:
            #прошу прощения за последующую громоздкость
            #не могу вспомнить, как делать серч по тегам,
            #а написать хоть что-то на экзамене нужно...
            tagging = re.search('content="[a-zA-Z0-9а-яА-Я]*" name="tagging"',line)
            if tagging:
                a = tagging.group()
                a = a[9:15]
            doc_id = re.search('content="[a-zA-Z0-9а-яА-Я]*" name="docid"',line)
            if doc_id:
                b = doc_id.group()
                b = b[9:13]
            title = re.search('content="[a-zA-Z0-9а-яА-Я]*" name="header"',line)
            if title:
                c = title.group()
                c = c[9:14]
            author = re.search('content="[a-zA-Z0-9а-яА-Я]*" name="author"',line)
            if author:
                d = author.group()
                d = d[9:14]
            created = re.search('content="[a-zA-Z0-9а-яА-Я]*" name="created"',line)
            if created:
                e = created.group()
                e = e[9:15]
            topic = re.search('content="[a-zA-Z0-9а-яА-Я]*" name="topic"',line)
            if topic:
                g = topic.group()
                g = g[9:13]
with open('for_five.txt', 'w', encoding='utf-8') as f:
    f.write(a)
    f.write(b)
    f.write(c)
    f.write(d)
    f.write(e)
    f.write(g)
                
  
            
        
