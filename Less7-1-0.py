import sys,time
import asyncio
balance = 100

async def withdraw(amount):
    global balance
    if balance >= amount:
        await asyncio.sleep(0.1)  # Имитация проверки баланса
        balance -= amount
        return True
    return False

async def main():
    transaction1 = asyncio.create_task(withdraw(100))
    transaction2 = asyncio.create_task(withdraw(100))
    results = await asyncio.gather(transaction1, transaction2)
    print("Transactions successful:", results)
    

start_time = time.perf_counter()
asyncio.run(main())
print("Final balance:", balance)
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
