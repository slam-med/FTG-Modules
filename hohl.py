from .. import loader, utils
from asyncio import sleep
gif_url ="https://c.tenor.com/BS0X4mOtkRIAAAAd/%D1%85%D0%BE%D1%85%D0%BE%D0%BB-happy.gif"
@loader.tds
class HoholMod(loader.Module):
  async def hohlcmd(self, message):
    for _ in range(2):
      for sending in ['Отправка.','Отправка..','Отправка...']:
        await utils.answer(message,sending)
        await sleep(1)
      await utils.answer(message,"Ваш хохольчик")
      await message.client.sendVideo(message,gif_url)