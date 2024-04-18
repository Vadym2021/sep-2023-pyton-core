# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
#                                - другий повертає всі записи
from typing import Tuple, List


def todo():
    todo_list = []

    def add_task():
        task = input("Enter task:")
        todo_list.append(task)
        print("task added:", task)
        # print(f"Added task: {task}")

    def get_tasks():
        print(todo_list)
        return todo_list

    return add_task, get_tasks


add_task, get_tasks = todo()

while True:
    add_task()
    new_task = input("Add another task? (y/n):")
    if new_task.lower() != 'y':
        break

tasks = get_tasks()
print("All tasks:", tasks)


# 2) протипізувати перше завдання
def todo() -> Tuple[callable, callable]:
    todo_list: List[str] = []

    def add_task() -> None:
        task = input("Enter task:")
        todo_list.append(task)
        print("task added:", task)
        # print(f"Added task: {task}")

    def get_tasks() -> List[str]:
        print(todo_list)
        return todo_list

    return add_task, get_tasks


add_task, get_tasks = todo()

while True:
    add_task()
    new_task = input("Add another task? (y/n):")
    if new_task.lower() != 'y':
        break

tasks = get_tasks()
print("All tasks:", tasks)


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def transform() -> str:
    result = []
    num = input("Enter number:")
    for i, digit in enumerate(num):
        if digit != "0":
            result.append(f"{digit}{"0" * (len(num) - i - 1)}")
    # print(result)
    print("+".join(result))
    return "+".join(result)


transform()


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def counter_decorator(func):
    def decorator(*args, **kwargs):
        decorator.calls += 1
        result = func(*args, **kwargs)
        print('*' * 20)
        print(f"Function '{func.__name__}' was called {decorator.calls} times")
        print('*' * 20)
        return result

    decorator.calls = 0
    return decorator


def function():
    print("function called")


decorated_function = counter_decorator(function)

while True:
    decorated_function()
    new_task = input("Run again (y/n):")
    if new_task.lower() != 'y':
        break
