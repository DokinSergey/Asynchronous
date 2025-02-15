import asyncio

async def my_coroutine(num):
    print(f'Начинаем выполнение корутины {num}')
    
    await asyncio.sleep(1)
    
    current_task = asyncio.current_task()
    
    asyncio.current_task().set_name(url)
    
    task.add_done_callback(callback)

async def main():
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(1, 6)]
    
    done,pending  = await asyncio.wait(tasks,return_when=asyncio.ALL_COMPLETED)
    
    await asyncio.gather(*tasks)
    
    shield_obj = asyncio.shield(my_coroutine())
    
    [future.cancel() for future in pending]
    
    if random.choice((True, False):#вероятность 50%
        pass
        
    {k: await vfun() async for k, vfun in funcs_dict.items() if await conditionfun(k)}
    
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание трех задач
        [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]

    # Ожидание, пока все задачи не будут завершены...
    print('Все задачи были выполнены!')
    
    #Чтение асинхронное чтение json файла
    async with aiofiles.open(FileName, mode='r', encoding = 'utf_8') as fn:
        context = await fn.read()
        templates = json.loads(context)

    random.choices([True, None], weights=[25, 75])[0]

    await asyncio.gather(*tasks)
# print(f'Тип защитного объекта shield: {type(shield_obj).__name__}') # Future
asyncio.run(main())
