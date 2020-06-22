""""Пример декораторов """


# декоратор
def make_string_upper(func):
    def inner(string):
        print('До')
        func(string.upper())
        print("После")

    return inner


@make_string_upper
def print_text(string):
    print(string)


print_text('Проверка')
print(print_text.__name__) # Вывод названия функции
