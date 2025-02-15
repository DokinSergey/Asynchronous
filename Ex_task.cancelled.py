import sys,time
import asyncio

# Пример кода task.cancelled():

async def main_task():
    print("Корутина main_task запустилась")
    await asyncio.sleep(5)
    print("Корутина main_task завершилась")


async def main():
    task = asyncio.create_task(main_task())
    await asyncio.sleep(1)
    task.cancel()  # Отмена задачи 
    await asyncio.sleep(2)
    if task.cancelled():  # Проверка, была ли задача отменена
        print(f"Задача отменена - {task.cancelled()}")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
