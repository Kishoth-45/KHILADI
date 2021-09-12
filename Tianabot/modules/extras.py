import html
import random
import time

import Avangersbot.modules.fun_strings as fun_strings
import Avangersbot.modules.music_strings as music_strings
from Avangersbot import dispatcher
from Avangersbot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from Avangersbot.modules.helper_funcs.chat_status import is_user_admin
from Avangersbot.modules.helper_funcs.alternate import typing_action
from Avangersbot.modules.helper_funcs.filters import CustomFilters
from Avangersbot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async, CommandHandler, Filters

import Avangersbot.modules.helper_funcs.string_store as fun


@run_async
def sing(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.SING_STRINGS))


@run_async
def love(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.LOVE_STRINGS))


@run_async
def joke(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.JOKE_STRINGS))
    

@run_async
def cringe(update: Update, context: CallbackContext):
    reply_sticker = update.effective_message.reply_to_message.reply_sticker if update.effective_message.reply_to_message else update.effective_message.reply_sticker
    reply_sticker(random.choice(fun_strings.CRINGE))

@run_async
def cm(update: Update, context: CallbackContext):
    reply_audio = update.effective_message.reply_to_message.reply_audio if update.effective_message.reply_to_message else update.effective_message.reply_audio
    reply_audio(random.choice(fun_strings.COMEDY_MUSIC))  

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

SING_HANDLER = DisableAbleCommandHandler("sing", sing)
LOVE_HANDLER = DisableAbleCommandHandler("love", love)
JOKE_HANDLER = DisableAbleCommandHandler("joke", joke)
CRINGE_HANDLER = DisableAbleCommandHandler("cringe", cringe)
CM_HANDLER = DisableAbleCommandHandler("cm", cm)
LM_HANDLER = DisableAbleCommandHandler("lm", lm)
MASS_HANDLER = DisableAbleCommandHandler("mass", mass)
SAD_HANDLER = DisableAbleCommandHandler("sad", sad)


dispatcher.add_handler(SING_HANDLER)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(JOKE_HANDLER)
dispatcher.add_handler(CRINGE_HANDLER)
dispatcher.add_handler(CM_HANDLER)
dispatcher.add_handler(LM_HANDLER)
dispatcher.add_handler(MASS_HANDLER)
dispatcher.add_handler(SAD_HANDLER)

__mod_name__ = "FUN😍"
__command_list__ = [
    "sing",
    "love",
    "joke",
    "cringe",
    "cm",
    "lm",
    "mass",
    "sad",
]
__handlers__ = [
    SING_HANDLER,
    LOVE_HANDLER,
    JOKE_HANDLER,
    CRINGE_HANDLER,
    CM_HANDLER,
    LM_HANDLER,
    MASS_HANDLER,
    SAD_HANDLER,
]
