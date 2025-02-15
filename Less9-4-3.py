import sys,time
import asyncio
#pylint: disable-msg=W0603

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

condition = asyncio.Condition()

event_st = asyncio.Event()
event_me = asyncio.Event()
event_cl = asyncio.Event()

storage_stone = 0
storage_metal = 0
storage_cloth = 0

async def gather_stone():
    # Добываем камень, 10ед каждую сек.
    global storage_stone
    async with condition:
        while not event_st.is_set():
            await asyncio.sleep(1)
            storage_stone += 10
            print(f"Добыто 10 ед. камня. На складе {storage_stone} ед.")
            condition.notify_all()
            await condition.wait()

async def gather_metal():
    # Добываем металл, 6ед каждую сек.
    global storage_metal
    while not event_me.is_set():
        await asyncio.sleep(1)
        async with condition:
            storage_metal += 6
            print(f"Добыто 6 ед. металла. На складе {storage_metal} ед.")
            condition.notify_all()
            await condition.wait()

async def gather_cloth():
    # Добываем ткань, 8ед каждую сек.
    global storage_cloth
    while not event_cl.is_set():
        await asyncio.sleep(1)
        async with condition:
            storage_cloth += 8
            print(f"Добыто 8 ед. ткани. На складе {storage_cloth} ед.")
            condition.notify_all()
            await condition.wait()

async def craft_stone_items():
    # Мастерская по крафту из камня
    global storage_stone
    for _item, _required in stone_resources_dict.items():
        async with condition:
            while storage_stone < _required:  # ждем пока накопится нужное кол-во дерева
                await condition.wait()
                condition.notify_all()
            storage_stone -= _required  # изготавливаем предмет
            print(f"Изготовлен {_item} из камня.")
            condition.notify_all()
    event_st.set()

async def craft_metal_items():
    # Мастерская по крафту из мателла
    global storage_metal
    for _item, _required in metal_resources_dict.items():
        async with condition:
            while storage_metal < _required:  # ждем пока накопится нужное кол-во дерева
                await condition.wait()
                condition.notify_all()
            storage_metal -= _required# изготавливаем предмет
            print(f"Изготовлен {_item} из металла.")
            condition.notify_all()
    event_me.set()

async def craft_cloth_items():
    # Мастерская по крафту из ткани
    global storage_cloth
    for _item, _required in cloth_resources_dict.items():
        async with condition:
            while storage_cloth < _required:  # ждем пока накопится нужное кол-во дерева
                await condition.wait()
                condition.notify_all()
            storage_cloth -= _required# изготавливаем предмет
            print(f"Изготовлен {_item} из ткани.")
            condition.notify_all()
    event_cl.set()

async def main():
    # Запускаем производства
    asyncio.create_task(gather_stone())
    asyncio.create_task(gather_metal())
    asyncio.create_task(gather_cloth())
    await asyncio.sleep(1)
    asyncio.create_task(craft_stone_items())
    asyncio.create_task(craft_metal_items())
    asyncio.create_task(craft_cloth_items())

    await event_me.wait()

    # await event_st.wait()
    # await event_cl.wait()


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
