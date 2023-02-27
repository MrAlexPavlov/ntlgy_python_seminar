# Задача 40: Определить среднюю стоимость дома, 
# где кол-во людей от 0 до 500 (population)

# california_housing_train.csv

f_path = 'task40/california_housing_train.csv'

def separate(text):
    return [key.strip('"') for key in text.strip().split(',')]

def filterdict(f, dict_):
    return {i:items for i, items in file_dict.items() if f(items)}

def average(dict_, field):
    list_ = list(dict_.values())
    return round(sum([a[field] for a in list_]) / len(list_), 4)

def read_csv(path):
    dict_ = dict()
    with open(path) as f:
        field_list = separate(f.readline())
        # print(field_list)
        for i, line in enumerate(f):
            value_list = separate(f.readline())
            # print(value_list)
            dict_[i] = {key:float(value_list[a]) for a, key in enumerate(field_list)}
            # print(dict_)
            # return
    return dict_

file_dict = read_csv(f_path)

filter_dict = filterdict(lambda x : x['population']<=500, file_dict)

# print(len(file_dict),' =>',len(filter_dict))
print('средняя стоимость дома : ',average(file_dict,'median_house_value'))

