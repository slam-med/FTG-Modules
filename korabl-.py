from .. import loader
from asyncio import sleep

@loader.tds
class KorablMod(loader.Module):
	"""Мем (Капитан Залупа С Корабля Сбежал)"""
	strings = {'name': 'Korabl'}
	@loader.owner
	async def korablcmd(self,message_id):
		await message_id.edit("плыли мы по морю")
		await sleep(3,5)
		await message_id.edit("ветер май штурвал")
		await sleep(3,5)
		await message_id.edit("капитан залупа с корабля сбежал,")
		await sleep(3,5)
		await message_id.edit("я стоял на вахте и держал весло")
		await sleep(3,5)
		await message_id.edit("чем то уебало и меня снесло,")
		await sleep(3,5)
		await message_id.edit("я плыву по морю и весь хуй промок,")
		await sleep(3,5)
		await message_id.edit("пока ебался в жопу ")
		await sleep(3,5)
		await message_id.edit("приплыли на какой то островок ")
		await sleep(3,5)
		await message_id.edit("на острове нету не души ")
		await sleep(3,5)
		await message_id.edit("хоть садись на камни и яйцо чеши")