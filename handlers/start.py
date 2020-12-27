from pyrogram import filters
from pyrogram.handlers import MessageHandler


async def start(client, message):
    await message.reply_text("היי, שלח לי קישור לשיר / סרטון מיוטויב ואני אשמיע אותו בקבוצה: 
@radio_ilGroup

הבוט רץ ע"י @Yishaicohen")

__handlers__ = [
    [
        MessageHandler(
            start,
            filters.command("start", "/")
            & filters.private
        )
    ]
]
