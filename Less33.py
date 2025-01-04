import asyncio


async def example_coroutine():
    await asyncio.sleep(1)
    print("Hello from coroutine!")

async def main():
    tasks = []
    for _ in range(10):
        task = asyncio.create_task(example_coroutine())  # создаем 10 задач
        tasks.append(task)  # добавляем все задачи в список tasks
    await asyncio.gather(*tasks)  # запускаем все задачи из списка tasks

asyncio.run(main())

input(':->')
