import asyncio

async def generate(a):
    print(f'Корутина generate с аргументом {a}')

async def main():
    for i in range(10):
        await generate(i)

asyncio.run(main())