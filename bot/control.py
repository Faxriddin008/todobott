import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .config import token

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage)
