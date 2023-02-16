# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

user_int = int(input('Введите трехзначное число: '))
answer = user_int//100 + (user_int//10)%10 + user_int%10

print(
    f"{user_int} -> "
    f" = {answer} "
    f"({user_int//100} + {(user_int//10)%10} + {user_int%10})",
)
