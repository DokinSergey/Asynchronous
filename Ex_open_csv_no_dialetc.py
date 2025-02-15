import os
import sys,time
from datetime import datetime
import traceback
# from glob import glob
from rich import print as rpn
from aiocsv import AsyncDictWriter
import csv
import json
import asyncio
import aiofiles
import aiofiles.os as aos
#pylint: disable-msg=W0603

ResList:dict[str,str] = []
listJSON = []
semaphore = asyncio.Semaphore(1000)
reslock = asyncio.Lock()
lstlock = asyncio.Lock()

##############################################################################################################
async def ParsingLine(td):
    global ResList
    try:
        if td['HTTP-статус'] == 200:
            async with reslock:
                ResList.append(td)
            # rpn(f'\t[green1]{td['ФИО']} : {td['Балл ЕГЭ']}')
    except Exception as _err:
        rpn(f'[red1]PR:{_err}')
        rpn(f'[red1]PR:{td}')
        rpn(f'[red1]PR:{traceback.format_exc()}')
        input('Err :-> ')
##############################################################################################################
async def ReadFile(FileName):
    try:
        async with semaphore:
            async with aiofiles.open(FileName, mode='r', encoding = 'utf_8') as fn:
                context = await fn.read()
                templates = json.loads(context)
                tasks_p = [asyncio.create_task(ParsingLine(CurDict)) for CurDict in templates]
                await asyncio.gather(*tasks_p)
                # for idict in templates:
                    # rpn(idict)
        # rpn(f'[yellow]{FileName}')
        rpn('*',end = '',flush = True)
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        # rpn(f'[red1]PR:{line}')
        # rpn(f'[red1]PR:{keyss}')
        # rpn(f'[red1]PR:{line.split(',')}')
        rpn(f'[red1]RF:{traceback.format_exc()}')
################################################################################################################
async def ParsingPath(CurrentPath:str):
    global listJSON
    nextpaths = []
    try:
        for item in await aos.listdir(CurrentPath):
            item1 = os.path.join(CurrentPath,item)
            if os.path.isfile(item1):
                _, ext = os.path.splitext(item)
                if ext.lower() == '.json':
                    async with lstlock:
                        listJSON.append(item1)
            else:
                nextpaths.append(item1)
    #--------------------------------------------------------
    except Exception as _err:
        rpn(f'[red1]PP:{_err}')
        rpn(f'[red1]PP:{traceback.format_exc()}')
    return nextpaths
################################################################################################################
async def main():
    i = 0
    try:
        NextPath = [r'C:\Dev\logs']
        while NextPath:
            tasks = [asyncio.create_task(ParsingPath(PNext)) for PNext in NextPath]
            NextPath = []
            await asyncio.gather(*tasks)
            for task in tasks:
                NextPath += task.result()# for task in tasks]
            i += len(NextPath)
            rpn(i)
        rpn(f'Обработано папок {i} добавлено {len(listJSON)} файлов')
    #-------------------------------------------------------------------------------
        # await asyncio.create_task(ReadFile(listJSON[0]))
        tasks = [asyncio.create_task(ReadFile(FileName)) for FileName in listJSON]
        await asyncio.gather(*tasks)
    #--------------------------------------------------------------------------------
        rpn('\n----------------------------')
        # tds = ResList
        tds = sorted(ResList, key=lambda x: x['Время и дата'])
        for itd in tds:
            ddata = datetime .strptime(itd['Время и дата'],'%Y-%m-%d %H:%M:%S')
            pdata = ddata.strftime('%d.%m.%Y %H:%M:%S')
            # rpn(ddata,pdata)
            itd['Время и дата'] = pdata
    #--------------------------------------------------------------------------------
        async with aiofiles.open(r'C:\Dev\logs.csv', mode="w", encoding="utf-8-sig", newline="") as afp:
            # writer = AsyncDictWriter(afp, fieldnames=['Время и дата', 'IP-адрес','User-Agent','Запрошенный URL','HTTP-статус','']), quoting=csv.QUOTE_MINIMAL-sig
            fieldnames=['Время и дата', 'IP-адрес','User-Agent','Запрошенный URL','HTTP-статус','Реферер','Cookie',
                'Размер страницы и заголовки ответа','Метод запроса','Информация об ошибке']
            writer = AsyncDictWriter(afp,fieldnames, delimiter=';', quotechar='"',lineterminator = '\n', quoting=csv.QUOTE_MINIMAL)
            await writer.writeheader()
            await writer.writerows(tds) #, dialect='customDialect'


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
