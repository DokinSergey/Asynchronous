import os,sys,time
# from glob import glob
from rich import print as rpn
import asyncio
import aiofiles
import aiofiles.os as aos
#pylint: disable-msg=W0603

AllSumm = 0
FilePath = r'C:\Dev\files'
semaphore = asyncio.Semaphore(1000)


async def ReadFile(FileName):
    global AllSumm
    try:
        FileNameR = os.path.join(FilePath,FileName)
        async with semaphore:
            async with aiofiles.open(FileNameR, mode='r', encoding = 'utf_8') as fn:
                linerow = await fn.readline()
            line = linerow.strip()
            digit = int(line) if line.isdigit() and not int(line)%2 else 0
            print(f'{FileNameR = } {line = } {int(line)%2} {digit = }')
            AllSumm += digit
    except Exception as _err:
        rpn(f'[red1]Ошибка {_err}')

async def main():
    try:
        # print(await aos.listdir(FilePath))
        tasks = [asyncio.create_task(ReadFile(FileName)) for FileName in await aos.listdir(FilePath)]
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
