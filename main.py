# main.py

# Задача 1 (просто) "Арифметика"
# 1st program
result1 = 9 ** 0.5 * 5
print(result1)

# Задача 2 (просто) "Логика"
# 2nd program
result2 = 9.99 > 9.98 and 1000 != 1000.1
print(result2)

# Задача 3 (средне) "Школьная загадка"
# 3rd program
result3_no_priority = 2 * 2 + 2
result3_with_priority = 2 * (2 + 2)
comparison_result = result3_no_priority == result3_with_priority
print(result3_no_priority)
print(result3_with_priority)
print(comparison_result)

# Задача 4 (сложно) "Первый после точки"
# 4th program
number_str = '123.456'
number_float = float(number_str) # Преобразуем строку в число
shifted_number = number_float * 10 # Умножаем на 10
first_digit_after_decimal = int(shifted_number) % 10 # Получаем первую цифру после запятой
print(first_digit_after_decimal)