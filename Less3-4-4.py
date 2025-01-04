import sys

import asyncio

async def async_operation():
    
    try:
        print("Начало асинхронной операции.")
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise
    else:
        print("Асинхронная операция успешно завершилась.")

async def main():
    print("Главная корутина запущена.")
    try:
        task = asyncio.create_task(async_operation())
        
        await asyncio.sleep(0.1)
        print("Попытка отмены Task.")

        task.cancel()

        await task

        result = task.result()
        print("Результат Task:", result)
    except asyncio.CancelledError:
        print("Обработка исключения: Task был отменен.")

    if task.cancelled():
        print("Проверка: Task был отменен.")
    else:
        print("Проверка: Task не был отменен.")
    print("Главная корутина завершена.")

asyncio.run(main())

if not(len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
