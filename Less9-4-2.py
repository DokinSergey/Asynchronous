import sys,time
import asyncio
#pylint: disable-msg=W0603

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,}

storage = 0

async def gather_wood(event,condition):
    # Код по добыче 2 единиц древесины в секунду
    global storage
    while event:
        await asyncio.sleep(0.1)
        async with condition:
            # await condition.wait()
            storage +=2
            print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
            condition.notify_all()
    print('Заввершили добычу')

async def craft_item(condition,item,qtty):
    global storage
    # Код по изготовлению деревянных предметов
    async with condition:
        # print(f'Start {item}')
        while storage < qtty:
            await condition.wait()
        await asyncio.sleep(0)
        storage -= qtty
        print(f"Изготовлен {item}.")
    # print(f'Stop {item}')

async def main():
    event = asyncio.Event()
    event.set()
    condition = asyncio.Condition()
    asyncio.create_task(gather_wood(event,condition))
    tasks = [asyncio.create_task(craft_item(condition,item,qtty)) for item,qtty in wood_resources_dict.items()]
    await asyncio.gather(*tasks)
    
    # async with condition:
        # await asyncio.sleep(0.1)
        # condition.notify_all()


    # await asyncio.sleep(1)
    # # condition.notify()
    # task = asyncio.create_task(gather_wood(event,condition))
    # await asyncio.gather(*tasks)
    # event.clear()
    print(event.is_set(), condition.locked())

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
