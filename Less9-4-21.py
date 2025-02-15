import sys,time
import asyncio
#pylint: disable-msg=W0603

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}

storage = 0  # Склад
condition = asyncio.Condition()
crafting_done = asyncio.Event()

res = []
async def gather_wood():
    global storage
    while storage < 35:  # пока не накопится 35 единиц дерева
        await asyncio.sleep(1)  # ждем 1 секунду
        storage += 2  # добываем 2 единицы дерева
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
        async with condition:
            condition.notify_all()  # уведомляем о изменении состояния склада


async def craft_item():
    global storage
    for item, wood_required in wood_resources_dict.items():
        async with condition:
            while storage < wood_required:  # ждем пока накопится нужное кол-во дерева
                await condition.wait()
            storage -= wood_required  # изготавливаем предмет
            print(f"Изготовлен {item}.")

    crafting_done.set()  # Устанавливаем событие, чтобы сигнализировать о завершении


async def main():
    gather_task = asyncio.create_task(gather_wood())
    craft_task = asyncio.create_task(craft_item())

    await crafting_done.wait()  # Ждем завершения всех задач #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
