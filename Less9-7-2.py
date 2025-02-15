import sys,time
import asyncio
#pylint: disable-msg=W0603

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0}

barrier = asyncio.Barrier(5)

async def enter_dungeon(player):
    await asyncio.sleep(players[player])
    print(f"{player} готов войти в подземелье")
    try:
        await asyncio.wait_for(barrier.wait(),5)
        print(f"{player} вошел в подземелье")
    except Exception:
        await barrier.abort()
        print(f"{player} не смог попасть в подземелье. Группа не собрана")

async def main():
    tasks = [asyncio.create_task(enter_dungeon(player)) for player in players]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
