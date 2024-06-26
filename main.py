from pyrogram import Client, types, filters
from pyrogram.enums import ChatType
import time


api_id = ""
api_hash = ""

text = 'text'

chat_ids = [-1001917608732]

client = Client(name='name', api_id=api_id, api_hash=api_hash)


async def main():
    async with client:
        async for dialog in client.get_dialogs():
            if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                for chat_id in chat_ids:
                    await client.send_message(chat_id=chat_id, text=text)
                    print('сообщение отправлено')
                    time.sleep(30)# настраивай время


client.run(main())
