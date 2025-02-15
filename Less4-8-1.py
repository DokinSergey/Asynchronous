import sys,time
import asyncio

dishes = {
    'Куриный суп': 118, 
    'Бефстроганов': 13, 
    'Рататуй': 49, 
    'Лазанья': 108, 
    'Паэлья': 51, 
    'Утка по-пекински': 41,}

async def cook_dish(name, duration):
    print(f"Приготовление {name} начато.")
    await asyncio.sleep(duration/10)
    print(f"Приготовление {name} завершено. за {duration/10}")

async def main():
    tasks = [asyncio.create_task(cook_dish(dish, delay),name = dish) for dish,delay in dishes.items()]
    done,pending = await asyncio.wait(tasks,timeout=10, return_when=asyncio.ALL_COMPLETED)
    for task in pending:
        print(f"{task.get_name()} не успел(а,о) приготовиться и будет отменено.")
        task.cancel()


    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
