import sys,time
# from random import random
import asyncio
# При выводе в консоль можно использовать ANSI коды
RED = '\033[31m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
END = '\033[0m'  # Возврат к настройкам


async def customer(queue):
    # Цикл работает до опустошения очереди
    while not queue.empty():
        await asyncio.sleep(.5)
        elem = queue.get_nowait()
        print(f'Из очереди получен элемент_{elem}')

    print(f'{YELLOW}Очередь опустошена{END}')
    # Применяем метод get_nowait() для вызова исключения asyncio.QueueEmpty
    try:
        elem = queue.get_nowait()
        print(f'Из очереди получен элемент_{elem}')  # Принт не сработает
    except asyncio.QueueEmpty:
        print(f'{RED}Попытка получить элемент из пустой очереди методом get_nowait() вызвала asyncio.QueueEmpty{END}')


async def producer(queue):
    for i in range(5):
        await asyncio.sleep(.5)
        queue.put_nowait(i)
        print(f'В очередь поставлен элемент_{i}')
        if queue.full():  # Если очередь заполнена
            print(f'{YELLOW}Очередь заполнена{END}')
            try:
                # Применяем метод put_nowait() для вызова исключения asyncio.QueueFull
                queue.put_nowait(i + 1)
                print(f'В очередь поставлен элемент_{i}')  # Принт не сработает
            except asyncio.QueueFull:
                print(
                    f'{RED}Попытка поместить элемент в заполненную очередь методом put_nowait() вызвала asyncio.QueueFull{END}')
                print(f'{GREEN}Запускаем процесс получения элементов из очереди{END}')
                # Приостанавливаем producer() и ожидаем выполнения customer()
                await customer(queue)


async def main():
    # Создаем очередь с maxsize == 5
    queue = asyncio.LifoQueue(5)
    print(f'{GREEN}Емкость созданной очереди: {queue.maxsize} элементов{END}')
    prod = asyncio.create_task(producer(queue))
    # Приостанавливаем текущую задачу и ожидаем выполнения prod
    await prod
    print('End')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
