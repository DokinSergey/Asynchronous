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
    await asyncio.sleep(cast_time)
    return (student,spell,cast_time)

async def main():
    tasks = [asyncio.create_task(cast_spell(student, spell, cast_time)) for spell, cast_time in spells.items() for student in students]
    try:
        await asyncio.wait_for(asyncio.gather(*[asyncio.shield(task) for task in tasks]), max_cast_time)
    except TimeoutError:
        pass

    TaskNotDone = []
    for Task in tasks:
        if Task.done():
            res = Task.result()
            print(f"{res[0]} успешно кастует {res[1]} за {res[2]} сек.")
        else:TaskNotDone.append(Task)

    await asyncio.sleep(2)

    for Task in TaskNotDone:
        res = Task.result()
        print(f"Ученик {res[0]} не справился с заклинанием {res[1]}, и учитель применил щит. {res[0]} успешно завершает заклинание с помощью shield.")


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
