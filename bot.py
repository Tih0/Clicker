import asyncio

from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button (text="🖼️ Сделай Никите кудри!", web_app=WebAppInfo(
        url="..."
    ))
    return builder.as_markup()

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Помоги Никите стать красивым!', reply_markup=webapp_builder())

async def main() -> None:
    bot = Bot(..., parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())