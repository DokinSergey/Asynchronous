import sys,time
import asyncio
import random
# Не менять!
random.seed(0)

async def fetch_weather(source, city):
    await asyncio.sleep(random.randint(1,5))
    return f"Данные о погоде получены из источника {source} для города {city}: {random.randint(-10,35)}°C"

async def main():
    city = "Москва"
    sources = [
        'http://api.weatherapi.com',
        'http://api.openweathermap.org',
        'http://api.weatherstack.com',
        'http://api.weatherbit.io',
        'http://api.meteostat.net',
        'http://api.climacell.co'
    ]
    tasks = [asyncio.create_task(fetch_weather(source, city)) for source in sources]
    done,_ = await asyncio.wait(tasks, return_when = asyncio.FIRST_COMPLETED)
    print(done.pop().result())


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
