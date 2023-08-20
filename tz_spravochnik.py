from pathlib import Path
import pydoc
import readline

def sort_single_file(nums, low, high, nomer):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i][nomer] < pivot[nomer]:
            i += 1

        j -= 1
        while nums[j][nomer] > pivot[nomer]:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums, nomer):
        def _quick_sort(items, low, high):
            if low < high:
                split_index = sort_single_file(items, low, high, nomer)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

def binary_search(low, high, values, item_to_find):
    while low <= high:
        mid = low + (high - low) // 2

        if item_to_find == values[mid][0]:
            return mid
        elif item_to_find < values[mid][0]:
            high = mid - 1
        elif item_to_find > values[mid][0]:
            low = mid + 1

    return 'No such name'

aa = int(input('Хотите ввести имя и номер - введите 1 или ищем - введите 2 посмотреть список имен и номеров - введите 3?'))
if aa == 1:

    a:str
    b:int
    a, b = input(f'Введите имя и номер телефона через запятую:').split(',')
    print(a,b)
    try:
        f = open('telephone_spravochnik.txt', 'r+')
        data = f.read()
        f.write(f'{a},{b}\n')
        f.close
    except IOError:
        f = open('telephone_spravochnik.txt', 'w+')
        data = f.read()
        f.write(f'{a},{b}\n')
        f.close

if aa == 2:
    name = input('Введите имя, по которому ищем номер')
    with open('telephone_spravochnik.txt', 'r') as f:
        data = f.read().splitlines()
        print(data)
        data_=[]
        for i in data:
            x = i.split(',')
            data_.append(x)
        quick_sort(data_, nomer=0)
        print(data_)
        print(data_[binary_search(0, len(data_)-1, data_, name)])#Pechataet index imeni, ego vstavlyaem v data_


if aa == 3:
    if Path('telephone_spravochnik.txt').is_file():
        with open('telephone_spravochnik.txt', 'r') as f:
            data = f.read()
            # print(data)
            pydoc.pager(data)
    if not Path('telephone_spravochnik.txt').is_file():
        print('Еще не ввели ни одного номера')



