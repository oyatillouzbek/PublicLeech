#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Assalomu alaykum.Men Youtubedan video yuklab beruvchi bot bolaman. Foydalanish uchun habar yozayotganingizda @vid Ummon deb yozing va jonatmay ozgina kuting.Ummonning youtubedagi kliplari chiqadi.Ustiga bosib osha xabarga javob tariqasida reply qilib /ytdl buyrugini yuboring.Uyogini oziz tushinib olasiz")

async def help_message_f(client, message):
    # await message.reply_text("Sizga yordam bera olmayman).", quote=True)
    # display the /help message
    await message.reply_text(
        f"Assalomu alaykum.Men Youtubedan video yuklab beruvchi bot bolaman. Foydalanish uchun habar yozayotganingizda @vid Ummon deb yozing va jonatmay ozgina kuting.Ummonning youtubedagi kliplari chiqadi.Ustiga bosib osha xabarga javob tariqasida reply qilib /ytdl buyrugini yuboring.Uyogini oziz tushinib olasiz",
        quote=True
    )


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="Bu yerga kiring.",
            url="https://t.me/YTDownloaders/7389"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "Botda qayta nomlash funksiyasi vaqtinchalik ishlamayapti.",
        quote=True,
        reply_markup=reply_markup
    )
