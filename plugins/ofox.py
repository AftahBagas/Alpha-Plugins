"""By code-rgb"""

import pyrogram 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from userge import userge, Message
import json
import requests
from html_telegraph_poster import TelegraphPoster


@userge.on_cmd("ofox", about={'header': "get orangefox recovery by device codename"})
async def ofox_(message: Message):
  if not message.input_str:
    await message.err("Provide a device codename to search recovery", del_in=2)
    return
  t = TelegraphPoster(use_api=True)
  t.create_api_token('Userge-X')
  await message.edit("🔍 searching for recovery...", del_in=2)
  photo = "https://i.imgur.com/582uaSk.png" 
  API_HOST = 'https://api.orangefox.download/v2/device/'
  codename = message.input_str
  try:
    cn = requests.get(f"{API_HOST}{codename}")
    r = cn.json()
  except ValueError:
    await message.err(f"recovery not found for {codename}!", del_in=3) 
    return
  s = requests.get(f"{API_HOST}{codename}/releases/stable/last").json()
  info = f"📱 **Device**: {r['fullname']}\n"
  info += f"👤 **Maintainer**: {r['maintainer']['name']}\n\n"
  recovery = f"🦊 <code>{s['file_name']}</code>\n"
  recovery+= f"📅 {s['date']}\n"
  recovery += f"ℹ️ **Version:** {s['version']}\n"
  recovery+= f"📌 **Build Type:** {s['build_type']}\n"
  recovery+= f"🔰 **Size:** {s['size_human']}\n\n"
  recovery+= "📍 **Changelog:**\n"
  recovery+= f"<code>{s['changelog']}</code>\n\n" 
  msg = info
  msg += recovery
  notes_ = s.get('notes')
  if notes_: 
    notes = t.post(
      title='READ Notes', 
      author="", 
      text=notes_
    )
    
    button = [[
      pyrogram.InlineKeyboardButton(
      text="🗒️ NOTES", url=notes['url']
      ),
      pyrogram.InlineKeyboardButton(
      text="⬇️ DOWNLOAD", url=s['url']
      )     
    ]]
  else:
    button = [[
      pyrogram.InlineKeyboardButton(
      text="⬇️ DOWNLOAD", url=s['url']
      )     
    ]]
  
    # Client Check
  if message.client.is_bot:
    ubot = userge.bot
    #
    await ubot.send_photo(
      message.chat.id,
      photo=photo,
      caption=msg,
      reply_markup=pyrogram.InlineKeyboardMarkup(button)
    )
    return
  ubot = userge  
  if notes_: 
    msg += f"🗒️ <a href={notes['url']}>NOTES</a>\n"
  msg +=f"⬇️ <a href={s['url']}>DOWNLOAD</a>"
  await ubot.send_photo(
      message.chat.id,
      photo=photo,
      caption=msg
  )
