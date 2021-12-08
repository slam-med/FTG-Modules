from .. import loader, utils
from asyncio import sleep
@loader.tds
class LopataMod(loader.Module):
	"""На лопату в лицо"""
	strings = {'name':'Обычная лопата'}
	async def lopatacmd (self,message):
		"""Лопату заказывали?"""
		await utils.answer(message,"Лопату заказывали")
		await sleep(1)
		await utils.answer(message,"Нет?")
		await sleep(1)
		await utils.answer(message,"Ну ладно :(")
		await sleep(1)
		await utils.answer(message,"Может вы всё таки заказывали?")
	async def lopata_memecmd (self,message):
		"""Мемная лопата"""
		for _ in range(1):
			for lopata in [
		'-Где лопата?',
		'-Я не знаю.',
		'-Кто за лопату отвечает?',
		'-Не я, я сказал...',
		'-А кто отвечает?Лопата была у тебя в руках!',
		'-Я её воткнул в кучу.',
		'-Рот закрой!',
		'-А ты не пизди.',
		'*Шлепок*',
		'-Ты ахуел?!',
		'-Ты чё меня бьёшь?!',
		'-Куда ты лезешь, Вась?!',
		'-Слушай Вась, слушай теперь меня!Где лопата?',
		'-Я не знаю!',
		'-Кто ответственный?Иди ищи лопату!',
		'-...',
		'-Сам иди ищи, понял! Пидор!',]:
				await utils.answer(message,lopata)
				await sleep(1)

