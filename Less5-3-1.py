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
    for task in tasks:
        status = 'завершена' if task.done() else 'в процессе'
        print(f'Задача {task.get_name()}: {status}, Статус задачи {task.done()}')

async def main():
    pending = tasks = [asyncio.create_task(download_file(file_name,size,8), name=file_name) for file_name,size in files.items()]
    tm = 0.1
    while len(pending) > 0:
        _, pending = await asyncio.wait(pending, timeout = tm, return_when=asyncio.ALL_COMPLETED)#FIRST_COMPLETED)
        await monitor_tasks(tasks)
        tm = 1.0
    print('Все файлы успешно загружены')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
