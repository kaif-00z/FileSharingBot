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


from . import dB
from .config import Var

# ------------------Auth_User_db-------------------
if Var.OWNER_ID:
    auth = eval(dB.get("AUTH_USERS") or "[]")
    if Var.OWNER_ID not in auth:
        auth.append(Var.OWNER_ID)
        dB.set("AUTH_USERS", str(auth))


def get_auth():
    return eval(dB.get("AUTH_USERS") or "[]")


def is_auth(id):
    if id in eval(dB.get("AUTH_USERS") or "[]"):
        return True
    return False


def add_auth(id):
    auth = eval(dB.get("AUTH_USERS") or "[]")
    if id not in auth:
        auth.append(id)
        dB.set("AUTH_USERS", str(auth))


def rem_auth(id):
    auth = eval(dB.get("AUTH_USERS") or "[]")
    if id in auth:
        auth.remove(id)
        dB.set("AUTH_USERS", str(auth))


# ----------------------BoardCast_db-----------------


def add_user(id):
    board = eval(dB.get("BOARDCAST_USERS") or "[]")
    if id not in board:
        board.append(id)
        dB.set("BOARDCAST_USERS", str(board).replace(" ", ""))


def rem_user(id):
    board = eval(dB.get("BOARDCAST_USERS") or "[]")
    if id in board:
        board.remove(id)
        dB.set("BOARDCAST_USERS", str(board).replace(" ", ""))


def get_users():
    return eval(dB.get("BOARDCAST_USERS") or "[]")


# ------------------------STORE_DB------------------


def store_iteam(unique_id, id):
    _ = eval(dB.get("STORE") or "{}")
    _.update({unique_id: str(id)})
    dB.set("STORE", str(_))


def get_stored_iteam(unique_id):
    _ = eval(dB.get("STORE") or "{}")
    if _.get(unique_id):
        return eval(_[unique_id])
    return None


def del_stored_iteam(unique_id):
    _ = eval(dB.get("STORE") or "{}")
    if _.get(unique_id):
        _.pop(unique_id)
        dB.set("STORE", str(_))
