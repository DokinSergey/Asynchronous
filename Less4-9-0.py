import sys,time
import asyncio

data = [
  {
    "Имя": "Sarah",
    "Фамилия": "Lewis",
    "Уровень секретности": 1,
    "Срок доступа": "5857 часов",
  },
  {
    "Имя": "Kevin",
    "Фамилия": "Watkins",
    "Уровень секретности": 9,
    "Срок доступа": "7446 часов",
  },
  {
    "Имя": "Andrew",
    "Фамилия": "Allen",
    "Уровень секретности": 2,
    "Срок доступа": "1652 часов",
  },
  {
    "Имя": "Amanda",
    "Фамилия": "Smith",
    "Уровень секретности": 1,
    "Срок доступа": "6185 часов",
  },
  {
    "Имя": "Samantha",
    "Фамилия": "Nguyen",
    "Уровень секретности": 9,
    "Срок доступа": "2346 часов",
  },
  {
    "Имя": "David",
    "Фамилия": "Ingram",
    "Уровень секретности": 1,
    "Срок доступа": "3363 часов",
  },
  {
    "Имя": "Emma",
    "Фамилия": "Richardson",
    "Уровень секретности": 9,
    "Срок доступа": "115 часов",
  },
  {
    "Имя": "Brian",
    "Фамилия": "Aguilar",
     "Уровень секретности": 6,
    "Срок доступа": "2947 часов",
  },
  {
    "Имя": "Samantha",
    "Фамилия": "Chang",
    "Уровень секретности": 4,
    "Срок доступа": "6693 часов",
  },
  {
    "Имя": "Brandon",
    "Фамилия": "Williams",
    "Уровень секретности": 2,
    "Срок доступа": "2810 часов",
  },
  {
    "Имя": "Michael",
    "Фамилия": "Strickland",
    "Уровень секретности": 7,
    "Срок доступа": None,
  },
  {
    "Имя": "Kyle",
    "Фамилия": "Barnett",
    "Уровень секретности": 1,
    "Срок доступа": "7745 часов",
   },
  {
    "Имя": "Damon",
    "Фамилия": "Alvarado",
    "Уровень секретности": 5,
    "Срок доступа": "3894 часов",
  },
  {
    "Имя": "Cindy",
    "Фамилия": "Sanchez",
    "Уровень секретности": 9,
    "Срок доступа": "4045 часов",
  },
  {
    "Имя": "Michelle",
    "Фамилия": "Hernandez",
    "Уровень секретности": 3,
    "Срок доступа": "2744 часов",
  },
  {
    "Имя": "Whitney",
    "Фамилия": "Ross",
    "Уровень секретности": 10,
    "Срок доступа": "2687 часов",
  },
  {
    "Имя": "Deborah",
    "Фамилия": "Golden",
    "Уровень секретности": 2,
    "Срок доступа": "698 часов",
  },
  {
    "Имя": "Nicholas",
    "Фамилия": "Whitaker",
    "Уровень секретности": 10,
    "Срок доступа": "47 часов",
  },
  {
    "Имя": "Rebecca",
    "Фамилия": "Mercer",
    "Уровень секретности": 4,
    "Срок доступа": "141 часов",
  },
  {
    "Имя": "Mary",
    "Фамилия": "Mora",
    "Уровень секретности": 1,
    "Срок доступа": "4474 часов",
  }]

async def check_access(data_elem):
    # print(f'Test {data_elem["Срок доступа"]} {type(data_elem["Срок доступа"])} {data_elem["Фамилия"]} {data_elem["Имя"]} {data_elem["Уровень секретности"]}')
    await asyncio.sleep(data_elem["Уровень секретности"])
    if data_elem["Срок доступа"]:
        print(f'Участник {data_elem["Имя"]} {data_elem["Фамилия"]} имеет действующий доступ. Продолжительность доступа: {data_elem["Срок доступа"]}')
    else:
        # print(f'Test поймали исключение {data_elem["Имя"]} {data_elem["Фамилия"]}')
        raise ValueError(f'Ошибка доступа: У участника {data_elem["Имя"]} {data_elem["Фамилия"]} срок доступа истек или не указан.')

async def main():
    tasks = [asyncio.create_task(check_access(participant),name = f'{participant["Имя"]} {participant["Фамилия"]}') for participant in data]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    for task in done:
        if task.exception() is not None:
            print(task.exception())
            for penftask in pending:
                print(f'Доступ участника {penftask.get_name()} отменен из-за критической ошибки.')
                # отменять необязательно, так как задачи приостановлены
                # penftask.cancel()
            break

        # print("Задание завершено:", task.get_name())
start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
