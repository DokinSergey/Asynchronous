import os,sys,time,traceback
# from glob import glob
from rich import print as rpn
import asyncio
import aiofiles
import aiofiles.os as aos
#pylint: disable-msg=W0603

AllSumm = 0
PathPath = r'C:\Dev\5000folder'
semaphore = asyncio.Semaphore(1000)
lock = asyncio.Lock()

async def ReadFile(CurrentPath):
    global AllSumm
    try:
        FilePath = os.path.join(PathPath,CurrentPath)
        # rpn(f'FilePath = {FilePath}')
        async with semaphore:
            for PFN in await aos.listdir(FilePath):
                FileName = os.path.join(FilePath,PFN)
                # rpn(f'\tFileName = {FileName}')
                async with aiofiles.open(FileName, mode='r', encoding = 'utf_8') as fn:
                    linerow = await fn.readline()
                line = linerow.strip()
                digit = int(line) if line.isdigit()  else 0
                rpn(f'\t{FileName = } {line = } {digit = }')
                async with lock:
                    AllSumm += digit
    except Exception as _err:
        rpn(f'[red1]RF: {_err}')
        rpn(f'[red1]RF: {traceback.format_exc()}')

async def main():
    try:
        # print(await aos.listdir(FilePath))
        tasks = [asyncio.create_task(ReadFile(FileName)) for FileName in await aos.listdir(PathPath)]
        await asyncio.gather(*tasks)
        print(AllSumm)
                # rpn('-',end = '', flush=True)
    except Exception as err:
        rpn(f'[red1]Ошибка {err}')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
