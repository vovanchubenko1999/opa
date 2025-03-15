from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from config.database.data import DataBase
import os

db = DataBase(os.path.join(os.getcwd(), "config", "database", "data.db"))

# _________________________Настройка Бота____________________________
admin_id = [6063898733]
token = "1234567:TOKEN"
# ___________________________________________________________________

# ___________________________________________________________________
balance_for_referral = 20
balance_for_click = 1
money_name = "EndCoin"
bot_username = "endway"
min_withdraw = 228
redirect_link = "https://endway.org"
min_referrer_withdraw = 1
feedback_link = "https://endway.org"
# ___________________________________________________________________
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
