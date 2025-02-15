import sys,time
import asyncio

async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception('Нет данных...')
    return {'data': data}


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(get_data(1))
            task2 = tg.create_task(get_data(2))
            task3 = tg.create_task(get_data(0))
            task4 = tg.create_task(file_reader('fake.png'))
            task5 = tg.create_task(file_reader('new_fake.png'))
            task6 = tg.create_task(get_data(0))
        # Результат мы все равно не увидим, так как спровоцируем вызов исключений.
        result = [task1.result(), task2.result(), task3.result(), task4.result(), task5.result(), task6.result()]
        print('Готово!!!', result)
    # Добавляем обработчики, которые будут группировать ошибки одного типа.
    except* FileNotFoundError as e:
        for error in e.exceptions:
            print(error)
    except* Exception as e:
        for error in e.exceptions:
            print(error)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
