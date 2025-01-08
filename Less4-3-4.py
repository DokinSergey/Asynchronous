import sys,time

import asyncio

async def process_request(request_name, stages, status):
    for stage_name in stages:
        time.sleep(1)  # Симулируем время выполнения этапа
        status[request_name] = stage_name
        await  asyncio.sleep(0)


async def update_status(request_name, status):
    while True:
        print(status)
        if status == {request_name: 'Отправка уведомлений'}:
            break
        await asyncio.sleep(0)


async def main():
    # Исходные данные по запросу и этапам его обработки
    request_name = 'Запрос 1'
    stages = ["Загрузка данных", "Проверка данных", "Анализ данных", "Сохранение результатов", "Отправка уведомлений"]

    status = {request_name: None}

    # Создание задач для каждой корутины
    process_task = asyncio.create_task(process_request(request_name, stages, status))
    updater_task = asyncio.create_task(update_status(request_name, status))

    await asyncio.gather(process_task, updater_task)


start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'Общее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
