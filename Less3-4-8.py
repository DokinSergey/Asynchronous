import sys

import asyncio

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}

async def study_course(student,course, steps, speed):
    print(f"{student} начал проходить курс {course}")
    reading_time = round(steps/speed,2)
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {reading_time} ч.")
    
    #Решение от препода
    # return f"{student} прошел курс {course} за {round(reading_time, 2)} ч."

async def main():
    # Создаем задачи для асинхронного выполнения
    tasks = []
    for key,value in students.items():
        tasks.append(asyncio.create_task(study_course(key,value['course'],value['steps'],value['speed'])))
    await asyncio.gather(*tasks)
    
    #Решение от препода
    # Ожидание завершения каждой задачи индивидуально
    # for task in tasks:
        # print(await task)

asyncio.run(main())

if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
