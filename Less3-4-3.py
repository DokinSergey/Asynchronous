import sys

import asyncio

async def set_future_result(delay, value):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value

async def create_and_use_future():
    # future = asyncio.Future()
    task = asyncio.create_task(set_future_result(2,"Успех"))

    if not task.done():print("Состояние Task до выполнения: Ожидание")
    print("Задача запущена, ожидаем завершения...")

    await task

    if task.done():print("Состояние Task после выполнения: Завершено")

    # print(f'Результат из Task: {task.result()}')

    return task.result()

async def main():

    result = await create_and_use_future()
    print("Результат из Task:", result)

asyncio.run(main())

if not len(sys.argv) > 1 and sys.argv[1] == 'cons':input(':-> ')
sys.exit(0)
