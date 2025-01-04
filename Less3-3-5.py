import asyncio

max_counts = {
    'Counter 1': 13,
    'Counter 2': 7
}

async def counter(name_count:str,delay:int):
    ncounter = 0
    while ncounter < max_counts[name_count]:
        ncounter +=1
        await asyncio.sleep(delay)
        print(f'{name_count}: {ncounter}')

async def main():
    task1 = asyncio.create_task(counter('Counter 1',1))  # создаем 3 задач
    task2 = asyncio.create_task(counter('Counter 2',1))
    await asyncio.gather(task1,task2)  # запускаем все задачи из списка tasks

asyncio.run(main())

input(':->')
