import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from app.api.v1.router import api_router
from app.bot.setup import start_bot, stop_bot
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_bot()
    yield
    await stop_bot()


app = FastAPI(title="FitLab API", lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")


@app.post("/webhook")
async def webhook(request: Request):
    from aiogram.types import Update
    from app.bot.setup import bot, dp

    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
