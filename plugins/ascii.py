"""Reply to an Media to convert to ascii sticker"""
# Module by @deleteduser420 (https://github.com/code-rgb)
# Copyright 2017, Shanshan Wang, MIT license
# Based on https://gist.github.com/wshanshan/c825efca4501a491447056849dd207d6

import os
from PIL import Image, ImageOps, ImageFont, ImageDraw
from userge import userge, Message, Config, media_to_image
import numpy as np
from colour import Color
import random


@userge.on_cmd("ascii", about={
    'header': "Ascii Sticker",
    'description': "transform on any gif/sticker/image to an Ascii Sticker. ",
    'usage': " {tr}ascii [reply to media]",
    'flags': {
        '-alt': "To get inverted Ascii Sticker"},
    'examples': [
        "{tr}ascii [reply to media]",
        "{tr}ascii -alt [reply to media]"]})
async def ascii_(message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.edit("```Reply To Message Dummy```")
        await message.reply_sticker('CAADAQADhgADwKwII4f61VT65CNGFgQ')
        return
    if '-alt' in message.flags:
        ascii_type = "alt"
    else:
        ascii_type = ""
    dls_loc = await media_to_image(message)
    if not dls_loc:
        return
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808"
    webp_file = asciiart(dls_loc, 0.1, 1.9, color1, color2, bgcolor, ascii_type)
    await message.client.send_sticker(
        chat_id=message.chat.id,
        sticker=webp_file,
        reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)
    os.remove(dls_loc)


def asciiart(in_f, SC, GCF, color1, color2, bgcolor, ascii_type):
    chars = np.asarray(list(' .,:irs?@9B&#'))
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height / letter_width
    img = Image.open(in_f)
    if not img.mode == 'RGB':
       img = img.convert('RGB')
    if ascii_type == "alt":
        img = ImageOps.invert(img)
    widthByLetter = round(img.size[0] * SC * WCF)
    heightByLetter = round(img.size[1] * SC)
    S = (widthByLetter, heightByLetter)
    img = img.resize(S)
    img = np.sum(np.asarray(img), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)
    lines = ("\n".join(("".join(r) for r in chars[img.astype(int)]))).split("\n")
    nbins = len(lines)
    colorRange = list(Color(color1).range_to(Color(color2), nbins))
    newImg_width = letter_width * widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)
    leftpadding = 0
    y = 0
    lineIdx = 0
    for line in lines:
        color = colorRange[lineIdx]
        lineIdx += 1
        draw.text((leftpadding, y), line, color.hex, font=font)
        y += letter_height
    image_name = "ascii.webp"
    webp_file = os.path.join(Config.DOWN_PATH, image_name)
    newImg.save(webp_file, "WebP")
    return webp_file


def random_color():
    number_of_colors = 2
    color = ['#' + ''.join([random.choice('0123456789ABCDEF') for j in
             range(6)]) for i in range(number_of_colors)]
    return color
