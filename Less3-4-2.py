import asyncio

async def set_future_result(delay, value, future: asyncio.Future):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    future.set_result(value)
    # return value

async def create_and_use_future():
    future = asyncio.Future()
    task = asyncio.create_task(set_future_result(2,"Успех",future))

    if not task.done():print("Состояние Task до выполнения: Ожидание")

    await task

    if future.done():print("Состояние Task после выполнения: Завершено")
        
    print(f'Результат из Task: {future.result()}')

async def main():
    await create_and_use_future()
    # result = await future
    # print(result)

asyncio.run(main())
input(':->')
