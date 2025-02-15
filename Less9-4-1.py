import sys,time
import asyncio

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']

async def User_access_DB(condition, UserName):
    async with condition:
        print(f'Пользователь {UserName} ожидает доступа к базе данных')
        await condition.wait()
        print(f'Пользователь {UserName} подключился к БД')
        await asyncio.sleep(0.1)
        print(f'Пользователь {UserName} отключается от БД')

async def main():
    condition = asyncio.Condition()
    tasks = [asyncio.create_task(User_access_DB(condition, UserName)) for UserName in users]
    # await asyncio.gather(*tasks)
    await asyncio.sleep(1)
    # condition.notify()
    async with condition:
        condition.notify_all()
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
