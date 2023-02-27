# Задача 40: Определить среднюю стоимость дома, 
# где кол-во людей от 0 до 500 (population)

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
filter_dict = filterdict(lambda x : x['population']<=500, file_dict)

print('средняя стоимость дома : ',average(file_dict,'median_house_value'))


