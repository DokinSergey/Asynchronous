import sys,time
import asyncio

# объявление асинхронной функции producer, принимающей аргумент queue
async def producer(n, queue, prod_range):
    for i in range(*prod_range):
        item = f'Элемент {i}'  # создание строки с элементом и его номером
        await queue.put(item)  # добавление элемента в очередь
        print(f'producer {n} добавил в очередь элемент: {item}')
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


# объявление асинхронной функции consumer, принимающей аргумент queue
async def consumer(queue):
    while True:
        item = await queue.get()  # получение элемента из очереди
        if item is None:  # если элемент равен None - выход из цикла
            break
        print(f'consumer получил из очереди элемент: {item}')
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


async def main():
    queue = asyncio.Queue()  # создание очереди

    # создание задач для функции producer и consumer
    prod_task_1 = asyncio.create_task(producer(1, queue, (0, 10, 2)))
    prod_task_2 = asyncio.create_task(producer(2, queue, (1, 10, 2)))
    cons_task = asyncio.create_task(consumer(queue))
    await prod_task_1
    await prod_task_2
    await queue.put(None)  # добавление элемента None в очередь для выхода из цикла
    await cons_task

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
