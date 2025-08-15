from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import time

# Ваши данные (Зайдите на my.telegram.org)
api_id =   # Замените на ваш API ID
api_hash = ''  # Замените на ваш API Hash
phone = '+79999999909'  # Ваш номер телефона Telegram

# Ограничение частоты ответов (cooldown 1 минута)
last_reply_time = {}

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    # Проверяем, содержит ли сообщение "!помощь" или "!инфо"
    if '!помощь' in event.raw_text.lower():
        chat = await event.get_chat()
        sender = await event.get_sender()
        current_time = time.time()

        # Проверяем, был ли недавно ответ (cooldown 1 минута)
        if chat.id in last_reply_time and (current_time - last_reply_time[chat.id]) < 60:
            return

        # Если это личное сообщение
        if isinstance(event.peer_id, PeerUser):
            await event.reply("Зову на помощь!")
            last_reply_time[chat.id] = current_time
        # Если это группа/канал
        else:
            await event.reply("Пожалуйста, напишите в личных сообщениях.")
            last_reply_time[chat.id] = current_time

    # Обработка команды !инфо
    elif '!инфо' in event.raw_text.lower():
        info_text = (
            "**AutoMessage v.1.30**\n"
            "AutoMessage - Авто сообщение от разработчика **sergaytrain**, узнать мои соц-сети - !Соц-Сети.\n\n"
            "© AutoMessage 2025, [https://automsg.tfpproj.ru/](https://automsg.tfpproj.ru/)"
        )
        await event.reply(info_text, link_preview=False)

client.start(phone)
client.run_until_disconnected()
