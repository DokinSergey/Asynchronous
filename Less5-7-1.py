import sys,time
import asyncio
order = {'Диван': 5, 'Обеденный_стол': 3, 'Табуретка': 50, 'Гардероб': 1}
warehouse_store = {'Диван': 10, 'Обеденный_стол': 10, 'Табуретка': 45, 'Гардероб': 0}

async def check_store(item, quantity):
    if not (qtt := warehouse_store.get(item,0)):
        asyncio.current_task().set_name(f"Отсутствует: {item}")
    elif qtt < quantity:asyncio.current_task().set_name(f"Частично в наличии: {item}")
    else:asyncio.current_task().set_name(f"В наличии: {item}")


# ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(check_store(item, quantity)) for item, quantity in order.items()]
    # await asyncio.gather(*tasks)
    done,_ = await asyncio.wait(tasks,return_when=asyncio.ALL_COMPLETED)
    rtasks = [_i.get_name() for _i in done]
    rtasks.sort()
    print(rtasks)
    for task in rtasks:
        print(task)


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
