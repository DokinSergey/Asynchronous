import sys,time
import asyncio

async def test_task(i):
    print(f"Задача {i} запущена")
    await asyncio.sleep(i)
    print(f"Задача {i} завершена")


async def main():
    main_task = asyncio.current_task()
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(test_task(i)) for i in range(1, 4)]
            # Даем задачам возможность запуститься
            await asyncio.sleep(0.1)
            # Отмена всех задач
            for task in tasks:
                task.cancel()
            # Переключение контекста, чтобы отмена произошла
            await asyncio.sleep(0)
            # Если задачи отменены, сообщаем об этом
            if all(task.cancelled() for task in tasks):
                print("Все задачи были отменены")
    except asyncio.CancelledError:
        print("Выполнение main() было отменено")
    print('Выполнение main() успешно завершено!')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
