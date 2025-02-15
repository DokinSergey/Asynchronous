import sys,time
import asyncio

# Создание объекта Lock
lock = asyncio.Lock()

async def my_task(task_id):
    print(f"Задача {task_id} ожидает блокировки с помощью Lock")
    # Ожидание получения блокировки
    await lock.acquire()
    try:
        print(f"Задача {task_id} получила блокировку")
        await asyncio.sleep(2)

    finally:
        print(f"Задача {task_id} блокировка снята")
        # Освобождение блокировки
        lock.release()

async def main():
    tasks = [asyncio.create_task(my_task(i)) for i in range(3)]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
