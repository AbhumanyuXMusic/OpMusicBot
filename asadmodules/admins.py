# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks Â© @Dr_Asad_Ali Â© Rocks
# Owner Asad + Harshit
 

from cache.admins import admins
from rocksdriver.asad import call_py
from pyrogram import Client, filters
from rocksdriver.decorators import authorized_users_only
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, clear_queue
from rocksdriver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL, REPO_OWNER, BOT_UPDATE, MY_BRO, MY_SERVER, BOT_NAME, MY_HEART
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ð É¢á´ Êá´á´á´", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ð á´Êá´sá´", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(f"""**âââââââââââââââââââ
ð¥ Êá´ÊÊá´, Éª á´á´ á´ÊÉªsÊá´ á´ á´ á´Êá´Êá´Ê
Êá´á´ Òá´Ê á´á´Êá´É¢Êá´á´ É¢Êá´á´á´s.
âââââââââââââââââââ
â£â Êá´á´ : [Êá´Êá´á´á´á´á´](t.me/{BOT_USERNAME})
â£â á´á´á´ÉªÉ´ : á´á´ [{BOT_NAME}](t.me/{GROUP_SUPPORT}) Êá´ÒÊá´sÊá´á´
â£â sá´á´á´á´Êá´ : [Êá´á´ á´á´á´á´á´á´s](t.me/BOT_UPDATE)
âââââââââââââââââââ
ð¸ á´Ê Êá´á´Êá´ [Cá´É´á´Ê](t.me/{MY_HEART})
ð ÉªÒ Êá´á´ Êá´á´ á´ á´É´Ê Â» Ç«á´á´sá´Éªá´É´
á´Êá´É´ á´á´ á´á´ á´Ê [á´á´¡É´á´Ê](t.me/{REPO_OWNER})
âââââââââââââââââââ**""",
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("â **á´á´ [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) É´á´á´ÊÉªÉ´É¢ Éªs á´á´ÊÊá´É´á´ÊÊ á´Êá´ÊÉªÉ´É¢**")
        elif op == 1:
            await m.reply("â __Qá´á´á´á´s__ **Éªs á´á´á´á´Ê.**\n\n**â¢ ÒÊá´á´ [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) á´sá´ÊÊá´á´ Êá´á´á´ ÉªÉ´É¢ á´ á´Éªá´á´ á´Êá´á´**")
        elif op == 2:
            await m.reply("ðï¸ **CÊá´á´ÊÉªÉ´É¢ á´Êá´ Qá´á´á´á´s**\n\n**ÒÊá´á´ [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) á´sá´ÊÊá´á´ Êá´á´á´ ÉªÉ´É¢ á´ á´Éªá´á´ á´Êá´á´**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"â­ **sá´Éªá´á´á´á´ á´á´ É´á´xá´ á´Êá´á´á´.**\n\nð· **É´á´á´á´:** [{op[0]}]({op[1]})\n\nð¡ **sá´á´á´á´s:** `Playing`\nð§ **Êá´Ç«á´á´sá´ ÊÊ:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "ð **sá´É´É¢ Êá´á´á´á´ á´á´**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("â **ÒÊá´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **sá´Êá´á´á´ Êá´s á´É´á´á´á´**")
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **EÊÊá´Êr:**\n\n`{e}`")
    else:
        await m.reply("â **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **É´á´á´ÊÉªÉ´É¢ Éªs sá´Êá´á´á´ÉªÉ´É¢**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "â¸ **TÊá´á´á´á´ á´á´á´sá´á´.**\n\nâ¢ **Tá´ Êá´sá´á´á´ á´sá´ á´Êá´**\nÂ» /resume **á´á´á´á´á´É´á´**."
            )
        except Exception as e:
            await m.reply(f"ð« **EÊÊá´Ê:**\n\n`{e}`")
    else:
        await m.reply("â **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **É´á´á´ÊÉªÉ´É¢ Éªs sá´Êá´á´á´ÉªÉ´É¢**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "â¶ï¸ **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **TÊá´á´á´ Éªs Êá´sá´á´á´á´.**\n\nâ¢ **To pause the stream, use the**\nÂ» /pause command."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **Error:**\n\n`{e}`")
    else:
        await m.reply("â **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **É´á´á´ÊÉªÉ´É¢ Éªs sá´Êá´á´á´ÉªÉ´É¢**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "ð **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **á´sá´ÊÊá´á´ Éªs á´á´á´á´á´.**\n\nâ¢ **Tá´ á´É´á´á´á´á´ á´Êá´ á´sá´ÊÊá´á´, á´sá´ á´Êá´**\nÂ» /unmute **á´á´á´á´á´É´á´**."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **EÊÊá´Ê:**\n\n`{e}`")
    else:
        await m.reply("â **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **É´á´á´ÊÉªÉ´É¢ Éªs sá´Êá´á´á´ÉªÉ´É¢**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "ð **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **á´sá´ÊÊá´á´ Éªs á´É´á´á´á´á´á´.**\n\nâ¢ **á´á´ á´á´á´á´ á´Êá´ á´sá´ÊÊá´á´ á´sá´ á´Êá´**\nÂ» /mute **á´á´á´á´á´É´á´**."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"ð« **EÊÊá´Ê:**\n\n`{e}`")
    else:
        await m.reply("â **á´á´** [á´ÊÉªê±Êá´ sá´Êá´ á´Ê](t.me/{GROUP_SUPPORT}) **É´á´á´ÊÉªÉ´É¢ Éªs sá´Êá´á´á´ÉªÉ´É¢**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¢ðÊá´É´É´á´Ê", url=f"https://t.me/Pubglovers_shayri_lovers"),
                InlineKeyboardButton("â¢ðá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "â¸ the streaming has paused", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "â¶ï¸ the streaming has resumed", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("â **this streaming has ended**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "ð userbot succesfully muted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "ð á´sá´ÊÊá´á´ sá´á´á´á´sÒá´ÊÊÊ á´É´á´á´á´á´á´**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **á´ÊÊá´Ê:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("â **É´á´á´ÊÉªÉ´É¢ Éªs á´á´Êá´É´á´ÊÊ sá´Êá´á´á´ÉªÉ´É¢**", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"â **á´ á´Êá´á´á´ sá´á´ á´á´** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"ð« **á´ÊÊá´Ê:**\n\n`{e}`")
    else:
        await m.reply("â **É´á´á´ÊÉªÉ´É¢ Éªs sá´Êá´á´á´ÉªÉ´É¢**")
