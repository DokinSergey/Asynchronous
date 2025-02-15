import sys,time
import asyncio

async def speech_synt(bot, message):
    print(f'bot {bot} {message}')

# Корутина для демонстрации реакции ботов.
async def robot_reaction(event, bot, message):
    await event.wait()
    await speech_synt(bot, message)

# Корутина проверки id от датчика персонала
async def _event(id, id_sm, event):
    if id == id_sm:
        await asyncio.sleep(2)
        event.set()
    else:
        print('Спокойно, ждем сержанта!')

async def birthday():
    id_sm = 'sms_62933d018e09401bb61c3e823bdb4477'
    id_bots = ["d234", "d235", "d236", "d237", "d238", "d239", "d240", "d241"]
    message = "Повелитель механизмов! Долгих лет! Ты ведешь нас! Слава сержанту! Ура!"
    # Создаем событие
    happy_event = asyncio.Event()
    # Создаем задачи для демонстрации реакции ботов
    bots_tasks = [asyncio.create_task(robot_reaction(happy_event, bot, message)) for bot in id_bots]
    asyncio.gather(*bots_tasks)
    # Подключение корутины _event к датчику в системе контроля экипажа
    # await sensor_id_124(_event, id_sm, happy_event)

    crew_list = ['smh547e3cebb1934a34a43d23bf31a96396', 'smn9c88220fbeaa4c24aa6c8342d437618a',
             'smef64767c46d444c6c89937346c8cc4288', 'sms_62933d018e09401bb61c3e823bdb4477']
    for id in crew_list:
        await _event(id, id_sm, happy_event)
    # print(bots_tasks.append(*[asyncio.create_task( ) ]))
    
    #await asyncio.gather(*bots_tasks)

async def main():
    await birthday()

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
