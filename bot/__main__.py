#    This file is part of the FileSharing distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/FileSharingBot/blob/main/License> .


from . import *
from .worker import *

bot.start(bot_token=Var.BOT_TOKEN)
LOGS.info("Bot starting...")


@bot.on(
    events.NewMessage(
        incoming=True, pattern="/start ?(.*)", func=lambda e: e.is_private
    )
)
async def _(e):
    add_user(e.sender_id)
    u_id = e.pattern_match.group(1)
    if u_id:
        await get_iteams(e, u_id)
    else:
        await e.reply(
            f"Hi {e.sender.first_name}\n**I can store private files and others users can access files form shareable link**",
            buttons=[
                [Button.inline("HELP", data="help")],
                [
                    Button.url("SOURCE CODE", url="github.com/kaif-00z/"),
                    Button.url("DEVELOPER", url="t.me/kaif_00z"),
                ],
            ],
        )


@bot.on(events.NewMessage(incoming=True, pattern="/generatelink"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    await gen_link(e)


@bot.on(events.NewMessage(incoming=True, pattern="/revoke"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    link = e.text.split()[1]
    u_id = link.split("start=")[1]
    await revoke_link(e, u_id)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("help")))
async def _(e):
    await e.edit(
        "`/generatelink` for generate link\n`/revoke <link>` for revoke the link"
    )


@bot.on(events.ChatAction)
async def _(e):
    await hmm(e)


@bot.on(events.NewMessage(incoming=True, pattern="\\/boardcast"))
async def _(e):
    await bcast(e)


@bot.on(events.NewMessage(incoming=True, pattern="\\/auth (.*)"))
async def _(e):
    await addauth(e)


@bot.on(events.NewMessage(incoming=True, pattern="\\/remauth (.*)"))
async def _(e):
    await remauth(e)


@bot.on(events.NewMessage(incoming=True, pattern="\\/listauth$"))
async def _(e):
    await listauth(e)


LOGS.info("bot has started..")
bot.run_until_disconnected()
