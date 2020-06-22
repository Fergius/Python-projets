def bread(func):
    def wrapper():
        print("</----\>")
        func()
        print("<\____/>")
    return wrapper

@bread
def sandwich(food="--ветчина--"):
    return food


print(sandwich())