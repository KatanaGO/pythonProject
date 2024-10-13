# Работа со словарями
# Создание словаря my_dict
my_dict = {
    'Vasya': 1975,
    'Egor': 1999,
    'Masha': 2002
}

# Вывод словаря на экран
print("Dict:", my_dict)

# Вывод значения по существующему ключу
print("Existing value:", my_dict.get('Masha'))

# Вывод значения по отсутствующему ключу с обработкой
print("Not existing value:", my_dict.get('NonExistingKey', None))

# Добавление двух новых пар в словарь
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915

# Удаление одной пары по существующему ключу
deleted_value = my_dict.pop('Egor', None)  # Удаляем Egor и сохраняем значение
print("Deleted value:", deleted_value)

# Вывод измененного словаря на экран
print("Modified dictionary:", my_dict)

# Работа с множествами
# Создание множества my_set
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}  # Повторяющееся значение будет проигнорировано

# Вывод множества на экран
print("Set:", my_set)

# Добавление двух новых элементов в множество
my_set.add(13)
my_set.add((5, 6, 1.6))

# Удаление одного элемента из множества
my_set.pop()  # Удаляем произвольный элемент

# Вывод измененного множества на экран
print("Modified set:", my_set)
