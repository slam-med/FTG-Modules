#Create users seesonrise for @wich1
#My github github.com/seesonrise
#Github @wich1 github.com/wich1
#This module has a Copyright please do not copy this code


from .. import loader
from asyncio import sleep
import random

@loader.tds
class HentaiMod(loader.Module):
	"""Дает рандомную ссылку на nhetai"""
	strings = {'name': 'Hentai Module'}
	@loader.owner
	async def nhcmd(self,message_id):
		"""Начать поиск"""
		await message_id.edit("Поиск хентыча")
		await asyncio.sleep(1)
		for _ in range(3):
			for search in ['Поиск.','Поиск..','Поиск...']:
				await message_id.edit(search)
				await asyncio.sleep(1) 
		await asyncio.sleep(1) 
		await message_id.edit("Ваш хентай")
		await asyncio.sleep(1)
		x = random.randint(1,383041)
		await message_id.edit("nhentai.net/g/"+ str(x))
