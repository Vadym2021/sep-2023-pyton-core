# 1) Є ось такий файл...
# ваша задача записати в новий файл тільки
# email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)

with open('emails.txt', 'r') as file:
    lines = file.readlines()

filtered_emails = []
for line in lines:
    parts = line.split()
    # print(parts)
    try:
        email = parts[1]
        # print(email)
        if email.strip().endswith('@gmail.com'):
            filtered_emails.append(email)
    finally:
        pass
    # except IndexError:
    #     pass
# print(filtered_emails)
with open('output.txt', 'w') as file:
    for email in filtered_emails:
        file.write(email + '\n')




# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
#                                      - всі покупки зберігаємо в файлі
# з функціоналу:
# * вивід всіх покупок
#              * має бути змога додавати покупку в книгу
#                                                  * має бути змога шукати по будь якому полю покупку
#                                                                                             * має бути змога показати найдорожчу покупку
#                                                                                                                                  * має бути можливість видаляти покупку по id
# (ну і меню на це все)




# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

res = []
added_ids = set()

for sublist in data:
    for item in sublist:
        if item["id"] not in added_ids:
            res.append(item["id"])
            added_ids.add(item["id"])

print(res)
