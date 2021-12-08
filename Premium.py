from .. import loader, utils

@loader.tds
class PremMod(loader.Module):
  """ Тест роботы проверки лицензии"""
  
  strings ={'name':'Test Premium'}
  
  @loader.owner
  async def premcmd (self,message):
    """ Проверка лицензии"""
    if message == gopabobra:
      await utils.answer(message," Лицензия робит")
    else
      await utils.answer(message, "Ярик всё хуйня")