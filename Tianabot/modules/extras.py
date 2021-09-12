import html
import random
import time

import Tianabot.modules.music_strings as music_strings
from Tianabot import dispatcher
from Tianabot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from Tianabot.modules.helper_funcs.chat_status import is_user_admin
from Tianabot.modules.helper_funcs.alternate import typing_action
from Tianabot.modules.helper_funcs.filters import CustomFilters
from Tianabot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async, CommandHandler, Filters

import Tianabot.modules.helper_funcs.string_store as fun


@run_async
def lm(update: Update, context: CallbackContext):
    reply_audio = update.effective_message.reply_to_message.reply_audio if update.effective_message.reply_to_message else update.effective_message.reply_audio
    reply_audio(random.choice(music_strings.LOVEAUDIO))

@run_async
def mass(update: Update, context: CallbackContext):
    reply_audio = update.effective_message.reply_to_message.reply_audio if update.effective_message.reply_to_message else update.effective_message.reply_audio
    reply_audio(random.choice(music_strings.MASSAUDIO))

@run_async
def sad(update: Update, context: CallbackContext):
    reply_audio = update.effective_message.reply_to_message.reply_audio if update.effective_message.reply_to_message else update.effective_message.reply_audio
    reply_audio(random.choice(music_strings.SADAUDIO))

     
__help__ = """
 ❍ /sing*:* Tamil famous song some lyrics
 ❍ /love*:* Famous love diolougue and love quotes
 ❍ /joke*:* Kadi jokes in tamil language
 ❍ /cringe*:* upload a random cringe stickers
"""

LM_HANDLER = DisableAbleCommandHandler("lm", lm)
MASS_HANDLER = DisableAbleCommandHandler("mass", mass)
SAD_HANDLER = DisableAbleCommandHandler("sad", sad)


dispatcher.add_handler(LM_HANDLER)
dispatcher.add_handler(MASS_HANDLER)
dispatcher.add_handler(SAD_HANDLER)

__mod_name__ = "FUN😍"
__command_list__ = [
    "lm",
    "mass",
    "sad",
]
__handlers__ = [
    LM_HANDLER,
    MASS_HANDLER,
    SAD_HANDLER,
]
