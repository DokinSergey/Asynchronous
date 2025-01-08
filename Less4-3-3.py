import sys,time

import asyncio
import random

# Не менять.
random.seed(1)

class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"

# Тут пишите ваш код
async def check_mail(server):

    # while True:
    for _ in range(5):
        new_mail = await server.check_for_new_mail()
        if isinstance(new_mail,str):
            print(new_mail)
        elif new_mail:
            mail = await server.fetch_new_mail()
            print(mail)
        else:
            print("Новых писем нет.")
        await asyncio.sleep(1)


async def main():

    server = MailServer()
    await check_mail(server)


start_time = time.perf_counter()
asyncio.run(main())
stop_time = time.perf_counter()
Inetrval = stop_time - start_time
print(f'Общее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
