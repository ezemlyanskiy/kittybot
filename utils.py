import logging

import aiohttp

from aiogram.types import Message

from constants import CAT_ENDPOINT, DOG_ENDPOINT, MESSAGES
from keyboards import reply_kb

logger = logging.getLogger(__name__)


async def fetch_image(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json = await response.json()
            return json[0].get('url')


async def get_new_image() -> str:
    try:
        return await fetch_image(CAT_ENDPOINT)
    except Exception as e:
        logger.error(MESSAGES.get('main_api_error').format(e))
        return await fetch_image(DOG_ENDPOINT)


async def send_image(message: Message, start: bool = True) -> None:
    await message.answer_photo(
        await get_new_image(),
        reply_markup=reply_kb if start else None,
    )
