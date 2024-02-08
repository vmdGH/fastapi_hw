from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='func1',
            description='Проверочный get-запрос'
        ),
        BotCommand(
            command='func2',
            description='Помощь'
        ),
        BotCommand(
            command='func3',
            description='Получить собаку по id'
        ),
        BotCommand(
            command='func4',
            description='Помощь'
        ),
        BotCommand(
            command='func5',
            description='Добавить собаку'
        ),
        BotCommand(
            command='func6',
            description='Помощь'
        )


    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())