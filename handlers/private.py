
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
šš”š¢š¬ šš¬ šššÆšš§šš š„ššš„šš š«šš¦ šš®š¬š¢š š¶ ššØš­ \nšš®š§ šš§ šš«š¢šÆšš­š š„ šš©š¬ š«ššš«šÆšš« š \nšššš„ ā¤ļø šš¢š š” šš®šš„š¢š­š² šš®š¬š¢š š§ šš§ šš šš¤ \nā­šššÆšš„šØš©šš šš² [š²š¦š½š¼šæš šš²šš¼šæ](https://t.me/Its_Hexor)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā°š¢šš»š²šæā±", url="https://t.me/Sanki_Owner")
                  ],[
                    InlineKeyboardButton(
                        "ā°š¦šš½š½š¼šæššā±", url="https://t.me/eSport_BOTs"
                    ),
                    InlineKeyboardButton(
                        "ā°ššæš¼šš½š©ā±", url="https://t.me/EsportClan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ā°šš¼šŗšŗš®š±šš„ā±", url="https://telegra.ph/%EA%9C%B1%E1%B4%8D%E1%B4%8F%E1%B4%8B%E1%B4%87%CA%80-%E1%B4%8D%E1%B4%9C%EA%9C%B1%C9%AA%E1%B4%84-%CA%99%E1%B4%8F%E1%B4%9B-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85%EA%9C%B1-08-29"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ššš©šØš«š­ šš®š¬š¢š'š šš§š„š¢š§š\nš ššš©šØš«š­_šš© š„**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š¦šš½š½š¼šæšā¤ļø", url="https://t.me/eSport_BOTs")
                ]
            ]
        )
   )
