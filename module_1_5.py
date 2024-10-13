# Создание кортежа immutable_var
immutable_var = (1, 2, 'a', 'b')

# Вывод кортежа на экран
print("Immutable tuple:", immutable_var)

# Попытка изменить элементы кортежа
try:
    immutable_var[0] = 10  # Это вызовет ошибку
except TypeError as e:
    print("Ошибка:", e)

# Объяснение
print("Кортеж (tuple) в Python является неизменяемым типом данных. Это означает, что после его создания "
      "нельзя изменить значения его элементов. Если попытаться изменить элемент кортежа, будет вызвана ошибка.")

# Создание списка mutable_list
mutable_list = [1, 2, 'a', 'b']

# Изменение элементов списка
mutable_list[0] = 10  # Изменяем первый элемент
mutable_list.append('Modified')  # Добавляем новый элемент

# Вывод измененного списка на экран
print("Mutable list:", mutable_list)
