"""Spammy Animations β οΈ"""
import asyncio
from collections import deque

from alphaz import Message, alphaz


@alphaz.on_cmd("think$", about={"header": "Berpura-pura Berpikir"})
async def think_(message: Message):
    """think"""
    deq = deque(list("π€π§π€π§π€π§"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@alphaz.on_cmd("lmaos$", about={"header": "lmaos Bruh! xD Lol"})
async def lamos_(message: Message):
    """lmaos"""
    deq = deque(list("ππ€£ππ€£ππ€£"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@alphaz.on_cmd("nothappy$", about={"header": "Perubahan emosi secara cepat"})
async def Moods_(message: Message):
    """Mood Swing"""
    deq = deque(list("πβΉοΈπβΉοΈπβΉοΈπ"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await message.edit("".join(deq))
        deq.rotate(1)


@alphaz.on_cmd("muah$", about={"header": "LUV"})
async def muah_(message: Message):
    """MUAH"""
    deq = deque(list("πππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@alphaz.on_cmd("heart$", about={"header": "Hati pelangi"})
async def heart_(message: Message):
    """β₯οΈ"""
    deq = deque(list("β€οΈπ§‘πππππ€"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@alphaz.on_cmd("gym$", about={"header": "Jadilah Aktif !, Tetap sehat πͺ"})
async def gym_(message: Message):
    """Gym"""
    deq = deque(list("πβπβπ€Έβπβπβπ€Έβπβπβπ€Έβ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@alphaz.on_cmd("smoon$", about={"header": "Animasi kensar moon lainnya"})
async def smoon_(message: Message):
    """smoon"""
    animation_interval = 0.1
    animation_ttl = range(101)
    await message.edit("smoon..")
    animation_chars = [
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 8])


@alphaz.on_cmd("tmoon$", about={"header": "Animasi kensar moon lainnya"})
async def tmoon_(message: Message):
    """tmoon"""
    animation_interval = 0.1
    animation_ttl = range(117)
    await message.edit("tmoon")
    animation_chars = [
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 32])
