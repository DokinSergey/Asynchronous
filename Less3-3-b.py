import sys
import asyncio

# Список поваров.
chef_list = ['', 'Франсуа', 'Жан', 'Марсель']


async def cook_order(order_number, dish):
    # Повар готовит блюдо
    print(f"Повар {chef_list[order_number]} начинает готовить заказ №{order_number}: {dish}")
    await asyncio.sleep(2)  # Имитация времени на готовку
    print(f"Заказ №{order_number}: {dish} готов!")
    return f"{dish} для заказа №{order_number}"


async def serve_order(order_number, dish):
    # Официант подает блюдо
    await cook_order(order_number, dish)
    print(f"Официант подает {dish}")


async def manager():
    # Менеджер (событийный цикл) назначает задачи
    orders = [(1, 'Салат'), (2, 'Стейк'), (3, 'Суп')]
    tasks = [asyncio.create_task(serve_order(order_number, dish)) for order_number, dish in orders]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)

# Запуск событийного цикла
asyncio.run(manager())
'''
Функция cook_order() аналогична работе повара, который готовит блюдо. Эта функция использует await asyncio.sleep(2),
 чтобы имитировать время, затрачиваемое на приготовление блюда.

Функция serve_order() соответствует действиям официанта, который получает заказ, передает его повару (cook_order()),
 ожидает, пока блюдо не приготовится и подает его.

Функция manager() играет роль менеджера ресторана, который назначает задачи официанту и использует asyncio.create_task()
 для их планирования. Создание задач позволяет официанту (serve_order) раздать задания каждому повару (cook_order).

Используя asyncio.gather(), менеджер отдает команду получить все заказы официанту и в итоге дождаться завершения всех задач,
 т.е., задачи официанта будут завершены только после того, как все блюда будут готовы и поданы. 
'''

if len(sys.argv)>1 and sys.argv[1] == 'cons':
    input(':-> ')
    sys.exit(0)
else:
    input(':-> ')
    os._exit(0)