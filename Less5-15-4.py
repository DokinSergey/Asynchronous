import sys,time
import asyncio

async def publish_post(text):
    await asyncio.sleep(1)
    print(f"Пост опубликован: {text}")
    return f"Пост опубликован: {text}"

async def notify_subscribers(subscriber):
    await asyncio.sleep(1)
    print(f"Уведомление отправлено {subscriber}")

async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    await asyncio.create_task(publish_post(post_text))
    tasks = [asyncio.create_task(notify_subscribers(subscriber)) for subscriber in subscribers]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
