import sys,time
import asyncio

files = ['image.png', 'file.csv', 'file1.txt', 'file3.csv', 'file4.csv', 'file5.csv']
missed_files = ['file3.csv', 'file4.csv', 'file5.csv']

# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    await asyncio.sleep(1)
    return f'Файл {file_name} успешно скачан'

# ваш код пишите тут:
async def main():
    try:
        async with asyncio.TaskGroup() as taskgroup:
            [taskgroup.create_task(download_file(file_name)) for file_name in files]
            await asyncio.sleep(0.1)
    except* Exception as e:
        for error in e.exceptions:
            print(error)


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
