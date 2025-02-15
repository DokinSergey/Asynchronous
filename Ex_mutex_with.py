​​​​'''
Алексей хочет войти в комнату.
Алексей вошел в комнату.
Мария хочет войти в комнату.
Иван хочет войти в комнату.
Алексей вышел из комнаты.
Мария вошел в комнату.
Мария вышел из комнаты.
Иван вошел в комнату.
Иван вышел из комнаты.
В этом исправленном коде async with self.lock: заменяет прямое использование await self.lock.acquire()
 и self.lock.release(), обеспечивая автоматическое управление блокировкой. Это делает код более безопасным
 и упрощает его понимание, поскольку не требуется явно вызывать методы захвата и освобождения замка,
 минимизируя риск ошибок управления состоянием замка.
'''
import sys,time
import asyncio

# Эмуляция комнаты с замком
class Room:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def use(self, name):
        # Использование менеджера контекста для работы с замком
        async with self.lock:
            print(f"{name} вошел в комнату.")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(1)
            print(f"{name} вышел из комнаты.")

async def person(name, room):
    # Человек (задача) пытается использовать комнату
    print(f"{name} хочет войти в комнату.")
    await room.use(name)

async def main():
    room = Room()  # Инициализация комнаты с замком

    # Создание задач для нескольких людей, пытающихся войти в комнату
    await asyncio.gather(
        person("Алексей", room),
        person("Мария", room),
        person("Иван", room))

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
