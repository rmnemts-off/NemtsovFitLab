from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.core.config import settings

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()


async def start_bot():
    from app.bot import handlers  # noqa: F401 — registers all handlers
    await bot.set_webhook(settings.webhook_url)


async def stop_bot():
    await bot.delete_webhook()
    await bot.session.close()
