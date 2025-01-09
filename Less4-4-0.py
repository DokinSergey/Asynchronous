import sys,time

import asyncio

async def my_coroutine():
    # Получаем имя текущей задачи.
    task = asyncio.current_task()
    task_name = task.get_name()

    print(f'Задача {task_name} запущена.')
    await asyncio.sleep(1)
    print(f'Задача {task_name} была выполнена.')


async def main():
    task = asyncio.create_task(my_coroutine(), name='my_task')
    print(f"Задача {task.get_name()} создана, но еще не запущена")
    await task
    print('Ожидание выполнения my_task окончено, управление было возвращено в main().\nmain() завершает свою работу.')


start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'Общее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
