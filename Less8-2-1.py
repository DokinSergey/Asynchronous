import sys,time
# from random import random
import asyncio

patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]

async def producer(queue):
    for patient in patient_info:
        await queue.put(patient)
        print(f'Регистратор добавил в очередь: {patient}')
        await asyncio.sleep(0)

async def consumer(queue):
    while True:
        item = await queue.get()  # получение элемента из очереди
        if item is None:  # если элемент равен None - выход из цикла
            break
        print(f'Врач принял пациента: {item}')
        # указание, что ранее поставленная в очередь задача завершена
        queue.task_done()
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)

async def main():
    queue = asyncio.Queue()
    prod_task = asyncio.create_task(producer(queue))
    cons_task = asyncio.create_task(consumer(queue))
    await prod_task
    await queue.put(None)  # добавление элемента None в очередь для выхода из цикла
    await cons_task

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
