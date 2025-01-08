import sys
import asyncio

# Пример данных
log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0}
    ]

async def fetch_log(event):

    await asyncio.sleep(event["delay"])
    return f"Событие: '{event["event"]}' обработано с задержкой {event["delay"]} сек."

async def main():

    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


asyncio.run(main())

if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
