import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

async def counter(name_count:str):
    ncounter = 0
    while ncounter < max_counts[name_count]:
        ncounter +=1
        await asyncio.sleep(delays[name_count])
        print(f'{name_count}: {ncounter}')

async def main():
    task1 = asyncio.create_task(counter('Counter 1'))  # создаем 3 задач
    task2 = asyncio.create_task(counter('Counter 2'))
    task3 = asyncio.create_task(counter('Counter 3'))
    await asyncio.gather(task1,task2, task3)  # запускаем все задачи из списка tasks

asyncio.run(main())

input(':->')
