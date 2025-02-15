import sys,time
import asyncio

spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7}

students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]
max_cast_time = 5  # Секунды

async def cast_spell(student, spell, cast_time):
    try:
        await asyncio.sleep(cast_time)
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    except asyncio.CancelledError:
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")

async def main():
    tasks = [asyncio.shield( cast_spell(student, spell, cast_time)) for spell, cast_time in spells.items() for student in students]
    # try:
    await asyncio.wait_for(asyncio.gather(*tasks), max_cast_time)
    # except TimeoutError:
        # pass

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
