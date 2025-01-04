import asyncio

async def example_task():
    return "Задача выполнена"


async def main():
    task = asyncio.create_task(example_task())  # создание задачи из корутины example_task()
    await task  # запуск задачи и ожидание выполнения
    result = task.result()  # сохранение результата в переменную result
    print(result)

asyncio.run(main())
'''Вывод

Задача выполнена
'''
input(':->')
