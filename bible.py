#coding: utf-8
import csv
def bible(a):
    if a == 'выход':
        exit()
    if a == 'меню':
        return True        
    reader = csv.reader(open("data.csv", "rb",),delimiter=';')
    name = 'По заданому запросу иформации не найдено'
    for x in reader:
        if len(x) == 3 and a == x[2]:
            name = x[0], x[1]
        elif len(x) == 3 and a == x[0]:
            name =  x[2]
    print ' '.join(name) 



def writer(b):
    if b == 'выход':
        exit()
    if b == 'меню':
        return True        
    writer = csv.writer(open('data.csv', 'a'), delimiter=';').writerow(b.split())
       

def vibor():
    v = raw_input('Выберите режим работы (внести, найти, выход): ')

    if v == 'внести':
        while not writer(raw_input('Внесите данные: ')):
            pass
    elif v == 'найти':
        while not bible(raw_input('Введите запрос: ')):
            pass
    else:
        exit()
vibor()