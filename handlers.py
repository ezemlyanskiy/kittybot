from aiogram import Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from constants import MESSAGES
from utils import send_image

router = Router()


@router.message(CommandStart())
async def cmd_start_handler(message: Message) -> None:
    await message.answer(
        MESSAGES.get('start').format(html.bold(message.from_user.full_name))
    )
    await send_image(message)
    await message.answer(MESSAGES.get('one_more'))


@router.message(Command('help'))
async def cmd_help_handler(message: Message) -> None:
    await message.answer(MESSAGES.get('help'))


@router.message(Command('kitty'))
async def cmd_kitty_handler(message: Message) -> None:
    await send_image(message, start=False)


@router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception:
        await message.answer(MESSAGES.get('bad_request'))
