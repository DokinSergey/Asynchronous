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
    # try:
    await asyncio.sleep(cast_time)
    return f"{student} успешно кастует {spell} за {cast_time} сек."
    # except asyncio.CancelledError:
        # return f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield."

async def main():
    tasks = [asyncio.create_task(cast_spell(student, spell, cast_time)) for spell, cast_time in spells.items() for student in students]
    try:
        t = await asyncio.wait_for(asyncio.gather(*[asyncio.shield(task) for task in tasks]), max_cast_time)
        # done, pending = await asyncio.wait(asyncio.shield(asyncio.gather(*tasks, return_exceptions=False)),timeout = max_cast_time), return_exceptions=False
    except TimeoutError as asr:
        pass
        # await asyncio.sleep(7)
        # print(f'1:{t.result()}')
    except TimeoutError as asr:
        print(f'21:{asr}')
    except asyncio.CancelledError as bsr:
        print(f'22:{bsr}')
    # except Exception as merr:
        # print(f'23:{merr}')
    try:
        for Task in tasks:
            print(Task.cancelled(),Task.done())
            if Task.done():
                print(Task.result())
            else:
                await asyncio.sleep(3)
                # # res = await Task
                print(f'!!!{Task.done()}')
    except TimeoutError as asr:
        print(f'21:{asr}')
    except asyncio.CancelledError as bsr:
        print(f'22:{bsr}')
    # except Exception as merr:
        # print(f'23:{merr}')
    # await asyncio.sleep(7)

    # for Task in tasks:
        # if Task.cancelled():
            # await asyncio.sleep(7)
            # res = await Task
            # print(f'!!!{res}')
        # else:
            # print(f'{Task.cancelled()} : {Task.result()}')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
