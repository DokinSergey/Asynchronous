import sys

import asyncio

async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    # Создаем задачи для асинхронного выполнения
    task1 = asyncio.create_task(read_book('Алекс',5))
    task2 = asyncio.create_task(read_book('Мария',3))
    task3 = asyncio.create_task(read_book('Иван',4))
    await asyncio.gather(task1,task2,task3)



# async def waiter(future):
    # await future
    # print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")

# async def setter(future):
    # await asyncio.sleep(random.randint(1,3))
    # future.set_result(True)

asyncio.run(main())

if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
