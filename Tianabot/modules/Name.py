
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types

from Tianabot.events import register as Tianabot




@Tianabot(pattern="^/namehistory ?(.*)")
async def _(event):

    if event.fwd_from:

        return

    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        else:
            return
    if not event.reply_to_msg_id:

        await event.reply("```Reply to any user message.```")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.reply("```reply to text message```")

        return

    chat = "@DetectiveInfoBot"
    uid = reply_message.sender_id
    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    lol = await event.reply("```Processing```")

    async with ubot.conversation(chat) as conv:

        try:

            # response = conv.wait_event(
            #   events.NewMessage(incoming=True, from_users=1706537835)
            # )

            await silently_send_message(conv, f"/detect_id {uid}")

            # response = await response
            responses = await silently_send_message(conv, f"/detect_id {uid}")
        except YouBlockedUserError:

            await event.reply("```Please unblock @DetectiveInfoBot and try again```")

            return
        await lol.edit(f"{responses.text}")
        # await lol.edit(f"{response.message.message}")
