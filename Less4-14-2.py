import sys,time
import asyncio
import random

articles = [
    {
        "id": 1,
        "title": "Основы Python",
        "content": "Python – язык программирования, который подходит для решения широкого спектра задач, от веб-разработки до анализа данных и машинного обучения. Благодаря своей простоте Python часто используется в начале обучения программированию. Python поддерживает множество библиотек, фреймворков, таких как Django для веб-разработки и Pandas для работы с данными. Выбирайте Python !"
    },
    {
        "id": 2,
        "title": "Введение в JavaScript",
        "content": "JavaScript – это язык программирования, который выполняется в браузере и позволяет создавать динамичные, интерактивные веб-страницы. JavaScript поддерживает функциональное, а также объектно-ориентированное программирование, асинхронное программирование. JavaScript является основным языком для фронтенд-разработки, часто используется вместе с HTML и CSS."
    },]

def find_most_common_word(text: str):
    dct = {}
    listxt = text.lower().split()
    for itxt in listxt:
        dct[itxt] = listxt.count(itxt)
    return [ai for ai,bi in dct.items() if bi == max(dct.values())][0]

async def download_and_process(article: dict):
    await asyncio.sleep(random.uniform(0.1, 0.5))
    res = await asyncio.to_thread(find_most_common_word,article["content"])
    article['tag'] = res

async def main():
    await asyncio.gather(*[asyncio.create_task(download_and_process(article)) for article in articles])

    for iti in articles:
        print(f"{iti['title']}: {iti['tag']}")


start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
