import sys,time
import asyncio

# корутина, ожидающая наступление условия
async def waiting_coro(condition, task_id):
    async with condition:
        print(f'Задача {task_id} освобождает блокировку и встает в очередь, ожидая уведомления')
        await condition.wait()
        print(f'Задача {task_id} снова захватывает блокировку и продолжает работу')
        await asyncio.sleep(1)  # Тут любая работа с данными, требующими синхронизации доступа
        print(f'Задача {task_id} завершила работу, блокировка свободна')

# корутина, отправляющая уведомление
async def notifying_coro(condition):
    async with condition:
        await asyncio.sleep(1)
        print('Отправлены уведомления всем ожидающим задачам')
        condition.notify_all()

async def main():
    condition = asyncio.Condition()
    waiting_tasks = [asyncio.create_task(waiting_coro(condition, f'task{i}')) for i in range(1, 4)]
    notifying_task = asyncio.create_task(notifying_coro(condition))
    await asyncio.gather(*waiting_tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
