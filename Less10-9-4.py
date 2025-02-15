import os,sys,time
import traceback
from glob import glob
from rich import print as rpn
import json
import asyncio
import aiofiles
# import aiofiles.os as aos
#pylint: disable-msg=W0603

# semaphore = asyncio.Semaphore(100)
lock = asyncio.Lock()
Result:list[dict[str,str]] = []

async def ParsingLine(line,keyss):
    global Result
    td = {}
    for ni,nv in enumerate(line.split(';')):
        td[keyss[ni]] = nv
    rpn(f'{td}')
    # async with lock:
        # Result.append(td)
    # rpn(f'\t{td['Идентификатор объекта']}')


async def main():
    try:
        FileName = r'C:\Dev\address_10000.csv'
        async with aiofiles.open(FileName, mode='r', encoding = 'utf-8-sig') as fn:
            listline = await fn.readlines()
        if listline:linerow = listline[0]
        keyss = list(ii for ii in linerow.strip().split(';'))
        # rpn(keyss)
        tasks = [asyncio.create_task(ParsingLine(line.strip(),keyss)) for nn,line in enumerate(listline) if nn]
        await asyncio.gather(*tasks)
                # line = linerow.strip()[22:]
                # await ParsingLine(line)
        
        to_json = json.dumps(Result, indent=4, ensure_ascii=False)
        with open(r'C:\Dev\address.json', 'w', encoding = 'utf_8') as cf:
            print(to_json,file = cf)
        rpn('Готово')
        # rpn(to_json)
    except Exception as err:
        rpn(f'[red1]Main:{err}')
        rpn(f'[red1]Main:{traceback.format_exc()}')
start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
