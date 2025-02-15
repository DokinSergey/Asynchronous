import sys,time
import asyncio
import random
#Пример кода с несколькими задачами и проверкой их результата

async def task_func(task_id):
    print(f"Старт задачи {task_id}, из корутины task_func")
    await asyncio.sleep(random.uniform(0, 2))
    print(f"Задача {task_id} выполнена в корутине task_func")


async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(task_func(i))
        tasks.append(task)
    print("Все задачи созданы")

    # Цикл, который выполняется, пока есть активные задачи
    while len(tasks) > 0:

        # Ожидание завершения задач
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        # Цикл для вывода сообщения о завершении каждой задачи
        for task in done:
            print(f"Задача выполнена- {task.get_name()} и имеет флаг- {task.done()}")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
