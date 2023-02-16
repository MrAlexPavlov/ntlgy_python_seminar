# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета

# Примеры:
# 385916 -> yes
# 123456 -> no

bus_ticket = input('Введите номер билета: ')

if int(bus_ticket):
    first_half = int(bus_ticket[:3])
    second_half = int(bus_ticket[3:])

    sum_first = first_half//100 + (first_half//10)%10 + first_half%10
    sum_second = second_half//100 + (second_half//10)%10 + second_half%10

    if sum_first == sum_second:
        answer = "Yes"
    else:
        answer = "No"

print(f"\nTicket #{bus_ticket} -> {answer}")