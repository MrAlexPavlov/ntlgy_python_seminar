# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

n = int( input('Введите число натуральное число N: ') )

if n < 0:
    print(f"{n} не натуральное число! ")
else:
    pows, num_str = 2, '1 ' # 2 в степени 0 ровно 1
    while pows <= n:
        num_str += f"{pows} "
        pows *=2 
    print(f"{n} -> {num_str}")

