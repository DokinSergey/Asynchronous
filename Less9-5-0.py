import sys,time
import asyncio
from random import random
#pylint: disable-msg=W0603

semaphore = asyncio.Semaphore(3) # Создаем семафор

async def write_to_file(text):
    async with semaphore:  # Используем семафор для ограничения доступа к файлу
        with open("file.txt", "a") as file:
            file.write(text)

async def main():
    # Создаем список задач
    tasks = [write_to_file("строка 1\n"), write_to_file("строка 2\n"), write_to_file("строка 3\n")]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
