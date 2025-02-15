import sys,time
import asyncio

async def producer(queues,patient_info):
    for patient in patient_info:
        await asyncio.sleep(0.5)
        await queues[patient['direction']].put(patient)
        print(f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")
    for _,que in queues.items():
        await que.put(None)

async def consumer(queue):
    while (item := await queue.get()) is not None:
        # if (item := await queue.get()) is None:break
        print(f"{item['direction']} принял пациента: {item['name']}, процедура: {item['procedure']}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def main():
    patient_info = [
        {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
        {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
        {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
        {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
        {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
        {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
        {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
        {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
        {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
        {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}]
    direction = set(drc['direction'] for drc in patient_info)
    queues = ({dri:asyncio.Queue() for dri in direction})
    tasks = [asyncio.create_task(producer(queues,patient_info))]
    tasks += [asyncio.create_task(consumer(queue)) for _,queue in queues.items()]
    await asyncio.wait(tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
