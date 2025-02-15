import sys,time
import asyncio

#вот так правильно
async def task(number, locks):
    # Определяем порядок захвата блокировок по их идентификаторам
    sorted_locks = sorted(locks, key=id)

    print(f"Задача {number}: пытается захватить блокировки в порядке {sorted_locks}")
    async with sorted_locks[0]:
        async with sorted_locks[1]:
            print(f"Задача {number}: захватила обе блокировки")
            await asyncio.sleep(1)  # Имитация работы в критическом участке
    print(f"Задача {number}: завершила выполнение")

#вот так усё повиснет
# async def task(number, first_lock, second_lock):
    # print(f"Задача {number}: пытается захватить первую блокировку")
    # async with first_lock:
        # print(f"Задача {number}: захватила первую блокировку")
        # await asyncio.sleep(1)  # Имитация работы в критическом участке
        # print(f"Задача {number}: пытается захватить вторую блокировку")
        
        # async with second_lock:
            # print(f"Задача {number}: захватила вторую блокировку")
            # await asyncio.sleep(1)  # Дополнительная работа в критическом участке
    # print(f"Задача {number}: завершила выполнение")

async def main():
    # Инициализация двух асинхронных блокировок
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()

    # Запуск корутин с блокировками, передаваемыми в разном порядке, но захватывающимися в одном и том же порядке
    await asyncio.gather(

        task(1, [lock1, lock2]),
        task(2, [lock2, lock1]),
    )

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
