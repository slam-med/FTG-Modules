#created by @wich1
#Hohol - seesonrise
from .. import loader, utils

hohol_url = "https://c.tenor.com/BS0X4mOtkRIAAAAd/%D1%85%D0%BE%D1%85%D0%BE%D0%BB-happy.gif"


@loader.tds
class HoholMod(loader.Module):
    """Hohol"""
    strings = {"name": "Hohol"}

    async def hoholcmd(self, message):
        """Usage: .hohol (user)"""
        target = await self.get_target(message)
        if not target:
            return await message.edit("<b>Please specify who to hohol.</b>")

        msg = await utils.answer(message, "<b>Sending Hohol...</b>")
        await message.client.send_vide(target, hohol_url)
        await utils.answer(msg, "<b>Sent Hohol successfully!</b>")

    @staticmethod
    async def get_target(message):
        if message.chat_id > 0:
            return await message.client.get_entity(message.chat_id)
        args = utils.get_args_raw(message)
        if args:
            args = args.split()[0]
        reply = await message.get_reply_message()

        if not args and not reply:
            return None
        if reply and reply.from_id:
            return reply.from_id

        user = args if not args.isnumeric() else int(args)
        return await message.client.get_entity(user)
