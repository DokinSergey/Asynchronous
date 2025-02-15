​​​​import sys,time
import asyncio

bank_account = 1000

# Принимает сумму для снятия и блокировку для безопасного доступа к банковскому счету
async def withdraw_money(amount, lock):
    global bank_account

    # Используем асинхронную блокировку для безопасного доступа к банковскому счету
    async with lock:
        if bank_account >= amount:
            print(f"Снятие {amount} р. успешно")
            await asyncio.sleep(1)
            bank_account -= amount

async def main():
    lock = asyncio.Lock()
    task1 = asyncio.create_task(withdraw_money(900, lock))
    task2 = asyncio.create_task(withdraw_money(900, lock))


    await asyncio.gather(task1, task2)
    print(f'Остаток средств {bank_account} р.')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
