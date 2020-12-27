from pyrogram import filters
from pyrogram.handlers import MessageHandler
import player


async def song(client, message):
    get = player.currently_playing()
    if get:
        await message.reply_text(
            """
כותרת השיר: <a href="{}">{}</a>
ע"י: <a href="tg://user?id={}">{}</a>
            """.format(
                get["url"],
                get["title"],
                get["sent_by_id"],
                get["sent_by_name"]
            ),
            parse_mode="HTML"
        )
    else:
        await message.reply_text(
            "אין שיר מושמע כרגע."
        )

__handlers__ = [
    [
        MessageHandler(
            song,
            filters.command("song", "/")
            & filters.private
        )
    ]
]
