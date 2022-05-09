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
from .admin import *
from .boardcast import *
from .database import del_stored_iteam, get_stored_iteam, store_iteam


async def gen_link(event):
    X = []
    async with event.client.conversation(event.sender_id) as cv:
        await cv.send_message(
            "`Now send me Files/Messages one by one. After Sending All the Files/Message do `/done` .If you want to Cancel the Process do `/cancel` .`"
        )
        while True:
            x = await cv.get_response(timeout=60)
            if x.text.startswith("/cancel"):
                return await x.reply("`Process Cancelled Successfully`")
            elif x.text.startswith("/done"):
                break
            fwd = await x.forward_to(Var.STORAGE_CHANNEL)
            X.append(fwd.id)
            await x.reply("`Added`")
    u_id = secrets.token_hex(nbytes=16).replace("=", "")
    store_iteam(u_id, X)
    link = f"https://t.me/{((await event.client.get_me()).username)}?start={u_id}"
    await event.reply(
        f"**Successfully Added All Files, Shareable link is** {link}",
        link_preview=False,
    )


async def get_iteams(event, _u_id):
    lol = get_stored_iteam(_u_id)
    if not lol:
        return
    try:
        for x in lol:
            msg = await event.client.get_messages(Var.STORAGE_CHANNEL, ids=x)
            await event.client.send_message(event.sender_id, msg)
            await asyncio.sleep(0.5)
    except Exception as e:
        LOGS.info(str(e))
        return await event.reply(f"`Messages/Files not Found!`")


async def revoke_link(e, _u_id):
    lol = get_stored_iteam(_u_id)
    if lol:
        del_stored_iteam(_u_id)
        await e.reply("`Successfully Revoked the link`")
    else:
        await e.reply("`Link is already deleted`")
