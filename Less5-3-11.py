import sys,time
import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}

async def download_file(file_name,size,speed):
    load_time = round(size/speed, 3) if speed else 0
    print(f'Начинается загрузка файла: {file_name}, его размер {size} мб, время загрузки составит {load_time} сек')
    await asyncio.sleep(load_time)
    print(f'Загрузка завершена: {file_name}')

async def monitor_tasks(tasks):
    while not all(task.done() for task in tasks):
        await asyncio.sleep(1)  # Проверяем статус задач каждую секунду
        for task in tasks:
            print(f"Задача {task.get_name()}: {'завершена' if task.done() else 'в процессе'}, Статус задачи {task.done()}")
    print("Все файлы успешно загружены")


async def main():
    network_speed = 8  # Скорость сети в мегабайтах в секунду
    tasks = [asyncio.create_task(download_file(name, size, network_speed), name=name) for name, size in files.items()]
    await monitor_tasks(tasks)  # Мониторинг статуса задач


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
