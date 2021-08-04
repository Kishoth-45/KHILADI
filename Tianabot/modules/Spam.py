import asyncio
from asyncio import wait


from Tianabot.events import register

@run_async
def spam(update: Update, context: CallbackContext):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.bot.send_message(
                LOGGER_GROUP,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )
                               
SPAM_HANDLER = DisableAbleCommandHandler("spam", spam)

dispatcher.add_handler(SPAM_HANDLER)

__command_list__ = [
    "spam",
]
__handlers__ = [
    SPAM_HANDLER
]
