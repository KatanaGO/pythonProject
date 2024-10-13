# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем отсортированный список имен студентов
sorted_students = sorted(students)

# Создаем словарь для хранения среднего балла
average_grades = {}

# Подсчет среднего балла для каждого студента
for i, student in enumerate(sorted_students):
    average_grades[student] = sum(grades[i]) / len(grades[i])

# Вывод результата
print(average_grades)
