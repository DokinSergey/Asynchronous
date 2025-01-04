import asyncio

async def print_with_delay(a):
    await asyncio.sleep(1)
    print(f'Coroutine {a} is done')

async def main():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(print_with_delay(i))  # создаем 3 задач
        tasks.append(task)  # добавляем все задачи в список tasks
    await asyncio.gather(*tasks)  # запускаем все задачи из списка tasks

asyncio.run(main())

input(':->')
