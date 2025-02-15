import sys,time
import asyncio

import threading


# Выводит сообщения о начале и завершении выполнения, а также идентификатор текущего цикла событий.
async def task1(task_id, loop):
    print(f"Задача {task_id} начинается, цикл = {loop}")
    print(f'Идентификатор цикла в задаче {task_id}: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(2)
    print(f"Задача {task_id} завершена")


async def task2(task_id, loop):
    # Аналогично task1, но с другой задержкой.
    print(f"Задача {task_id} начинается, цикл = {loop}")
    print(f'Идентификатор цикла в задаче {task_id}: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(3)
    print(f"Задача {task_id} завершена")

# Функция для запуска асинхронной задачи в отдельном цикле событий в новом потоке.
def start_loop(loop, coroutine):

    # Установка переданного цикла событий как текущего для потока.
    asyncio.set_event_loop(loop)

    # Запуск переданной корутины до её полного выполнения.
    loop.run_until_complete(coroutine)

# Главная асинхронная функция, координирующая создание циклов событий и запуск задач.
async def main():

    # Вывод идентификатора исходного (оригинального) цикла событий.
    print(f'Идентификатор оригинального цикла: {id(asyncio.get_running_loop())}')

    # Создание и вывод идентификаторов новых циклов событий для демонстрации их уникальности.
    loop1 = asyncio.new_event_loop()
    print(f'Идентификатор первого нового цикла: {id(loop1)}')
    loop2 = asyncio.new_event_loop()
    print(f'Идентификатор второго нового цикла: {id(loop2)}')

    # Подготовка асинхронных задач для запуска в отдельных циклах и потоках.
    coroutine1 = task1(1, loop1)
    coroutine2 = task2(2, loop2)

    # Создание и запуск отдельных потоков для выполнения асинхронных задач в разных циклах событий.
    thread1 = threading.Thread(target=start_loop, args=(loop1, coroutine1,))
    thread2 = threading.Thread(target=start_loop, args=(loop2, coroutine2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
