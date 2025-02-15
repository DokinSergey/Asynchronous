import sys,time
import asyncio

async def send_message(message):
    print(f"Отправка сообщения: {message}")
    await asyncio.sleep(1)  # Имитация задержки отправки сообщения
    print(f"Сообщение отправлено: {message}")

async def receive_message():
    await asyncio.sleep(2)  # Имитация задержки получения сообщения
    message = "И тебе привет!"
    print(f"Сообщение получено: {message}")
    return message


async def main():
    send_task = asyncio.create_task(send_message("Привет"))
    receive_task = asyncio.create_task(receive_message())
    await asyncio.gather(send_task, receive_task)
    event_loop = asyncio.get_running_loop()
    print(f'Цикл событий активен: {event_loop.is_running()}')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
asyncio.run(main())

start_time = time.perf_counter()
# asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
