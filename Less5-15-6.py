import sys,time
import asyncio

banned_words = ['ошибка', 'баг', 'отладка', 'память', 'процессор', 'компиляция', 'алгоритм', 'функция', 'база данных', 'интерфейс']
message = [
    {"message_id": 45677,"message": "Я думаю, мы должны рассмотреть новый алгоритм для этого задания."},
    {"message_id": 66994,"message": "У нас есть ошибка в последнем коммите."},
    {"message_id": 61982,"message": "Мне кажется, мы можем оптимизировать использование памяти."},
    {"message_id": 24766,"message": "У нас проблемы с базой данных на продакшн сервере."},]

async def check_message(_message):
    # print(_message["message"].lower().strip('.,'))
    # wordlist = [word.lower() for word in _message["message"].split()]
    try:
        if any(stop.lower() in _message["message"].lower().strip('.,') for stop in banned_words):
            cur_task = asyncio.current_task()
            cur_task.cancel()
            await asyncio.sleep(0)
            
            # raise asyncio.CancelledError(_message["message_id"])
            # return _message["message_id"]
    except asyncio.CancelledError:
        # print(f'В сообщении {_message["message_id"]} стоп-слово:')
        return f'В сообщении {_message["message_id"]} стоп-слово: task.done(): {cur_task.done()}'
    else:
        # print(f'{_message["message_id"]}: {_message["message"]}')
        return(f'{_message["message_id"]}: {_message["message"]}')

async def main():
    # try:
    tasks = [asyncio.create_task(check_message(mess)) for mess in message]
    await asyncio.gather(*tasks, return_exceptions=True)
    for task in tasks:
        res = task.result()
        # print(task.done())
        print(res)
        # if len(res) > 1 and res[1]:
            # print(f'Всего найдено открытых портов {len(res[1])} {res[1]} для ip: {res[0]}')
    # except asyncio.CancelledError as ErrMess:
        # print(f'В сообщении {ErrMess} стоп-слово: ')
    # except Exception as ErrMess:
        # print(f'Error {ErrMess} ')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
