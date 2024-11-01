from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from SONALI import app
from SONALI.misc import SUDOERS
from SONALI.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND , prefixes=["", "/"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("در حال فعال‌سازی چت صوتی... لطفاً کمی صبر کنید.")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("چت فعالی نیست")
    else:
        await mystic.edit_text(
            f"**چت فعال :-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND , prefixes=["", "/"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("در حال فعال‌سازی چت صوتی... لطفاً کمی صبر کنید.")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("چت فعالی نیست")
    else:
        await mystic.edit_text(
            f"**ویدیو چت فعال:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["ac"]) & SUDOERS)
async def vc(client, message: Message):
    ac_audio = str(len(await get_active_chats()))

    await message.reply_text(f"مشخصات چت فعال: {ac_audio}")


__MODULE__ = "ویس چت"
__HELP__ = """
<b>✧ /ac</b> - چک کردن چت‌های صوتی فعال بر روی ربات.

<b>✧ /activevoice</b> - چک کردن چت‌های صوتی و تماس‌های ویدیویی فعال بر روی ربات.

<b>✧ /activevideo</b> - چک کردن تماس‌های ویدیویی فعال بر روی ربات.

<b>✧ /stats</b> - چک کردن آمار ربات‌ها

"""
