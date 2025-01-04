import asyncio

async def n_coroutine(a):
    await asyncio.sleep(1)
    print(f'Coroutine {a} is done')

async def main():
    tasks = []
    for i in range(1,4):
        task = asyncio.create_task(n_coroutine(i))  # создаем 3 задач
        tasks.append(task)  # добавляем все задачи в список tasks
    await asyncio.gather(*tasks)  # запускаем все задачи из списка tasks

asyncio.run(main())

input(':->')
