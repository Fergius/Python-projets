# очередной пример декоратора

def print_text(string):
    print(string)


print_text('привет')


def make_string_upper(func):
    def inner(string):
        func(string.upper())

    return inner


# так выглядит декаротор без использования @
print_upper_string = make_string_upper(print_text)
print_upper_string('hello')

# декоратор с @
@make_string_upper
def print_more_text(string):
    print(string)

print_more_text('привет')
