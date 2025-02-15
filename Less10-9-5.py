# import os
import sys,time
import traceback
from glob import glob
from rich import print as rpn
import aiocsv
import csv
import json
import asyncio
import aiofiles
# import aiofiles.os as aos
#pylint: disable-msg=W0603

Result:list[dict[str,str]] = []
semaphore = asyncio.Semaphore(1000)
lock = asyncio.Lock()

class CustomDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    doublequote = True# Если этот параметр True, две кавычки внутри поля трактуются как одна кавычка
    skipinitialspace = True# Если параметр True, пробелы в начале каждого поля игнорируются
    lineterminator = '\n'# Определяет символ окончания строки в csv файле как "\n"
    # Указывает, что кавычки должны окружать только те поля, которые содержат специальные символы (например,
    # разделитель, кавычки или любой из символов новой строки)
    quoting = csv.QUOTE_MINIMAL
#--------------------------------------------------------------------------------------------------------
csv.register_dialect('customDialect', CustomDialect) # Регистрирует диалект с именем 'customDialect'

async def ParsingLine(td):
    global Result
    try:
        if td['Балл ЕГЭ'].isdigit() and int(td['Балл ЕГЭ']) == 100:
            async with lock:
                Result.append(td)
            # rpn(f'\t[green1]{td['ФИО']} : {td['Балл ЕГЭ']}')
    except Exception as _err:
        rpn(f'[red1]PR:{_err}')
        rpn(f'[red1]PR:{td}')
        rpn(f'[red1]PR:{traceback.format_exc()}')
        input('Err :-> ')

async def ReadFile(FileName):
    try:
        async with semaphore:
            async with aiofiles.open(FileName, mode='r', encoding = 'utf-8-sig') as fn:
                reader = aiocsv.AsyncDictReader(fn, dialect='customDialect')
                async for row in reader:
                    await ParsingLine(row)

        rpn(f'[yellow]{FileName}')
    except Exception as _err:
        rpn(f'[red1]RF:{_err}')
        # rpn(f'[red1]PR:{line}')
        # rpn(f'[red1]PR:{keyss}')
        # rpn(f'[red1]PR:{line.split(',')}')
        rpn(f'[red1]RF:{traceback.format_exc()}')

async def main():
    try:
        listcsv = glob(r'C:\Dev\region_student\Задача Студенты\*\*.csv', recursive=True)
        tasks = [asyncio.create_task(ReadFile(FileName)) for FileName in listcsv]
        await asyncio.gather(*tasks)
        rpn('---')
        students = sorted(Result, key=lambda x: x['Телефон для связи'])
        # rpn('{')
        # for k,v in DictResult.items():
            # print(f'    "{k}": "{round(float(v)*0.03,2)}р",')
        # rpn('}')
        to_json = json.dumps(students, indent=4, ensure_ascii=False)
        with open(r'C:\Dev\ege.json', 'w', encoding = 'utf_8') as cf:
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
