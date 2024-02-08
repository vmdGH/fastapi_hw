from aiogram import Bot
from aiogram.types import Message
import aiohttp

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}')
    await message.answer(f'Hello, {message.from_user.first_name}')
    await message.reply(f'Hello, {message.from_user.first_name}, {message.from_user.id}')



API_URL = 'http://fastapi_service:80'
async def func1(message: Message, bot: Bot):
    try:
        url = API_URL
        response_url = await async_request(url)
        await message.answer(response_url)
    except Exception as ex:
        await message.answer(f'Error {str(ex)}')


async def async_request(url, total_timeout=40, return_only_status=False):
    session_timeout = aiohttp.ClientTimeout(total=total_timeout,sock_connect=10,sock_read=30)
    async with aiohttp.ClientSession(trust_env=True, timeout=session_timeout) as session:
        async with session.get(url) as resp:
            if return_only_status:
                return resp.status
            response = await resp.json(content_type=None)
            return response



    
async def func2(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Йоу2')

async def func3(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Йоу3')

async def func4(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Йоу4')

async def func5(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Йоу5')

async def func6(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Йоу6')


    