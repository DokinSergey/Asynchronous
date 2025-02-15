import sys
import asyncio

async def coroutine(x):
    await asyncio.sleep(1)
    print(f"Coroutine {x} is done")

async def main():
    
    tasks = [asyncio.create_task(corutine(i)) for i in range(10)]
    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)

#получение прерваной задачи, проверять остальное не имеет смысла
done, canceled = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    print([task.exception() for task in done if task.exception()][0])
    
asyncio.run(main())

if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
