# by Alfarezaπ

import asyncio

from alphaz import alphaz


@alphaz.on_cmd("hack$", about={'header': "kensar hacking animation"})
async def hack_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    heckerman = user['mention']
    animation_chars = [
        "```Connecting To Private Server \\```",
        "```Connecting To Private Server |```",
        "```Connecting To Private Server /```",
        "```Connecting To Private Server \\```",
        "```Connection Established ```",
        "```Target Selected```",
        "```Backdoor Found In Target```",
        "```Trying To Hack```",
        "```Hacking... 0%\nββββββββββββββββββββββ```",
        "```Hacking... 4%\nββββββββββββββββββββββ```",
        "```Hacking... 8%\nββββββββββββββββββββββ```",
        "```Hacking... 20%\nββββββββββββββββββββββ```",
        "```Hacking... 36%\nββββββββββββββββββββββ```",
        "```Hacking... 52%\nββββββββββββββββββββββ```",
        "```Hacking... 70%\nββββββββββββββββββββββ```",
        "```Hacking... 88%\nββββββββββββββββββββββ```",
        "```Hacking... 100%\nβββββββββββββββββββββββ```",
        "```Preparing Data... 1%\nβββββββββββββββββββββββ```",
        "```Preparing Data... 14%\nβββββββββββββββββββββββ```",
        "```Preparing Data... 30%\nβββββββββββββββββββββββ```",
        "```Preparing Data... 55%\nβββββββββββββββββββββββ```",
        "```Preparing Data... 72%\nβββββββββββββββββββββββ```",
        "```Preparing Data... 88%\nβββββββββββββββββββββββ```",
        "```Prepared Data... 100%\nβββββββββββββββββββββββ```",
        "```Uploading Data to Server... 12%\nβββββββββββββββββββββββ```",
        "```Uploading Data to Server... 44%\nβββββββββββββββββββββββ```",
        "```Uploading Data to Server... 68%\nβββββββββββββββββββββββ```",
        "```Uploading Data to Server... 89%\nβββββββββββββββββββββββ```",
        "```Uploaded Data to Server... 100%\nβββββββββββββββββββββββ```",
        "**User Data Upload Completed:** Target's User Data Stored "
        "at `downloads/victim/telegram-authuser.data.sql`",
    ]
    hecked = (f"**Targeted Account Hacked**\n\n```Pay 69$ To``` {heckerman}``` "
              "To Remove This Hack```")
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(2)
        await message.edit(animation_chars[i % max_ani])
    await message.edit(hecked)
