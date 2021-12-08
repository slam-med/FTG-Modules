from .. import loader, utils
from asyncio import sleep
@loader.tds
class LopataMod(loader.Module):
	"""На лопату в лицо"""
	asyns def lopatacmd (self , message):
		"""Лопату в лицо"""
		strings = {'name'='Обычная лопата'}
		await utils.answer(message,"лопату заказывали")
		await sleep(1)
		await utils.answer(message,"Нет?")
		await sleep(1)
		await utils.answer(message,"Ну ладно :(")
