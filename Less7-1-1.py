import sys,time
import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 3,  
    "Война и мир": 2,
    "Преступление и наказание": 1,}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
}

async def reserve_book(book):
    global library_catalog
    if library_catalog[book] > 0:
        await asyncio.sleep(1)
        library_catalog[book] -= 1
        print("Книга успешно зарезервирована.")
    else:print("Книга отсутствует. Резервирование отменено.")

async def main():
    tasks = [asyncio.create_task(reserve_book(book)) for _,book in reservation_tasks.items()]
    await asyncio.gather(*tasks)
    for book,qtty in library_catalog.items():
        print(f'{book}: {qtty}')


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
