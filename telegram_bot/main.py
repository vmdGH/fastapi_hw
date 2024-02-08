import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from core.handlers.basic import get_start, func1, func2, func3, func4, func5, func6
from core.settings import settings
from core.utils.commands import set_commands


import asyncio
import logging


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')




async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s" 
                        )
    # bot = Bot(token=settings.bots.bot_token)
    bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(func1, Command(commands=['func1']))
    dp.message.register(func2, Command(commands=['func2']))
    dp.message.register(func3, Command(commands=['func3']))
    dp.message.register(func4, Command(commands=['func4']))
    dp.message.register(func5, Command(commands=['func5']))
    dp.message.register(func6, Command(commands=['func6']))

    dp.message.register(get_start)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == '__main__':
    asyncio.run(start())










# import logging
# from aiogram import Bot, Dispatcher, types
# import asyncio

# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# import aiohttp
# import os

# API_TOKEN = os.environ['6961140643:AAFH4dCjBRs_eNcIFV2Jlzf-kU-vL6UgNAw']
# API_URL = 'https://hw-fastapi.onrender.com'

# async def async_request(url, total_timeout=40, return_only_status=False):
#     session_timeout = aiohttp.ClientTimeout(total=total_timeout,sock_connect=10,sock_read=30)
#     async with aiohttp.ClientSession(trust_env=True, timeout=session_timeout) as session:
#         async with session.get(url) as resp:
#             if return_only_status:
#                 return resp.status
#             response = await resp.json(content_type=None)
#             return response

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot, dispatcher, and storage
# bot = Bot(token=API_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

# # Define states
# class Form(StatesGroup):
#     button1 = State()
#     button2 = State()

# async def on_startup(_):
#     print("Bot is online")

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     inline_kb = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton(f"Check", callback_data=f"button_{1}")
#     inline_kb.add(button1)
#     button2 = types.InlineKeyboardButton(f"Dog by id", callback_data=f"button_{2}")
#     inline_kb.add(button2)
#     await message.answer("Choose a button:", reply_markup=inline_kb)

# @dp.callback_query_handler(lambda c: c.data.startswith('button_'))
# async def handle_button_click(callback_query: types.CallbackQuery, state: FSMContext):
#     button_number = callback_query.data.split('_')[1]
#     await bot.answer_callback_query(callback_query.id)

#     # Set state according to the button pressed
#     await state.set_state(Form.all_states[int(button_number)-1])
#     if int(button_number) == 1:
#         await callback_query.message.answer(f"You clicked Check button. Type anything to get response.")
#     if int(button_number) == 2:
#         await callback_query.message.answer(f"You clicked Dog by id button. Now, type dog id.")

# # Input handlers for each button
# @dp.message_handler(state=Form.button1)
# async def handle_input_button1(message: types.Message, state: FSMContext):
#     try:
#         url = API_URL
#         response_url = await async_request(url)
#         await message.answer(response_url)
#     except Exception as ex:
#         await message.answer(f'Error {str(ex)}')
#     await state.finish()

# @dp.message_handler(state=Form.button2)
# async def handle_input_button2(message: types.Message, state: FSMContext):
#     try:
#         dog_id = message.text
#         url = API_URL + '/dog/' + dog_id
#         response = await async_request(url)
#         await message.answer(f"Info about dog ID {dog_id}: " + str(response))
#     except Exception as ex:
#         await message.answer(f'Error {str(ex)}')
#     await state.finish()

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
