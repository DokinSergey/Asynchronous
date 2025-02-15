import os
import sys,time
import traceback
# from glob import glob
from rich import print as rpn
import aiocsv
import csv
import json
import asyncio
import aiofiles
import aiofiles.os as aos
#pylint: disable-msg=W0603

ResDict:dict[str,int] = {'Б/У':0,'Новый':0}
listcsv = []
semaphore = asyncio.Semaphore(1000)
reslock = asyncio.Lock()
lstlock = asyncio.Lock()

class CustomDialect(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    doublequote = True# Если этот параметр True, две кавычки внутри поля трактуются как одна кавычка
    skipinitialspace = True# Если параметр True, пробелы в начале каждого поля игнорируются
    lineterminator = '\n'# Определяет символ окончания строки в csv файле как "\n"
    # Указывает, что кавычки должны окружать только те поля, которые содержат специальные символы (например,
    # разделитель, кавычки или любой из символов новой строки)
    quoting = csv.QUOTE_MINIMAL
#--------------------------------------------------------------------------------------------------------
csv.register_dialect('customDialect', CustomDialect) # Регистрирует диалект с именем 'customDialect'
##############################################################################################################
async def ParsingLine(td):
    global ResDict
    try:
        if td['Состояние авто'] == 'Б/У':
            async with reslock:
                ResDict['Б/У'] += int(td['Стоимость авто'])
        elif td['Состояние авто'] == 'Новый':
            async with reslock:
                ResDict['Новый'] += int(td['Стоимость авто'])
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
            async with aiofiles.open(FileName, mode='r', encoding = 'windows-1251') as fn:
                reader = aiocsv.AsyncDictReader(fn, dialect='customDialect')
                async for row in reader:
                    await ParsingLine(row)
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
    global listcsv
    nextpaths = []
    try:
        for item in await aos.listdir(CurrentPath):
            item1 = os.path.join(CurrentPath,item)
            if os.path.isfile(item1):
                _, ext = os.path.splitext(item)
                if ext.lower() == '.csv':
                    async with lstlock:
                        listcsv.append(item1)
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
        NextPath = [r'C:\Dev\Auto']
        while NextPath:
            tasks = [asyncio.create_task(ParsingPath(PNext)) for PNext in NextPath]
            NextPath = []
            await asyncio.gather(*tasks)
            for task in tasks:
                NextPath += task.result()# for task in tasks]
            i += len(NextPath)
            rpn(i)
        rpn(f'Обработано папок {i} добавлено {len(listcsv)} файлов')
        #-------------------------------------------------------------------------------
        # await asyncio.create_task(ReadFile(listcsv[0]))
        tasks = [asyncio.create_task(ReadFile(FileName)) for FileName in listcsv]
        await asyncio.gather(*tasks)
        rpn('---')
        # students = sorted(Result, key=lambda x: x['Телефон для связи'])
        rpn(ResDict)

        to_json = json.dumps(ResDict, indent=4, ensure_ascii=False)
        with open(r'C:\Dev\auto.json', 'w', encoding = 'utf_8') as cf:
            print(to_json,file = cf)
        # rpn('Готово')
        # # rpn(to_json)
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
