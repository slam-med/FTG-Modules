#created by @wich
# v1.0

from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.wg(?: |$)(.*)')
async def typewriter(typew):
    await message("1")
    sleep(4)
    await message("2")
