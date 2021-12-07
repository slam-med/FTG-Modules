#created by @wich1

from .. import loader
from asyncio import sleep


@loader.tds
class GazetaMod(loader.Module):
	"""Мем (Китайская газета)"""
	strings = {'name': 'Gazeta'}
	@loader.owner
	async def gazetacmd(self, message_id):
		await message_id.edit(" Китайская газета -Хуй вам, хуй нам- ")
		await asyncio.sleep(4)
		await message_id.edit(" сообщает - что Француский король ")
		await asyncio.sleep(4)
		await message_id.edit(" Трипер второй выдаёт свою дочь, Ля Курву Дэ Бля Ве ")
		await asyncio.sleep(4)
		await message_id.edit(" замуж за французского подданого Дон-Дон Штопаный Гандон. ")
		await asyncio.sleep(4)
		await message_id.edit(" На пир были приглашены ")
		await asyncio.sleep(4)
		await message_id.edit(" с Румынской стороны Залупыська, ")
		await asyncio.sleep(4)
		await message_id.edit(" с русской Иван-Пиздарван, ")
		await asyncio.sleep(4)
		await message_id.edit(" с грузинской Целкаламидзе, ")
		await asyncio.sleep(4)
		await message_id.edit(" с китайской Сунь Хуй в Чай? ")
		await asyncio.sleep(4)
		await message_id.edit(" Вынь Сухим и дай подержать другим. ")
		await asyncio.sleep(4)
		await message_id.edit(" На обед были поданы - супы горячие, хуи стаоячие. ")
		await asyncio.sleep(4)
		await message_id.edit(" После обеда был просмотр фильма ")
		await asyncio.sleep(4)
		await message_id.edit(" -Не одна я в поле кувыркалась, не одной мне ветер в жопу дул-. ")
		await asyncio.sleep(4)
		await message_id.edit(" После этого был показ спектакля ")
		await asyncio.sleep(4)
		await message_id.edit(" -Как батька Махно выставил жопу в окно-. ")
		await asyncio.sleep(4)
		await message_id.edit(" И после этого была пропета украиньска народна письня ")
		await asyncio.sleep(4)
		await message_id.edit(" -Ох, да залупылась на хую шкурынка- ")
		await asyncio.sleep(4)
		await message_id.edit(" Сегоднешняя газета зкончилась ")#пасхалочка