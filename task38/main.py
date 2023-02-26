# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

import json

# Вывод на экран словаря
def show_select(dict_):
    for i,items in dict_.items():
        res = ''.join([f"{key}: {val}\t" for key, val in items.items()])
        print(i, res)

# Выводим записи из файла, все или какую-то конкретную
def select(file_name, wfield = '', wstr = ''):
    with open(file_name) as f:
        dict_ = dict()
        for i, line in enumerate(f):
            line = line.strip()
            dict_[i] = json.loads(line)

            if wstr != '' and dict_[i][wfield] == wstr:
                return {i:dict_[i]}
    return dict_

# Получаем поле и значения для поиска
def search_request(text):
    res = input(text).split(':')
    return res[0], res[1]

# Работа с файлом, вставляем запись в файл
def insert(file_name, dict_, attr = 'a'):
    with open(file_name, attr) as f:
        for key, item in dict_.items():
            json.dump(item, f)
            f.write('\n')

# Обновление или удаления записи в справочнике
def update(file_name, id, wfield = '', wstr = '', delete = False):
    dict_ = select(file_name)
    if delete == True:
        dict_.pop(id)
        insert(file_name, dict_, attr = 'w')
    else:
        dict_[id][wfield] = wstr
        insert(file_name, dict_, attr = 'w')

#  Заполняем поля для записи в файл
def book_data(fld):
    return {key:input(val) for key,val in fld.items()}



# Имя файла и поля справочника
file_name = 'base.txt'
fields = {
    'name':'Имя:',
    'surname':'Фамилия:',
    'phone':'Номер телефона:',
    'adress':'Адрес:'
}

# Выводим инструкцию по пользованию справочником передстартом работы
instruction = [
    's - Вывод всей информации из записной книжки',
    'i - Добавить запись',
    'f - Найти запись',
    'e - Отредактировать запись',
    'd - Удалить запись',
    'q - Закончить работать с записной книжкой',
    'h - Вызов этой инструкции'
]
print(*instruction, sep="\n")

# Ожидание команды от пользователя
while True:
    letter = input('ожидание команды: ').lower()

    if letter == 'h':
        print(*instruction, sep="\n")

    elif letter == 'q':
        break

    elif letter == 'e':
        field, search = search_request('где:что -> ')
        id = list( select(file_name, field, search).keys() )[0]
        new = input(f'Заменить {field} на: ')
        update(file_name, id, field, new)

    elif letter == 'd':
        field, search = search_request('где:что -> ')
        id = list( select(file_name, field, search).keys() )[0]
        update(file_name, id, delete=True)

    elif letter == 'f':
        field, search = search_request('где:что -> ')
        show_select( select(file_name, field, search) )

    elif letter == 'i':
        msg = dict()
        msg[0] = book_data(fields)
        insert(file_name, msg)

    elif letter == 's':
        show_select( select(file_name) )
