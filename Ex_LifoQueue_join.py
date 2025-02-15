import sys,time
# from random import random
import asyncio

async def worker(name, lifo_queue):
    while True:
        task = await lifo_queue.get()                       # Получаем задание из очереди
        print(f"Рабочий_{name}. Получил задачу: {task}")
        await asyncio.sleep(0.5)                            # Обрабатываем задание
        lifo_queue.task_done()                              # Отправляем сигнал, что задание выполнено

async def main():
    lifo_queue = asyncio.LifoQueue()                        # Создаем очередь
    for i in range(10):
        await lifo_queue.put(i)                             # Заполняем очередь заданиями
    
    # Создаем несколько задач-рабочих
    workers = [asyncio.create_task(worker(f"{i}", lifo_queue)) for i in range(3)]
    await lifo_queue.join()                                 # Ждем, пока все задания не будут выполнены
    for w in workers:                                       # Останавливаем задачи-рабочие
        w.cancel()

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
