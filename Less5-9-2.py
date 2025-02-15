import sys,time
import asyncio

data = [
    {'Name': 'Company1', 'Address': '9974 Lloyd Radial Suite 005, Andrewfort, PW 45078', 'Phone': '829-338-4124x62279',
     'Email': 'yhiggins@bishop-gentry.com', 'Website': 'https://www.griffith-diaz.org/', 'Year': 1981,
     'Employees': 2935, 'Description': 'Advanced eco-centric secured line', 'CEO': 'Amanda Hall', 'TaxID': 8627654889,
     'call_time': 5},
    {'Name': 'Company2', 'Address': '7703 Craig Spurs Suite 391, Acostafurt, MT 24156', 'Phone': '225-321-1903',
     'Email': 'amandathomas@jones.biz', 'Website': 'http://www.adkins.org/', 'Year': 2008, 'Employees': 2593,
     'Description': 'Sharable next generation hardware', 'CEO': 'Jacob Dunlap', 'TaxID': 2307021392, 'call_time': 2},
    {'Name': 'Company25', 'Address': '24106 Robinson Walks, Gibsonhaven, TX 66568', 'Phone': '(947)767-2860x856',
     'Email': 'ericpratt@parker.info', 'Website': 'https://rubio-webb.com/', 'Year': 2015, 'Employees': 6385,
     'Description': 'Reduced foreground workforce', 'CEO': 'Erin Lowe', 'TaxID': 3626826838, 'call_time': 11}
     ]

async def call_company(Company:dict[str,str]):
    _task = asyncio.current_task()
    try:
        await asyncio.sleep(Company['call_time'])
    except asyncio.CancelledError:
        print('CancelledError')
        # raise
    # await asyncio.sleep(5)
    # _task.cancel()
    else:
        print(f'Company {Company['Name']}: {Company['Phone']} дозвон успешен')

async def main():
    tasks = [asyncio.create_task(call_company(Company)) for Company in data]
    await asyncio.sleep(5.01)
    [task.cancel() for task in tasks]
    # try:
        # await asyncio.gather(*tasks)
    asyncio.wait_for(tasks,10)
    # except BaseException as BExErr:
        # print(f'0:{BExErr}')

        # except asyncio.CancelledError() as Cerr:
        # print(f'CancelledError:{Cerr}')
    # await asyncio.sleep(1)
    # task.cancel()  # Отмена задачи (запрос на отмену выполнения корутины main_task())

    # try:
        # await task
    # except asyncio.CancelledError:
        # print("Задача отменена")

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
