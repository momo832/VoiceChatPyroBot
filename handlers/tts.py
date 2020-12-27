import _thread
import subprocess
from gtts import gTTS
import time
from pyrogram import filters
from pyrogram.handlers import MessageHandler


async def tts(client, message):
    if message.text.replace("/tts", "") == "":
        await message.reply_text("תן לי קצת טקסט להשמיע.")
    else:
        try:
            gTTS(message.text.replace("/tts ", ""),
                 lang="en-US").save("downloads/tts.mp3")
            m = await message.reply_text("משמיע את הטקסט...")
            _thread.start_new_thread(
                subprocess.Popen(["mplayer", "downloads/tts.mp3"]).wait,
                ()
            )
            await m.edit("סיימתי להשמיע.")
        except:
            await message.reply_text("אירעה שגיאה.")

            
async def x(client, message):
    try:
        try:
            await message.delete()
        except:
            pass
        text = message.text.split(" ")
        del text[0]
        text = " ".join(text)
        gTTS(text, lang="en-US").save("downloads/tts.mp3")
        _thread.start_new_thread(
            subprocess.Popen(["mplayer", "downloads/tts.mp3"]).wait,
            ()
        )
    except:
        pass
            

__handlers__ = [
    [
        MessageHandler(
            tts,
            filters.command("tts", "/")
        )
    ],
    [
        MessageHandler(
            x,
            filters.regex(r"^x .+")
        )
    ]
]
