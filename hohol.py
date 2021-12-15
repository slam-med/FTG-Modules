#created by @wich1
#Hohol - seesonrise
from .. import loader, utils
from asyncio import sleep

hohol_url = "https://c.tenor.com/BS0X4mOtkRIAAAAd/%D1%85%D0%BE%D1%85%D0%BE%D0%BB-happy.gif"


@loader.tds
class HoholMod(loader.Module):
    """Hohol"""
    strings = {"name": "Hohol"}

    async def hoholcmd(self, message):
        """Использование: .hohol (user)"""
        
          await utils.answer(message, "Sending Hohol...")
          sleep(1)
        await message.client.send_video(message, hohol_url)
        await utils.answer(message, "Sent Hohol successfully!")
