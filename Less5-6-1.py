import sys,time
import asyncio
url_list = ['https://example.com','http://stepik.org','ftp://python-org','invalid-url']

async def check_url(url):
    if url[:4] != 'http':
        return None
    await asyncio.sleep(2)
    return 'Ok'

# ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(check_url(url)) for url in url_list]
    await asyncio.wait(tasks,timeout=1,return_when=asyncio.ALL_COMPLETED)
    # rtasks = asyncio.all_tasks()
    
    # await asyncio.gather(*tasks)
    
    # rtasks = asyncio.all_tasks()
    # for task in rtasks:
        # print(task)
    print(len(asyncio.all_tasks()) - 1)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
