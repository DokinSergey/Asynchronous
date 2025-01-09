import sys,time
import asyncio

async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        await asyncio.sleep(0.1)
        print(f"[{task_name}] Статус проверки: {status}")
        if 'Катастрофически' in status:
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")

async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        await asyncio.sleep(0.1)
        print(f"[{task_name}] Статус проверки: {status}")
        if 'Катастрофически' in status:
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")

async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        await asyncio.sleep(0.1)
        print(f"[{task_name}] Статус проверки: {status}")
        if 'Катастрофически' in status:
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")

async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически",
        ]
    task_cpu = asyncio.create_task(monitor_cpu(status_list), name="CPU")
    task_ram = asyncio.create_task(monitor_memory(status_list), name="Память")
    task_hdd = asyncio.create_task(monitor_disk_space(status_list), name="Дисковое пространство")
    await asyncio.gather(task_cpu,task_ram,task_hdd)

start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
