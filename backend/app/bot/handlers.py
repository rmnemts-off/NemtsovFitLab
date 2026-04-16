from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.setup import dp
from app.core.config import settings


def trainer_only(message: Message) -> bool:
    return message.from_user.id == settings.trainer_telegram_id


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в FitLab!")


# ── Trainer commands ──────────────────────────────────────────────────────────

@dp.message(Command("subscribers"), F.func(trainer_only))
async def cmd_subscribers(message: Message):
    """List active subscribers per program."""
    # TODO: implement via SubscriptionService
    await message.answer("Список подписчиков — в разработке.")


# TODO: add FSM handlers for creating workouts and uploading exercises
