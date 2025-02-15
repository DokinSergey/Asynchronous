import sys,time
import asyncio

# Пример кода task.cancelling():

async def long_running_task():
    try:
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        # Обработка отмены задачи и вывод сообщения при перехвате asyncio.CancelledError
        print("Получена команда на отмену задачи task")
        # Подъем перехваченного ранее исключения, для срабатывания логики в main().
        raise

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(.5)
    # Отменяем задачу
    task.cancel()

    # Используем cancelling() для проверки, была ли задача помечена для отмены
    if task.cancelling() > 0:
        print("Дана команда отмены задачи task")
    else:
        print("Задача task не ожидает отмены")
    # Перехват исключения asyncio.CancelledError в main()
    try:
        await task
    except asyncio.CancelledError:
        print(f"Задача task отменена: {task.cancelled()}")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
