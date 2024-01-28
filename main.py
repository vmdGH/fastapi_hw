import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiohttp
import os

API_TOKEN = os.environ['BOT_TOKEN']
API_URL = 'https://hw-fastapi.onrender.com'

async def async_request(url, total_timeout=40, return_only_status=False):
    session_timeout = aiohttp.ClientTimeout(total=total_timeout,sock_connect=10,sock_read=30)
    async with aiohttp.ClientSession(trust_env=True, timeout=session_timeout) as session:
        async with session.get(url) as resp:
            if return_only_status:
                return resp.status
            response = await resp.json(content_type=None)
            return response

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot, dispatcher, and storage
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Define states
class Form(StatesGroup):
    button1 = State()
    button2 = State()

async def on_startup(_):
    print("Bot is online")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    inline_kb = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Check", callback_data=f"button_{1}")
    inline_kb.add(button1)
    button2 = types.InlineKeyboardButton(f"Dog by id", callback_data=f"button_{2}")
    inline_kb.add(button2)
    await message.answer("Choose a button:", reply_markup=inline_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('button_'))
async def handle_button_click(callback_query: types.CallbackQuery, state: FSMContext):
    button_number = callback_query.data.split('_')[1]
    await bot.answer_callback_query(callback_query.id)

    # Set state according to the button pressed
    await state.set_state(Form.all_states[int(button_number)-1])
    if int(button_number) == 1:
        await callback_query.message.answer(f"You clicked Check button. Type anything to get response.")
    if int(button_number) == 2:
        await callback_query.message.answer(f"You clicked Dog by id button. Now, type dog id.")

# Input handlers for each button
@dp.message_handler(state=Form.button1)
async def handle_input_button1(message: types.Message, state: FSMContext):
    try:
        url = API_URL
        response_url = await async_request(url)
        await message.answer(response_url)
    except Exception as ex:
        await message.answer(f'Error {str(ex)}')
    await state.finish()

@dp.message_handler(state=Form.button2)
async def handle_input_button2(message: types.Message, state: FSMContext):
    try:
        dog_id = message.text
        url = API_URL + '/dog/' + dog_id
        response = await async_request(url)
        await message.answer(f"Info about dog ID {dog_id}: " + str(response))
    except Exception as ex:
        await message.answer(f'Error {str(ex)}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
