#created by @wich1

from .. import loader, utils
from asyncio import sleep

@loader.tds
class KorablMod(loader.Module):
	"""Мем (Капитан Залупа С Корабля Сбежал)"""
	strings = {'name': 'Korabl'}
	@loader.owner
	async def korablcmd(self, message_id):
	"""старт"""
		await utils.answer(message, "плыли мы по морю")
		await asyncio.sleep(3,5)
		await utils.answer(message, "ветер май штурвал")
		await asyncio.sleep(3,5)
		await utils.answer(message, "капитан залупа с корабля сбежал,")
		await asyncio.sleep(3,5)
		await utils.answer(message, "я стоял на вахте и держал весло")
		await asyncio.sleep(3,5)
		await utils.answer(message, "чем то уебало и меня снесло,")
		await asyncio.sleep(3,5)
		await utils.answer(message, "я плыву по морю и весь хуй промок,")
		await asyncio.sleep(3,5)
		await utils.answer(message, "пока ебался в жопу ")
		await asyncio.sleep(3,5)
		await utils.answer(message, "приплыли на какой то островок ")
		await asyncio.sleep(3,5)
		await utils.answer(message, "на острове нету не души ")
		await asyncio.sleep(3,5)
		await utils.answer(message, "хоть садись на камни и яйцо чеши")