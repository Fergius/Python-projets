"""Собственный пример декораторов"""


def wrapper(func):
    def inner():
        print("Приветствие перед началом работы основной функции")
        func()
        print("А здесь конец этого мира")

    return inner


def wrapper_the_second(func):
    def inner(number):
        print("Возводим число в квадрат")
        number **=2
        func(number)

    return inner


@wrapper
def simple_func(string):
    """Вывод строки"""
    print(string)


@wrapper
def more_func():
    print("Код")


@wrapper_the_second
def numbers(number):
    print(number)


numbers(10)


# simple_func("Здравствуй")
