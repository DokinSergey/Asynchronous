import os
# import time
import traceback
# import chardet
import asyncio
import aiosqlite
from rich import print as rpn
##--------------------------------------------
FileSQL = r'D:\AдресаТелефоныАрхив\AddressBook.db'
Table = 'Phones'

#########################################################################################
async def ReadSQL(TabName:str)->bool:
    try:
        async with aiosqlite.connect(FileSQL) as aSQL:
            rpn(f'{dir(aSQL) = }')
            async with aSQL.execute(f"SELECT * from {TabName}") as cursor:
                rpn(f'{dir(cursor) = }')
                # async for row in cursor:

                    # rpn(row)
        await aSQL.close()

        rpn(aSQL)
    except Exception as _err:
        rpn('ErrMess',f'{_err}')
        rpn('ErrTrac',f'{traceback.format_exc()}')
        return False
    return True
#########################################################################################
#########################################################################################
if __name__ == '__main__':
    debug = True

    while not input('Выполнить :-> '):
        asyncio.run(ReadSQL(Table))

    ##-----------------------------------------
    os._exit(0)
