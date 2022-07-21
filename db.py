#Created by @xD_Comrade

from motor.motor_asyncio import AsyncIOMotorClient as MG

mongoc = MG("Your MongoDB here")
db = mongoc.Crypto

msgdb = db.Messages

async def is_msg():
    check = await msgdb.find({"message"})
    if check:
        return True
    return False

async def insert_msg(msg: str):
        prev_msg = await get_msg()
        if not prev_msg:
            return await msgdb.insert_one({"message": msg})
        
        return await msgdb.find_one_and_update(
            {"id": 1}, {"$set": {"message": msg}},
            upsert=True
        )

async def delete_msg():
    await msgdb.delete_one({"message"})

async def get_msg():
    msg_list = []
    msgs = msgdb.find({})
    [msg_list.append(i) async for i in msgs]
    for x in msg_list:
        msg = x["message"]
    if not msg:
        return None
    return msg