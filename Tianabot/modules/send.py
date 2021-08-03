from pyrogram import filters

from Tianabot.function.pluginhelpers import admins_only, get_text
from Tianabot.services.pyrogram import pbot


@pbot.on_message(
    filters.command("snd") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def send(client, message):
    args = get_text(message)
    await client.send_message(message.chat.id, text=args)
