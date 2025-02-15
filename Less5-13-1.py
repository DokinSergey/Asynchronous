import sys,time
import asyncio

delivery_times = {
    'Москва': 1,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 4,
    'Челябинск': 6,
    'Омск': 7,
    'Красноярск': 8,
    'Владивосток': 9,
    'Хабаровск': 9
}

# Заказы:
# orders = [(подарок, город, пометка), ...]
orders = [('Новогодняя кружка', 'Москва', 'нет'),('Шоколадный набор', 'Красноярск', 'нет'),('Ручка и блокнот', 'Новосибирск', 'важно'),
    ('Носки с новогодним принтом', 'Владивосток', 'нет'),('Плед', 'Омск', 'нет'),]

# Время до нового года:
days_left = 7

# Тут пишите ваш код:
async def deliver(order):
    item,city,_ = order
    await asyncio.sleep(delivery_times[city])
    print(f'Подарок {item} успешно доставлен в г. {city}')

async def main():
    tasks = []
    for order in orders:
        if order[2] == 'важно':
            tasks.append(asyncio.shield(deliver(order)))
        else:
            tasks.append(asyncio.create_task(deliver(order)))
    #---------------------------------------------------------
    _,pending = await asyncio.wait(tasks,timeout=days_left)
    [future.cancel() for future in pending]
    while len(asyncio.all_tasks()) - 1:
        print(f'{len(asyncio.all_tasks())}')
        await asyncio.sleep(1)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
