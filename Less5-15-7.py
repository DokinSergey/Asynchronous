import sys,time
import asyncio

banned_words = ["bug", "error", "exception", "fail", "crash", "hang", "slow", "memory leak", "infinite loop","deadlock"]
messages = [
{"message_id": 45677,"message": "Я думаю, мы должны рассмотреть новый алгоритм для этого задания.","role": "moderator"},
{"message_id": 66994,"message": "У нас есть ошибка в последнем коммите.","role": "moderator"},
{"message_id": 61982,"message": "Мне кажется, мы можем оптимизировать использование памяти.","role": "black_list_user"},
{"message_id": 24766,"message": "У нас проблемы с базой данных на продакшн сервере.","role": "None"},
{"message_id": 78228,"message": "Стоит ли рассмотреть отладку этого кода сейчас, убрав deadlock ?","role": "moderator"},
{"message_id": 59949,"message": "Проблема с процессором на сервере B.","role": "moderator"},
{"message_id": 15427,"message": "Баг был найден в последней версии кода.","role": "admin"},
{"message_id": 71942,"message": "Я сейчас занимаюсь компиляцией новой версии.","role": "None"},
{"message_id": 69061,"message": "Интерфейс этой системы довольно сложен для новичков.","role": "black_list_user"},
{"message_id": 15224,"message": "Не могу понять,hang в какой функции появляется этот bug.","role": "moderator"},
{"message_id": 33910,"message": "Твой код работает исключительно быстро.","role": "black_list_user"},
{"message_id": 50394,"message": "Я нашел пару отличных статей о машинном обучении.","role": "student"},
{"message_id": 64023,"message": "Ты пользуешься Git для управления версиями?","role": "None"},
{"message_id": 27769,"message": "Мы сможем справиться с этим проектом в срок, иначе fail.","role": "moderator"},
{"message_id": 20857,"message": "Расскажи мне о своем опыте использования Python.","role": "student"},
{"message_id": 85640,"message": "Какой твой любимый язык программирования?","role": "admin"},
{"message_id": 63481,"message": "Я работал с Java до этого проекта.","role": "admin"},
{"message_id": 46548,"message": "Мы можем встретиться завтра, чтобы обсудить этот код.","role": "student"},
{"message_id": 47734,"message": "Стоит ли использовать TensorFlow для этого проекта?","role": "None"},
{"message_id": 66161,"message": "Можешь проверить мой код перед коммитом?","role": "student"},
{"message_id": 18595,"message": "Очень сложно находить ошибки в коде без должной документации.","role": "moderator"},
]

async def check_message(_message):
    role = asyncio.current_task().get_name()
    await asyncio.sleep(0)
    if   role == "admin":mess = _message
    elif role == 'black_list_user':mess = "Пользователь забанен, сообщение скрыто"
    elif not role or role == 'None':mess = "ERROR_USER_NONE"
    else:
        mess = _message
        for bword in banned_words:
            if bword in _message:
                if role == 'moderator':mess = mess.replace(bword,'****')
                elif role == 'student':
                    mess = "В сообщении есть запрещённое слово, сообщение скрыто"
                    break
    print(f'{role}: {mess}')

async def main():
    # try:
    tasks = [asyncio.create_task(check_message(mess["message"]), name=mess["role"]) for mess in messages]
    await asyncio.gather(*tasks)
    # for task in tasks:
        # res = task.result()
        # print(res)

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
