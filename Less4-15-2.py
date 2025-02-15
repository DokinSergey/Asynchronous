import sys,time
import asyncio
import contextvars

order_state = contextvars.ContextVar('order_state', default='')

def set_order_state(state):
    return order_state.set(state)


async def process_order(order_id):
    states = ["Принят","Обрабатывается", "Отправлен"]
    for _order_state in states:
        await asyncio.sleep(1)
        token = set_order_state(_order_state)
        print(f"Заказ {order_id} сейчас в состоянии: {_order_state}")
    #---------------------------------
    order_state.reset(token)

async def main():
    orders = ["Заказ1", "Заказ123", "Заказ12345"]
    tasks = [asyncio.create_task(process_order(order_id)) for order_id in orders]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
