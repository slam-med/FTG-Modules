from .. import loader, utils

@loader.tds
class PremMod(loader.Module):
  
  strings ={'name':'Test Premium'}
  
  @loader.owner
  async def premcmd (self,message):
    """ Проверка лицензии"""
    if message == gopabobra:
      await utils.answer(message," Лицензия робит")
    elif
      await utils.answer(message, "Ярик всё хуйня")