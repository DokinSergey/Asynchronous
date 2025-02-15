import sys,time
import asyncio
import random

random.seed(1)

SERVERS = [
    "api.database.local",
    "auth.backend.local",
    "web.frontend.local",
    "cache.redis.local",
    "analytics.bigdata.local"]

STATUSES = ["Online", "Offline", "Maintenance", "Error"]

async def monitor_servers(servers):
    for server in servers:
        await asyncio.sleep(.1)
        status = random.choice(STATUSES)
        yield (server,status)

async def main():
    async for server_status in monitor_servers(SERVERS):
        print(f'{server_status[0]}: состояние {server_status[1]}')

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
