from pyrogram import filters
from pyrogram.handlers import MessageHandler
import player
from config import SUDO_FILTER, LOG_GROUP


async def stream(client, message):
    if player.current:
        await message.reply_text(
            "לא יכול להזרים בזמן השמעת מוזיקה."
        )
    else:
        args = message.text.split()

        if len(args) == 1:
            await message.reply_text(
                "שלח לי קישור ישיר להזרמה."
            )
        elif len(args) != 2:
            await message.reply_text(
                "נתת יותר מקישור אחד."
            )
        else:
            stream = player.stream(
                args[1],
                [
                    client.send_message,
                    [
                        LOG_GROUP,
                        "<b>עכשיו מזרים</b>\n"
                        "<pre>{}</pre>".format(
                            args[1]
                        )
                    ]
                ] if LOG_GROUP else None
            )

            await message.reply_text(
                "מזרים..."
            )

__handlers__ = [
    [
        MessageHandler(
            stream,
            filters.command("stream", "/")
            & SUDO_FILTER
        )
    ]
]
