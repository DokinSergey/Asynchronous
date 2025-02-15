import sys,time
import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]

async def download_data(report):
    try:
        if report["name"] == "Дмитрий Орлов":
            await cancel_task(asyncio.current_task())
            # await asyncio.sleep(0.1)
            # print(f"Загрузка отчета {report["report"]} для пользователя {report["name"]} остановлена. Введите новые данные")
        await asyncio.sleep(report["load_time"])
        print(f"Отчет: {report["report"]} для пользователя {report["name"]} готов")
    except asyncio.CancelledError as err:
        # print(f'+{err}+')
        print(f"Загрузка отчета {report["report"]} для пользователя {report["name"]} остановлена. Введите новые данные")

async def cancel_task(task):
    task.cancel()
    await asyncio.sleep(0.1)

async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]
    await asyncio.gather(*tasks)


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
