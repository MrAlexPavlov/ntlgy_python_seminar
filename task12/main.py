# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

limit = 1000
peters_prod_number = int(input('Введите произведение чисел: '))
peters_sum_number = int(input('Введите сумму чисел: '))

decided = False
for a in range(limit + 1):
    for b in range(limit + 1):
        sum, prod = a + b, a * b
        if ( sum == peters_sum_number 
            and prod == peters_prod_number ):
            decided = True
            break
    if decided: break

if decided: 
    print(f"оба числа найдены {a} и {b}")
else:
    print(f"числа не надены")



