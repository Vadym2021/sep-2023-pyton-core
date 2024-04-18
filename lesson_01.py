# Завдання 1
def extract_digits(input_string):
    digits = [char for char in input_string if char.isdigit()]
    return ', '.join(digits)

# Завдання 2
def extract_numbers(input_string):
    import re
    numbers = re.findall(r'\b\d+\b', input_string)
    return ', '.join(numbers)

# Завдання з list comprehension 1
greeting = 'Hello, world'
chars_upper = [char.upper() for char in greeting]

# Завдання з list comprehension 2
odd_squares = [num**2 for num in range(51) if num % 2 != 0]

# Функції
def print_list(some_list):
    print(some_list)

def max_of_three(a, b, c):
    maximum = max(a, b, c)
    print(maximum)
    return maximum

def min_of_many(*args):
    minimum = min(args)
    print(max(args))
    return minimum

def max_in_list(some_list):
    return max(some_list)

def min_in_list(some_list):
    return min(some_list)

def sum_of_list(some_list):
    return sum(some_list)

def average_of_list(some_list):
    return sum(some_list) / len(some_list)

# Завдання 1
numbers_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
min_number = min(numbers_list)
unique_numbers = list(set(numbers_list))
for i in range(3, len(numbers_list), 4):
    numbers_list[i] = 'X'

# Завдання 2
def draw_square(side_length):
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            print('*' * side_length)
        else:
            print('*' + ' ' * (side_length - 2) + '*')

# Завдання 3
def multiplication_table():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(f'{i} * {j} = {i * j}')
            j += 1
        i += 1

# Завдання 4
def menu():
    while True:
        print('1. Завдання 1')
        print('2. Завдання 2')
        print('3. Вийти')
        choice = input('Виберіть завдання (1-3): ')
        if choice == '1':
            input_string = input('Введіть рядок: ')
            print(extract_digits(input_string))
        elif choice == '2':
            input_string = input('Введіть рядок: ')
            print(extract_numbers(input_string))
        elif choice == '3':
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')

# Виклик функцій та вивід результатів
print(f"Завдання 1: {extract_digits('as 23 fdfdg544')}")
print(f"Завдання 2: {extract_numbers('as 23 fdfdg544 34')}")
print(f"Завдання з list comprehension 1: {chars_upper}")
print(f"Завдання з list comprehension 2: {odd_squares}")
print("Функції:")
print_list([1, 2, 3, 4, 5])
max_of_three(1, 2, 3)
min_of_many(1, 2, 3, 4, 5)
print(f"Максимум зі списку: {max_in_list([1, 2, 3, 4, 5])}")
print(f"Мінімум зі списку: {min_in_list([1, 2, 3, 4, 5])}")
print(f"Сума списку: {sum_of_list([1, 2, 3, 4, 5])}")
print(f"Середнє значення списку: {average_of_list([1, 2, 3, 4, 5])}")
print("Завдання 1:")
print(f"Мінімальне число: {min_number}")
print(f"Унікальні числа: {unique_numbers}")
print(f"Список замінений числами X: {numbers_list}")
print("Завдання 2:")
draw_square(5)
print("Завдання 3:")
multiplication_table()
print("Завдання 4:")
menu()
