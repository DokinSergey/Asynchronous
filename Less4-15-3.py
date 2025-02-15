import sys,time
import asyncio
import contextvars

current_language = contextvars.ContextVar('current_language', default='')

def set_language(language_code):
    return current_language.set(language_code)

async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings[current_language.get()]


async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurrió un error."
    }
    return error_messages[current_language.get()]

async def test_user_actions(language_code):
    token = set_language(language_code)
    print(await get_greeting())
    print(await get_error_message())
    current_language.reset(token)

async def main():
    languages = ('en','ru','es')
    tasks = [asyncio.create_task(test_user_actions(language_code)) for language_code in languages]
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
asyncio.run(main())
stop_time =  time.perf_counter()
Inetrval = stop_time - start_time
print(f'\nОбщее время выполнения {Inetrval:.7f}')
if not (len(sys.argv) > 1 and sys.argv[1] == 'cons'):input(':-> ')
sys.exit(0)
