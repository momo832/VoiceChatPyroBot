from pyrogram import filters
from pyrogram.handlers import MessageHandler
import player
from config import SUDO_FILTER


async def skip(client, message):
    if player.abort():
        await message.reply_text("מדלג לשיר הבא...")
    else:
        await message.reply_text("אין שיר מושמע כדי לדלג.")

__handlers__ = [
    [
        MessageHandler(
            skip,
            filters.command("skip", "/")
            & SUDO_FILTER
        )
    ]
]
