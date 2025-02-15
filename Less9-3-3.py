import sys,time
import asyncio
import random

error = None
count = 0
sek = 0

random.seed(0)

async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek
    try:
        # Допишите сюда цикл
        while interrupt_flag:
            if (error := random.choices([True, False], weights=[25, 75])[0]):break
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            count +=1
            sek += 1
            await asyncio.sleep(1)
    finally:
        # Поместите сообщение о завершении мониторинга
        print("Завершение мониторинга ракетных запусков")

async def main():
    # global error
    # global count
    # global sek
    # Создайте Task задачу
    interrupt_flag = asyncio.Event()
    asyncio.create_task(monitor_rocket_launches(interrupt_flag))
    # Допишите сюда цикл
    while count < 50:
        if error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print("Отмена мониторинга ракетных запусков...")
            break
        await asyncio.sleep(5)
        print(f"Время ожидания составило {sek} секунд. За это время ошибки не произошло")
    else:
        interrupt_flag.set()
    # Запустите созданную корутину в пункте 2 через await
    # await tack_monitor


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
