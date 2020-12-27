from pyrogram import filters
from pyrogram.handlers import MessageHandler


async def mistake(client, message):
    await message.reply_text("נראה שזה טעות...")


__handlers__ = [
    [
        MessageHandler(
            mistake,
            (filters.all & ~ filters.text)
            & filters.private
        )
    ]
]
