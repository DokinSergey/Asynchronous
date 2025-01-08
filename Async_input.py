import asyncio
import signal

def shutdown():
    # Отменяем все задачи, кроме вызвавшей
    for task in asyncio.Task.all_tasks():
        if task is not asyncio.tasks.Task.current_task():
            task.cancel()


async def user_io():
    loop = asyncio.get_event_loop()
    # Ждём действия от пользователя
    while True:
        # Запускаем input() в отдельном потоке и ждём его завершения
        command = await loop.run_in_executor(None, input, 'Для выхода введите C:\n')
        if command.lower() == 'c':
            shutdown() # Отменяем все задачи
            break      # и выходим из цикла


# Сопрограмма, выполняемая параллельно с ожиданием пользовательского ввода
async def task_manager():
    counter = 0
    while True:
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            break # Выходим из цикла, если задачу отменили
        counter += 1
        print("I'm a task manager {}!".format(counter))


if __name__ == '__main__':
    # Устанавливаем обработчик Ctrl+C
    signal.signal(signal.SIGINT, lambda n, f: shutdown())

    # Запускаем цикл событий
    loop = asyncio.get_event_loop()
    # Задача ждущая завершения сопрограм user_io и task_manager
    main_task = asyncio.wait([user_io(), task_manager()])
    try:
        loop.run_until_complete(main_task)
    except asyncio.CancelledError:
        # Позволяем main_task завершиться
        loop.run_until_complete(main_task)
    loop.close()
