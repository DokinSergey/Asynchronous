import asyncio

async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)

async def main():
    future = asyncio.Future()
    asyncio.ensure_future(set_after(future, 1, 'done'))
    result = await future
    print(result)

asyncio.run(main())
input(':->')
