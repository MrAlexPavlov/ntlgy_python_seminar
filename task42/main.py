# Задача 42: Узнать какая максимальная households в зоне минимального значения population

# california_housing_train.csv

f_path = 'task40/california_housing_train.csv'

# Разбиваем строку и удаляем лишние ковычки
def separate(text):
    return [key.strip('"') for key in text.strip().split(',')]

# Фильтруем словарь, оставльяя только необходимое
def filterdict(f, dict_):
    return {i:items for i, items in file_dict.items() if f(items)}

# Среднее значение по полю field
def average(dict_, field):
    list_ = list(dict_.values())
    return round(sum([a[field] for a in list_]) / len(list_), 4)

def read_csv(path):
    dict_ = dict()
    with open(path) as f:
        # Вытаскиваем имена полей из первой строки файла
        field_list = separate(f.readline())
        for i, line in enumerate(f):
            value_list = separate(f.readline())
            # наполняем словарь данными из файла, с ключами имен полей
            dict_[i] = {key:float(value_list[a]) for a, key in enumerate(field_list)}
    return dict_

file_dict = read_csv(f_path)

sorted_list = sorted(file_dict.values(), key=lambda x: x['population'], reverse=False)

# Перебор отсортированного списка среди минимальных значений 'population'
# Мксимальный 'households'
population = next(iter(sorted_list))['population']
households = next(iter(sorted_list))['households']

for a,items in enumerate(sorted_list):
    if population < items['population']:
        break
    if households < items['households']:
        households = items['households']

print('Минимальное значение `population`: ',population)
print('Максимальное значение `households`: ',households)
