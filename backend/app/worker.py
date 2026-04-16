from celery import Celery
from celery.schedules import crontab
from app.core.config import settings

celery_app = Celery("fitlab", broker=settings.redis_url, backend=settings.redis_url)

celery_app.conf.beat_schedule = {
    "send-daily-workouts": {
        "task": "app.worker.send_daily_workout_notifications",
        "schedule": crontab(hour=6, minute=0),
    },
}

@celery_app.task
def send_daily_workout_notifications():
    """
    Find all users with active subscriptions and send today's workout
    via Telegram bot notification.
    TODO: implement with asyncio.run() + bot.send_message()
    """
    pass
