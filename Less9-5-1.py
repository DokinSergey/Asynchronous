import sys,time
import asyncio
#pylint: disable-msg=W0603
users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]

sem = asyncio.Semaphore(3) # Создаем семафор

qr = 0

async def server_query(username):
    global qr
    async with sem:  # Используем семафор для ограничения доступа к файлу
        print(f'Пользователь {username} делает запрос')
        qr += 1
        await asyncio.sleep(0.1)
        print(f'Запрос от пользователя {username} завершен')
        print(f'Всего запросов: {qr}')

async def main():
    # Создаем список задач
    tasks = [asyncio.create_task(server_query(user)) for user in users]
    await asyncio.gather(*tasks)

    print(qr)
start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
