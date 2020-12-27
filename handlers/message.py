from pyrogram import filters
from pyrogram.handlers import MessageHandler
from helpers import is_youtube
from ytdl import download
import player
from config import LOG_GROUP


async def message(client, message):
    if message.text.startswith("/"):
        return

    if not is_youtube(message.text):
        await message.reply_text("קישור זה (link) לא תקין.")
        return

    if "list=" in message.text:
        await message.reply_text("שלח לי קישור לסרטון, לא קישור לפלייליסט.")
        return

    await message.reply_text("ההורדה תוזמנה", quote=True)
    download(
        (
            message.reply_text,
            ("מוריד...",)
        ),
        (
            message.reply_text,
            (f"השיר הורד ותוזמן להשמיע בתור מספר {player.q.qsize() + 1}.",)
        ),
        [
            player.play,
            [
                None,
                (
                    message.reply_text,
                    ("מנגן...",)
                ),
                (
                    message.reply_text,
                    ("סיימתי לנגן את השיר שלך, תודה 🎶",)
                ),
                None,
                None,
                message.from_user.id,
                message.from_user.first_name,
                [
                    client.send_message,
                    [
                        LOG_GROUP,
                        "<b>עכשיו מנגן</b>\n"
                        "כותרת השיר: <a href=\"{}\">{}</a>\n"
                        "ע"י: <a href=\"tg://user?id={}\">{}</a>"
                    ]
                ] if LOG_GROUP else None
            ]
        ],
        (
            message.reply_text,
            "אי אפשר להוריד שידורים חיים."
        ),
        message.text,
    )


__handlers__ = [
    [
        MessageHandler(
            message,
            filters.text
            & filters.private
            & ~ filters.regex(r"^x .+")
        ),
        2
    ]
]
