import sys,time
import asyncio

# Пример кода с успешной отменой задачи с помощью task.cancel():

async def main_task():
    print("Корутина main_task запустилась")
    await asyncio.sleep(5)
    print("Корутина main_task завершилась")

async def main():
    task = asyncio.create_task(main_task())
    await asyncio.sleep(1)
    task.cancel()  # Отмена задачи (запрос на отмену выполнения корутины main_task())

    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
