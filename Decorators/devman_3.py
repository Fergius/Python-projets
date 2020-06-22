""""Декоратор с именем функции"""

def make_string_upper(func):
    def inner(string):
        func(string.upper())
    inner.__name__ = func.__name__
    return inner

@make_string_upper
def print_text(string):
    print(string)

print(print_text.__name__)
