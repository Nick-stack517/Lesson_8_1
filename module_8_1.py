"""
2023/11/24 00:00|Домашнее задание по теме "Try и Except"

Задание "Программистам всё можно":
Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не
можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!
"""


def add_everything_up(a, b):
    try:
        res = a + b
        res = round(res, 3)
    except TypeError:
        # print("Чейто не того")
        res = str(a) + str(b)
    return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
