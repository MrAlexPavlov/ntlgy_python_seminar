# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random as rnd

# Генератор списка с уникальными цлочисленными значениями в заявленном диапазоне
def uniqrandomlist(n = 10, min = 0 ,max = 50):
    tmp_dict = dict()
    if (max - min)+1<n: return dict()
    while len(tmp_dict)<n:
        a = rnd.randint(min, max)
        tmp_dict[a] = 0
    return [i for i in tmp_dict.keys()]
        

i_list = uniqrandomlist(15, 1, 30)

i_min = int( input('Введите минимальное значения диапазона: ') )
i_max = int( input('Введите максимальное значения диапазона: ') )

print('\n',i_list)
print(f'{i_min} <= Значение <= {i_max}')

for i,val in enumerate(i_list):
    if i_min <= val <= i_max :
        print(f'индекс[{i}] значение:{val}')