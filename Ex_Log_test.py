import os,sys,time,traceback,inspect#,base64
# import chardet
import asyncio
import aiofiles
# from typing import Any
# import aiofiles.os as aos
from rich import print as rpn
# from multiprocessing import Process
from platform import python_version#,node
from datetime import datetime as dt#,date as ddate,time as dtime
##--------------------------------------------------------------------------------------
__author__  = 't.me/dokin_sergey'
__version__ = '0.0.1'
__verdate__ = '2026-01-21 12:59'
##-------------------------------------------------------------------------------------
LogPath:str = ''
LogFile:str = ''
ByError:int = 0
CountProc:int = 0
debug:bool = False
T0 = time.perf_counter()
##------------------------------------------------------------------------------------------
#pylint: disable-msg=W0602
project,_ = os.path.splitext(os.path.basename(__file__))
##################################################################################################################
def LogInit(dbg:bool = False)->bool:
    global LogFile,LogPath
    _GlobaLen = 170
    LogPath = os.path.join(os.path.dirname(__file__),'.dbg') if dbg else os.path.join(os.path.dirname(__file__),'.log')
    # LogPath = os.path.join(os.path.dirname(__file__),'.dbg')
    ##-------------------------------------------------------------------------------------------------------------
    try:
        if not os.path.isdir(LogPath):os.makedirs(LogPath)
        LogFile = os.path.join(LogPath,f'{dt.now().strftime("%Y-%m-%d")}-{os.getpid()}.txt')
        with open(LogFile, mode = 'a', encoding = 'utf-8-sig') as sn:
            print('## ','-' * (_GlobaLen ), file = sn)
    ##------------------------------------------------------------------------------------------------------------------------
    except Exception:
        Lini = False
    else:
        Lini = True
    return Lini
##################################################################################################################
async def Alog(Mess1:str,Mess2:str,Mess3:str = '',dbg:bool = False)->bool:
    global ByError
    #TypeMess = ('Message','Success','Warning','ErrMess','ErrTrac','EndWork')
    TypeMess = {'Message':'dark_cyan','Success':'light_green','Warning':'yellow1','ErrMess':'bright_red',
    'ErrTrac':'orange_red1','EndWork':'green1'}
    if len(Mess1) == 7 and Mess1 in TypeMess:
        TMess = Mess1#+' '
        RMess = Mess2
    else:
        TMess = 'Message'
        RMess = Mess1
    Funct = Mess3 if Mess3 else inspect.stack()[1][3]
    ##------------------------------------------------------------------------------------------
    if TMess in ('Warning','ErrMess','ErrTrac'):ByError += 1
    ##-------------------------------------------------------------------------------------------
    try:
        dtstr = dt.now().strftime("%H:%M:%S")
        lFN = 13
        FN = f'{Funct:{lFN}} ;' if Funct else f'{" ":{lFN}} ;'
        MesStr = f'{TMess};{dtstr};{FN}{RMess}\n'
    #------------------------------------------------------------------------------------------
        if dbg or not LogFile:
            rpn(f'[{TypeMess[TMess]}]{(time.perf_counter() - T0):>7.2f} :{FN}{RMess}')
        #------------------------------------------------------------------------------------------------
        if LogFile:
            async with aiofiles.open(LogFile, mode='a', encoding = 'utf-8-sig',newline = '\r\n') as _afn:
                await _afn.write(MesStr)
    #--------------------------------------------------------------------
        # if TMess == 'EndWork' and ByError and not dbg:
        # # if TMess == 'EndWork' and dbg:
            # await Report_Write(f'Выявлено {ByError} ошибок')
            # TgStr  = f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n{os.getlogin()}  @  {node()}\n'
            # TgStr += f'{os.path.basename(__file__)}\nВыявлено {ByError} ошибок'
            # await TgBotMess(TgStr)
        #--------------------------------------------------------------------------------------------------
    except Exception:
        Led = False
    else:
        Led = True
    return Led
