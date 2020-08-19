# BY code-rgb

from requests import get
from bs4 import BeautifulSoup
"""Gapps via inline bot"""
from userge import userge, Message, Config
from pyrogram import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    Filters, CallbackQuery)





@userge.on_cmd("gapps", about={
    'header': "Get Gapps"}, allow_channels=False)
async def gapps_inline(message: Message):
    await message.edit("`🔍 Finding Latest Gapps...`")
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "gapps")
    await userge.send_inline_bot_result(chat_id=message.chat.id,
                                        query_id=x.query_id,
                                        result_id=x.results[1].id)
    await message.delete()



if Config.BOT_TOKEN and Config.OWNER_ID:
    if Config.HU_STRING_SESSION:
        ubot = userge.bot
    else:
        ubot = userge


    @ubot.on_callback_query(filters=Filters.regex(pattern=r"^open_gapps$"))
    async def open_cb(_, callback_query: CallbackQuery):
        gapps_link = []
        sforge = "https://sourceforge.net/projects/opengapps/files/arm64/"
        url = get(sforge)
        if url.status_code == 404:
            return
        page = BeautifulSoup(url.content, 'lxml')
        date = page.table.tbody.tr['title']
        varient = ["aroma", "super", "stock", "full", "mini", "micro", "nano", "pico"]
        gapps = len(varient)
        for i in range(gapps):
            link = f"{sforge}/{date}/open_gapps-arm64-10.0-{varient[i]}-{date}.zip/download"
            gapps_link.append(link)                

        open_g = [
        [InlineKeyboardButton(text="aroma", url=gapps_link[0]),
        InlineKeyboardButton(text="super", url=gapps_link[1]),
        InlineKeyboardButton(text="stock", url=gapps_link[2])],
        [InlineKeyboardButton(text="full", url=gapps_link[3]),
        InlineKeyboardButton(text="mini", url=gapps_link[4]),
        InlineKeyboardButton(text="micro", url=gapps_link[5])],
        [InlineKeyboardButton(text="nano", url=gapps_link[6]),
        InlineKeyboardButton(text="pico", url=gapps_link[7])],
        [InlineKeyboardButton(text="⏪ Back", callback_data=back_gapps)]
        ]

        await callback_query.edit_message_text(callback_query.chat.id,
            callback_query.message_id,
            "**OPEN GAPPS**",
            reply_markup=InlineKeyboardMarkup(open_g)
        )

    @ubot.on_callback_query(filters=Filters.regex(pattern=r"^flame_gapps$"))
    async def flame_cb(_, callback_query: CallbackQuery):
        link = "https://sourceforge.net/projects/flamegapps/files/arm64/android-10/"
        url = get(link)
        if url.status_code == 404:
            return
        page = BeautifulSoup(url.content, 'lxml')
        content = page.tbody.tr
        date = content['title']
        date2 = date.replace("-","")
        flame = "{link}{date}/FlameGApps-10.0-{varient}-arm64-{date2}.zip/download"
        basic = flame.format(link=link, date=date, varient="basic", date2=date2)
        full = flame.format(link=link, date=date, varient="full", date2=date2)
       
        flame_g = [[InlineKeyboardButton(text="FULL", url=full),
                   InlineKeyboardButton(text="BASIC", url=basic)],
                   [InlineKeyboardButton(text="⏪ Back", callback_data=back_gapps)]]

        await callback_query.edit_message_text(callback_query.chat.id,
            callback_query.message_id,
            "**FLAME GAPPS**",
            reply_markup=InlineKeyboardMarkup(flame_g)
        )

    @ubot.on_callback_query(filters=Filters.regex(pattern=r"^nik_gapps$"))
    async def nik_cb(_, callback_query: CallbackQuery):
        link = "https://sourceforge.net/projects/nikgapps/files/Releases/NikGapps-Q/"
        url = get(link)
        if url.status_code == 404:
            return
        page = BeautifulSoup(url.content, 'lxml')
        content = page.tbody.tr
        date = content['title']
        latest_niks = f"{link}{date}/"
        nik_g = [[InlineKeyboardButton(text="Lastest", url=latest_niks)],
                 [InlineKeyboardButton(text="⏪ Back", callback_data=back_gapps)]]

        await callback_query.edit_message_text(callback_query.chat.id,
            callback_query.message_id,
            "**NIK GAPPS**",
            reply_markup=InlineKeyboardMarkup(nik_g)
        )

    @ubot.on_callback_query(filters=Filters.regex(pattern=r"^back_gapps$"))
    async def back_cb(_, callback_query: CallbackQuery):

        buttons = [[InlineKeyboardButton("Open Gapps", callback_data="open_gapps")],
                             [InlineKeyboardButton("Flame Gapps", callback_data="flame_gapps")],
                             [InlineKeyboardButton("Nik Gapps", callback_data="nik_gapps")]]
 
        await callback_query.edit_message_text(callback_query.chat.id,
            callback_query.message_id,
            "**LATEST Android 10 arm64 Gapps**",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
