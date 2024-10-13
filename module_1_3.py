# Создание переменной name
name = "Александр"
print("Name:", name)

# Создание переменной age
age = 34
print("Age:", age)

# Изменение значения age
age += 1  # Увеличиваем на 1
print("New Age:", age)

# Создание переменной is_student
is_student = True
print("Is Student:", is_student)

# Объявление переменных
completed_homework_count = 12  # Количество выполненных ДЗ
spent_hours = 1.5  # Количество затраченных часов
course_name = 'Python'  # Название курса

# Вычисление времени на одно задание
time_per_assignment = spent_hours / completed_homework_count  # Время на одно задание

# Вывод информации на экран
print("Курс:", course_name, ", всего задач:", completed_homework_count, ", затрачено часов:", spent_hours, ", среднее время выполнения", time_per_assignment, "часа.")

# Запись строки в переменную example
example = "Топинамбур"

# Вывод первого символа
print("Первый символ:", example[0])

# Вывод последнего символа с использованием отрицательного индекса
print("Последний символ:", example[-1])

# Вывод второй половины строки
middle_index = len(example) // 2
if len(example) % 2 == 0:
    second_half = example[middle_index:]  # Четное количество символов
else:
    second_half = example[middle_index + 1:]  # Нечетное количество символов
print("Вторая половина:", second_half)

# Вывод строки наоборот
reversed_example = example[::-1]
print("Слово наоборот:", reversed_example)

# Вывод каждого второго символа
every_second_character = example[1::2]  # Начинаем с индекса 1, чтобы получить второй символ
print("Каждый второй символ:", every_second_character)

