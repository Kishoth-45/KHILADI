import asyncio

from pyrogram import filters

from Tianabot import BOT_ID, BOT_NAME, sudo_plus, app
from Tianabot.core.decorators.errors import capture_err
from Tianabot.modules import ALL_MODULES
from Tianabot.utils.dbfunctions import (get_blacklist_filters_count,
                                   get_filters_count, get_gbans_count,
                                   get_karmas_count, get_notes_count,
                                   get_served_chats, get_served_users,
                                   get_warns_count, remove_served_chat)
from Tianabot.utils.fetch import fetch
from Tianabot.utils.inlinefuncs import keywords_list

""" CHAT WATCHER IS IN filters.py"""


@app.on_message(
    filters.command("gstats") & filters.user(sudo_plus) & ~filters.edited
)
@capture_err
async def global_stats(_, message):
    m = await app.send_message(
        message.chat.id,
        text="__**Analysing Stats**__",
        disable_web_page_preview=True,
    )

    # For bot served chat and users count
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    await m.edit(
        f"__**Generating Statistics Report, Should Take {len(served_chats)*2}+ Seconds.**__",
        disable_web_page_preview=True,
    )
    for served_chat in served_chats:
        try:
            await app.get_chat_members(served_chat, BOT_ID)
            await asyncio.sleep(2)
        except Exception:
            await remove_served_chat(served_chat)
            served_chats.remove(served_chat)
            pass
    served_users = await get_served_users()
    # Gbans count
    gbans = await get_gbans_count()
    _notes = await get_notes_count()
    notes_count = _notes["notes_count"]
    notes_chats_count = _notes["chats_count"]

    # Filters count across chats
    _filters = await get_filters_count()
    filters_count = _filters["filters_count"]
    filters_chats_count = _filters["chats_count"]

    # Blacklisted filters count across chats
    _filters = await get_blacklist_filters_count()
    blacklist_filters_count = _filters["filters_count"]
    blacklist_filters_chats_count = _filters["chats_count"]

    # Warns count across chats
    _warns = await get_warns_count()
    warns_count = _warns["warns_count"]
    warns_chats_count = _warns["chats_count"]

    # Karmas count across chats
    _karmas = await get_karmas_count()
    karmas_count = _karmas["karmas_count"]
    karmas_chats_count = _karmas["chats_count"]

    # Contributors/Developers count and commits on github
    url = "https://api.github.com/repos/Kishoth-45/KHILADI/contributors"
    rurl = "https://github.com/Kishoth-45/KHILADI"
    developers = await fetch(url)
    commits = 0
    for developer in developers:
        commits += developer["contributions"]
    developers = len(developers)
    # Modules info
    modules_count = len(ALL_MODULES)

    msg = f"""
**Global Stats of {BOT_NAME}**:
**{modules_count}** Modules Loaded
**{len(keywords_list)}** Inline Modules Loaded.
**{gbans}** Globally banned users.
**{filters_count}** Filters, Across **{filters_chats_count}** chats.
**{blacklist_filters_count}** Blacklist Filters, Across **{blacklist_filters_chats_count}** chats.
**{notes_count}** Notes, Across **{notes_chats_count}** chats.
**{warns_count}** Warns, Across **{warns_chats_count}** chats.
**{karmas_count}** Karma, Across **{karmas_chats_count}** chats.
**{len(served_users)}** Users, Across **{len(served_chats)}** chats.
**{developers}** Developers And **{commits}** Commits On **[Github]({rurl})**.
"""
    await m.edit(msg, disable_web_page_preview=True)
