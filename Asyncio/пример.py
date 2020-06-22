import asyncio


async def count_to_three():
    print("Веду отсчет. 1")
    await asyncio.sleep(0)
    print("Веду отсчет. 2")
    await asyncio.sleep(0)
    print("Веду отсчет. 3")


coroutine_counter = count_to_three()
while True:
    try:
        coroutine_counter.send(None)
    except StopIteration:
        break
#print(coroutine_counter)
coroutine_counter.send(None)  # Выведет 1
coroutine_counter.send(None)  # Выведет 2
coroutine_counter.send(None)  # Выведет 3
coroutine_counter_new = count_to_three()
coroutine_counter_new.send(None)
