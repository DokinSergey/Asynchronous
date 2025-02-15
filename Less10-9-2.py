import os,sys,time
import traceback
from rich import print as rpn
import json
import asyncio
import aiofiles
import aiofiles.os as aos
#pylint: disable-msg=W0603

DictResult = {}
FilePath = r'C:\Dev\chat_log'
semaphore = asyncio.Semaphore(100)
lock = asyncio.Lock()

async def ParsingLine(line):
    global DictResult
    key,value = line.split(':')
    # rpn(f'>{key}<;>{value.strip()}<')
    cost = len(value.strip())
    async with lock:
        if (oldvalue := DictResult.get(key)) is None:
            DictResult.setdefault(key,cost)
        else: DictResult[key] = oldvalue + cost
    # rpn(f'\t{key}')

async def ReadFile(FileName):
    try:
        FileNameR = os.path.join(FilePath,FileName)
        async with semaphore:
            async with aiofiles.open(FileNameR, mode='r', encoding = 'utf_8') as fn:
                async for linerow in fn:
                    # linerow = await fn.readline()
                    line = linerow.strip()[22:]
                    await ParsingLine(line)
        rpn(FileNameR)
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        rpn(f'[red1]RF:{traceback.format_exc()}')

async def main():
    try:
        # round(float(v), 2)*0.03
        tasks = [asyncio.create_task(ReadFile(FileName)) for FileName in await aos.listdir(FilePath)]
        await asyncio.gather(*tasks)
        # await asyncio.create_task(ReadFile('chat_1.txt'))

        rpn()
        rpn('{')
        for k,v in DictResult.items():
            print(f'    "{k}": "{round(float(v)*0.03,2)}р",')
        rpn('}')
        to_json = json.dumps(DictResult, indent=4, ensure_ascii=False)
        rpn()
        rpn(to_json)
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
