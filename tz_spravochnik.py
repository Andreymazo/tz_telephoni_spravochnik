from pathlib import Path
import pydoc
import readline

from service import binary_search, quick_sort

aa = int(input('Хотите ввести имя и номер - введите 1 или ищем - введите 2 посмотреть список имен и номеров - введите 3?'))
if aa == 1:

    a:str
    b:str
    d:int
    g:int
    c = '1'
    while c=='1':
        a, b, d, g = input(f'Введите Фамилию Имя Отчество, организацию, номер телефона раобчий, номер телефона сотовый через запятую:').split(',')
        print(a, b, d, g)
        try:
            f = open('telephone_spravochnik.txt', 'r+')
            data = f.read()
            f.write(f'{a}, {b}, {d}, {g}\n')
            f.close
            c = input('если хотите продолжить ввод, то введите 1, если нет то что-нибудь другое:')
        except IOError:
            f = open('telephone_spravochnik.txt', 'w+')
            data = f.read()
            f.write(f'{a}, {b}, {d}, {g}\n')
            f.close
            c = input('если хотите продолжить ввод, то введите 1, если нет то что-нибудь другое:')

if aa == 2:
    search_name = int(input('Введите цифру по которой ищем номер: по фамилии имени отчетсву - 0, по организации - 1'))
    with open('telephone_spravochnik.txt', 'r') as f:
        data = f.read().splitlines()
        # print(data)
        data_=[]
        for i in data:
            x = i.split(',')
            data_.append(x)
        quick_sort(data_, nomer=search_name)
        print(data_)
        name = input('Введите имя, по которому искать')
        print(data_[binary_search(0, len(data_)-1, data_, search_name, name)])#Pechataet index imeni, ego vstavlyaem v data_


if aa == 3:
    if Path('telephone_spravochnik.txt').is_file():
        with open('telephone_spravochnik.txt', 'r') as f:
            data = f.read()
            # print(data)
            pydoc.pager(data)
    if not Path('telephone_spravochnik.txt').is_file():
        print('Еще не ввели ни одного номера')



