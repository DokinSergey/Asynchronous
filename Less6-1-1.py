import sys,time
import asyncio
# import itertools
import random
# Пользователи:
users = ['user1', 'user2', 'user3']
# Продукты:
products = ['iPhone 14', 'Samsung Galaxy S23', 'MacBook Pro', 'Dell XPS 13', 'Sony WH-1000XM5', 'Apple Watch Series 8',
    'Kindle Paperwhite', 'GoPro Hero 11', 'Nintendo Switch', 'Oculus Quest 2']
# Типы действий:
actions = ['просмотр', 'покупка', 'добавление в избранное']

# Асинхронный генератор
async def user_action_generator():
    # iterlist = list(itertools.product(users, actions, products))
    # il = random.choice(iterlist)
    while True:
        await asyncio.sleep(.1)
        yield {'user_id':random.choice(users), 'action':random.choice(actions), 'product_id':random.choice(products)}

async def main():
    async for li in user_action_generator():  # Используем асинхронный цикл for для итерации
        print(li)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
