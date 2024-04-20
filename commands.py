from aiogram.types import BotCommand

commands: list[BotCommand] = [
    BotCommand(command='/help', description='get help'),
    BotCommand(command='/kitty', description='get a kitty'),
]
