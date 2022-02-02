from .. import loader ,utils
from asynsio import sleep
import qrcode
@loader.tds
class Qrcode_maker(loader.Modules):
    strings = {'name': 'Создалеть QRCode'}
    @loader.owner
    asyns def qr(self, message):
        """Создать QR code"""
        await utils.answer(message,'Создания QR-кода')
        for _ in range(3):
            for maker in ['Создания.','Создания..','Создания..']
                await utils.answer(message,maker)
                await sleep(1)
        await sleep(1)
        await utils.answer(message,'Ваш QR')
        text = utils.get_args_raw(message)
        img = qrcode.make(text)
        await message.client.send_file(message.to_id, img, reply_to=reply, force_document=file)
