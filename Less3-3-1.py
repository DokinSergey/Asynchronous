import asyncio

async def my_task():
    print("Task started")
    await asyncio.sleep(1)
    print("Task finished")

async def main():
    asyncio.create_task(my_task())
    await asyncio.sleep(2)

asyncio.run(main())


input(':->')
