# Декоратор это функция, ожидающая другую функцию в качестве параметра
def my_shiny_new_decorator(a_function_to_decorate):
    # внутри себя декоратор определяет функцию обертку.
    # она будет обернута вокруг декорируемой
    # получая возможность исполнять произвольный код до и после неё

    def the_wrapper_around_the_original_function():
        # поместим здесь код, который хотим запускать до вызова функции
        # оригинальной функции
        print("Я код, который отработает до вызова функции")

        # вызовем саму декорируемую функцию
        a_function_to_decorate

        # А здесь поместим код, который хотим запускать после вызова
        # оригинальной функции
        print("А я код, срабатывающий после")

    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    return "Я одинокая функция"

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function())

print(a_stand_alone_function_decorated())

