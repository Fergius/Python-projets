import asyncio


async def my_async_function():
    print("Я чем то занимаюсь")
    await asyncio.sleep(0)
    print("Продолжаю чем-то заниматься")

coroutine = my_async_function()

coroutine.send(None)

