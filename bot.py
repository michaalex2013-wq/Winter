import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)
TOKEN = "8375650210:AAG0oThklqf1oexTp2NEi3wXWiNW54p_zyQ"
WEBAPP_URL = "https://michaalex2013-wq.github.io/Winter/"

bot = Bot(token=TOKEN)
dp = Dispatcher()
users_db = set()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_name = message.from_user.username or f"id{message.from_user.id}"
    
    if user_name not in users_db:
        users_db.add(user_name)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❄️ Открыть WinterGram Каз", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton(text="💳 Пополнение / Вывод", callback_data="wallet_info")]
    ])
    
    await message.answer(
        f"Привет, @{user_name}! Добро пожаловать в **WinterGram Каз** 🎰\n\n"
        "Заходи в мини-приложение, крути кейсы и забирай призы!",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.callback_query(lambda c: c.data == "wallet_info")
async def process_wallet(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "💳 **Пополнение и вывод средств**\n\n"
        "Чтобы пополнить баланс или вывести выигранные NFT/Звёзды, обратитесь к менеджеру:\n\n"
        "👉 Связь: @rubup\n\n"
        "Напишите ему свой юзернейм и сумму для обмена.",
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
