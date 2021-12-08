import .. from loader, utils
from asyncio import sleep
@loader.tds
class PremMod(loader.Module):
  strings ={'name':'Test Premium')
  @loader.owner
  async def premcmd (self,message):
    if message == "e1cf2286":
      await utils.answer(message,"Вроде робит")