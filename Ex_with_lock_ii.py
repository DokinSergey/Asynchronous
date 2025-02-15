​​​​import sys,time
import asyncio

# Общий ресурс, который будет обновляться
shared_resource = 0

# Создаем асинхронный замок для обеспечения безопасности при обновлении shared_resource
lock = asyncio.Lock()

async def update_resource():

    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')

    # Используем асинхронный замок для обеспечения безопасности при обновлении shared_resource
    async with lock:

        # Сохраняем текущее значение shared_resource во временную переменную
        temp = shared_resource
        await asyncio.sleep(1)

        # Увеличиваем значение shared_resource на 1
        shared_resource = temp + 1
    print('Обновление shared_resource завершено')

async def main():
    await asyncio.gather(update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
