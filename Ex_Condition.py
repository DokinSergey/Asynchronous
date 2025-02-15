import sys,time
import asyncio

async def worker(condition, msg):
    # Захватываем блокировку 
    async with condition:
        print(f"worker() получил блокировку, сообщение {msg}")
        await condition.wait() # тут блокировка снимается на время ожидания корутины
        print('В worker() сработал await condition.wait() и она продолжает выполнять любую логику')
        print(f"worker() разблокирована, сообщение {msg}")

async def main():
    # Создаем условие
    condition = asyncio.Condition()
    task1 = asyncio.create_task(worker(condition, 'task1'))
    task2 = asyncio.create_task(worker(condition, 'task2'))
    await asyncio.sleep(1)
    # Захватываем блокировку
    async with condition:
        print("Корутина main получила блокировку")
        print("Корутина main реализует любую логику приложения")
        condition.notify_all()

        print('main() оповещает все корутины с помощью -  condition.notify_all(), и передаёт управление в цикл событий')
        print("Корутина main разблокирована")

    await task1
    await task2

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
