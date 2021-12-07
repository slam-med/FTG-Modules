#created users seesonrise

from .. import loader
from asyncio import sleep
import os

@loader.tds
class MotchaMod(loader.Module):
	"""Рукоблуд, ссанина"""
	strings = {"name": "Рукоблуд"}
	@loader.owner
	async def рукоблудcmd(self, message):
		"""Начнем"""
		await message.edit("Да ты...................")
		await sleep(0.3)
		for _ in range(10):
			for droch in ['Говно', 'залупа', 'пенис', 'хер', 'давалка', 'хуй', 'блядина', 
				      'Головка','шлюха','жопа','член','еблан','петух...','мудила',
				      'Рукоблуд','ссанина','очко','блядун','вагина',
				      'Сука','ебланище','влагалище','пердун','дрочила',
				      'Пидор','пизда','туз','малафья',
				      'Гомик','мудила','пилотка','манда',
				      'Анус','вагина','путана','елда...',
				      'Шалава','хуила','мошонка','Головка',]:
				await message.edit(droch)
				await sleep(0.3)
