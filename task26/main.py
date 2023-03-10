# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

#Рекурсивная функция возведения в степень
def MathPower(x, y):
    if y == 0: return 1
    return MathPower(x, y-1) * x


a = int(input('Введите число A: '))
b = int(input(f'Введите B степень числа {a}: '))

power_ab = MathPower(a, abs(b))

# Для вывода информации при отрицательной степени
answer = ''
if b < 0:
    answer = f' 1/{power_ab}'
    power_ab = 1/power_ab

print(f'A = {a}; B = {b} -> {power_ab}{answer}')