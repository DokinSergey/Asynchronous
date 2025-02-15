import sys,time
import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]

def callback_code(task):
    print(f'Код: {task.result()}')

async def print_massages(mess):
    await asyncio.sleep(0)
    code = codes[messages.index(mess)]
    odd = int(codes[messages.index(mess)][-1], base=16)%2
    print(code[-1],odd)
    if odd:print(f'Сообщение: {mess}')
    else:  print('Сообщение: Неверный код, сообщение скрыто')
    return code

async def main():
    for mess in messages:
        task = asyncio.create_task(print_massages(mess))
        task.add_done_callback(callback_code)
        await task

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
