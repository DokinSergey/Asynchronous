import sys,time
import asyncio
import threading

# Корутина, которая будет выполнена в каждом из независимых потоков.
async def task(loop, num):
    # Получаем id потока в котором выполняется задача.
    thread_id = threading.current_thread().ident
    # Получаем текущий цикл событий.
    e_loop_id = asyncio.get_running_loop()
    print(
        f"Задача task_{num} запущена в потоке id: {thread_id}, "
        f"текущий event loop id: {id(e_loop_id)}, "
        f"переданный event loop id: {id(loop)}")
    await asyncio.sleep(num)
    print(f"Задача task_{num} завершена!")


# Функция для запуска асинхронного цикла событий в отдельном потоке.
def start_loop(loop, coro, num):
    # Установка переданного цикла событий в качестве текущего для этого потока.
    asyncio.set_event_loop(loop)
    # Запуск задачи в установленном цикле событий, ожидание ее результата.
    loop.run_until_complete(coro(loop, num))
    # Закрываем цикл событий
    loop.close()

# Основная асинхронная функция, управляющая созданием циклов событий и потоков.
async def main():

    print(f'main()\nТекущий поток id: {threading.current_thread().ident}\n'
          f'Текущий цикл событий id: {id(asyncio.get_running_loop())}\n{"-" * 50}')
    loop1 = asyncio.new_event_loop()  # Создание нового цикла событий.
    print(f'Создан новый цикл событий id: {id(loop1)}')
    loop2 = asyncio.new_event_loop()  # Создание еще одного нового цикла событий.
    print(f'Создан новый цикл событий id: {id(loop2)}\n{"-" * 50}')

    # Создание и запуск независимых потоков для каждого цикла событий и корутины.
    thread1 = threading.Thread(target=start_loop, args=(loop1, task, 1,))
    thread2 = threading.Thread(target=start_loop, args=(loop2, task, 2))

    # Запуск потоков.
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков.
    thread1.join()
    thread2.join()

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
