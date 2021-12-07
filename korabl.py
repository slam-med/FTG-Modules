#created by @wich1

from .. import loader
from asyncio import sleep

@loader.tds
class KorablMod(loader.Module):
	"""Мем (Капитан Залупа С Корабля Сбежал)"""
	strings = {'name': 'Korabl'}
	@loader.owner
	async def korablcmd(self, message_id):
	"""старт"""
		await message_id.edit("плыли мы по морю")
		await asyncio.sleep(3,5)
		await message_id.edit("ветер май штурвал")
		await asyncio.sleep(3,5)
		await message_id.edit("капитан залупа с корабля сбежал,")
		await asyncio.sleep(3,5)
		await message_id.edit("я стоял на вахте и держал весло")
		await asyncio.sleep(3,5)
		await message_id.edit("чем то уебало и меня снесло,")
		await asyncio.sleep(3,5)
		await message_id.edit("я плыву по морю и весь хуй промок,")
		await asyncio.sleep(3,5)
		await message_id.edit("пока ебался в жопу ")
		await asyncio.sleep(3,5)
		await message_id.edit("приплыли на какой то островок ")
		await asyncio.sleep(3,5)
		await message_id.edit("на острове нету не души ")
		await asyncio.sleep(3,5)
		await message_id.edit("хоть садись на камни и яйцо чеши")