#######################################################################################################################
def Log(Mess1:str,Mess2:str,Mess3:str = '',dbg:bool = False)->bool:
    global ByError
    #TypeMess = ('Message','Success','Warning','ErrMess','ErrTrac','EndWork')
    TypeMess = {'Message':'dark_cyan','Success':'light_green','Warning':'yellow1','ErrMess':'bright_red',
    'ErrTrac':'orange_red1','EndWork':'green1'}
    if len(Mess1) == 7 and Mess1 in TypeMess:
        TMess = Mess1#+' '
        RMess = Mess2
    else:
        TMess = 'Message'
        RMess = Mess1
    Funct = Mess3 if Mess3 else inspect.stack()[1][3]
    ##------------------------------------------------------------------------------------------
    if TMess in ('Warning','ErrMess','ErrTrac'):ByError += 1
    ##-------------------------------------------------------------------------------------------
    try:
        dtstr = dt.now().strftime("%H:%M:%S")
        lFN = 13
        FN = f'{Funct:{lFN}} ;' if Funct else f'{" ":{lFN}} ;'
        MesStr = f'{TMess};{dtstr};{FN}{RMess}\n'
    #------------------------------------------------------------------------------------------
        if dbg or not LogFile:
            rpn(f'[{TypeMess[TMess]}]{(time.perf_counter() - T0):>7.2f} :{FN}{RMess}')
        #------------------------------------------------------------------------------------------------
        if LogFile:
            with open(LogFile, mode='a', encoding = 'utf-8-sig',newline = '\r\n') as _fn:
                _fn.write(MesStr)
    #--------------------------------------------------------------------
        # if TMess == 'EndWork' and ByError and not dbg:
        # # if TMess == 'EndWork' and dbg:
            # await Report_Write(f'Выявлено {ByError} ошибок')
            # TgStr  = f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n{os.getlogin()}  @  {node()}\n'
            # TgStr += f'{os.path.basename(__file__)}\nВыявлено {ByError} ошибок'
            # await TgBotMess(TgStr)
        #--------------------------------------------------------------------------------------------------
    except Exception:
        Led = False
    else:
        Led = True
    return Led
#######################################################################################################################
def test_proc(_key:str,_value:int)->None:
    print(f'Запущен процесс  {_key:5} : {_value}')
    time.sleep(_value)
    Log('Message',f'\t{_key:5} : {_value}',dbg = debug)
#######################################################################################################################
#######################################################################################################################
async def mainloop()->None:
    global nowdtl#,nstrok,FilePrs,SshHost,NewFInd,Servers

    # await Alog('Message',f'    psycopg: {PGversion.__version__}',dbg = debug)
    kwargs = {'one': 20, 'two': 5, 'three': 7, 'four': 15, 'five': 10,'six': 9, 'seven': 12, 'eight': 14, 'nine': 17, 'ten': 13}

    # Создайте процесс, передаем список и словарь через args и kwargs
    # await asyncio.gather(*[asyncio.create_task(asyncio.to_thread(test_proc,key,value) for key,value in kwargs.items())])
    # tasks = []
    try:
        for key,value in kwargs.items():
            asyncio.create_task(asyncio.to_thread(test_proc,key,value))
            # asyncio.create_task(test_proc(key,value))
            # await asyncio.gather(asyncio.to_thread(test_proc,key,value))
            # tasks.append(asyncio.to_thread(test_proc,key,value))
        # await asyncio.gather(*tasks)
    except BaseException as _err:
        await Alog('ErrTrac',f'{traceback.format_exc().splitlines()[-1]}',dbg = debug)
        # await Log('ErrTrac',f'FileName = {_fKey}',dbg = debug)
###########################################################################################################
if __name__ == '__main__':
    nowdtl = dt.now()
    debug = (len(sys.argv) > 1 and str(sys.argv[1]) in ('Debug','True','cons'))
    CountProc += 1
    # rpn(f'{(time.perf_counter() - T0):>7.2f} Запуск № {CountProc}')
    LogInit(debug)
    rpn(f'[cyan1]Start [green1]{project} [cyan1]Now [orange1]{nowdtl.strftime("%Y-%m-%d %H:%M:%S")}')
    rpn(f'[cyan1]debug is [orange_red1]{debug} [cyan1]Запуск № [green1]{CountProc}')
    rpn(f'[cyan1]Start ver.[green1]{__version__} [cyan1]от [green1]{__verdate__} [cyan1]Python: [green1]{python_version()}')
    Log('Message',f'Start {nowdtl.strftime("%Y-%m-%d %H:%M:%S")}',project)
    Log('Message',f'Start DeepKlin log 1C ver.{__version__} от {__verdate__} Python: {python_version()}')
    try:
        start_time = time.perf_counter()
        if sys.platform == "win32":#Python < 3.14
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(mainloop())
    except BaseException as _err:
        rpn(f'[orange_red1]{_err}')
        rpn(f'[orange_red1]{traceback.format_exc()}')
    if debug:input('__main__ :-)> ')
    sys.exit()
