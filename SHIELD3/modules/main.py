from pyrogram import Client, filters
import os
from pyrogram.types import *
from pyrogram import filters

import time
import random
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from SHIELD3 import SHIELD3 as app

import pyrogram
from pyrogram.errors import FloodWait


NYKAA = [
    "https://graph.org/file/9bba2b7ee9ba3806de65d.jpg",
    "https://graph.org/file/ef82f289043a4fa74f8ff.jpg",
    "https://graph.org/file/9c27c68958e06ae074c38.jpg",
    "https://graph.org/file/0ff325b1d2efe80299aa3.jpg",
    "https://graph.org/file/41167b953cf3579853d47.jpg",
    "https://graph.org/file/bd93ab42e69305f274028.jpg",
    "https://graph.org/file/97575db5586c05d6b2898.jpg",
    "https://graph.org/file/07c393fdf931a407c9bc0.jpg",
    "https://graph.org/file/f332767490ad3a5ca20e8.jpg",
    "https://graph.org/file/f3449e9069667f647d14e.jpg",
    "https://graph.org/file/9f51cdc739f907cbd2c7e.jpg",
    "https://telegra.ph/file/d7a6a923c38e051ce35f3.jpg",
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
    "https://graph.org/file/37248e7bdff70c662a702.jpg",
    "https://graph.org/file/0bfe29d15e918917d1305.jpg",
    "https://graph.org/file/16b1a2828cc507f8048bd.jpg",
    "https://graph.org/file/e6b01f23f2871e128dad8.jpg",
    "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
    "https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
    "https://graph.org/file/39d7277189360d2c85b62.jpg",
    "https://graph.org/file/5846b9214eaf12c3ed100.jpg",
    "https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
    "https://graph.org/file/3514efaabe774e4f181f2.jpg",    
]


start_txt = """<b> ❍ ʜɪɪ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n━━━━━━━━━━━━━━━━━━━━━━\n\n❍ ɪ ᴀᴍ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ.\n\n❍ ɪ ʜᴀᴠᴇ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ғᴇᴀᴛᴜʀᴇs.\n\n❍ ᴘᴏᴡᴇʀᴇᴅ 𝐀мяιт 𝐑ɑʝ  ࿐ </b>"""

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="nykaa_back"),
          InlineKeyboardButton("ʜᴇʟᴘ", callback_data="roy_back")
        ],
        [
          InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data="gib_source"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(random.choice(NYKAA), caption=start_txt,reply_markup=reply_markup
    )

# ------------------------------------------------------------------------------- #


gd_buttons = [              
        [
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/AMRIT_X_SUPPORT"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AMRIT_X_SUPPORTS"),    
        ]
        ]
# ------------------------------------------------------------------------------- #

ROY_BTN = [              
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AMRIT_X_SUPPORTS"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/AMRIT_X_SUPPORT"),    
        ]
]
# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("cuteback"))
async def cutebackbutton(client, callback_query: CallbackQuery, _):  
    try:
        startkeyboard = [
            [ 
              InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
              InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="nykaa_back"),
              InlineKeyboardButton("ʜᴇʟᴘ", callback_data="roy_back")
            ],
            [
              InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data="gib_source"),
            ]
        ]
        await callback_query.message.edit_caption(start_txt,  
                reply_markup=InlineKeyboardMarkup(startkeyboard)
                )
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        await callback_query.message.reply_text(error_message)

    

@app.on_callback_query(filters.regex("nykaa_back"))
async def nykaa_back(_, query: CallbackQuery):
    await query.message.edit_caption(ABOUT_STRING,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


ABOUT_STRING = """**✦ ɪ ʜᴀᴠᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ғᴇᴀᴛᴜʀᴇs.\n\n❍ ɴᴏ ᴘᴏʀɴᴏɢʀᴀᴘʜʏ \n❍ ɴᴏ ᴍᴇssᴀɢᴇ ᴇᴅɪᴛ\n❍ ɴᴏ ᴘᴅғ ғɪʟᴇ sʜᴀʀᴇ\n❍ ɴᴏ ʟᴏɴɢ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ\n❍ ɴᴏ sᴘᴀᴍᴍᴇʀ ʀᴇᴘᴏʀᴛs\n❍ ɴᴏ ɴᴄᴇʀᴛ ᴄᴏɴᴛᴇsᴛ\n\n✦ ᴀɴᴅ ᴍᴏʀᴇ ᴄᴏɴᴛᴇsᴛs ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ, ғᴜʟʟ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ.**"""


# -------------------------------------------------------------------------------------

HELP_STRING = """**✽ ᴏᴡɴᴇʀ/sᴜᴅᴏ ᴜsᴇʀ ᴄᴍᴅs ⏤͟͟͞͞★\n\n❍ /bcast ➠ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴʏ ᴍᴇssᴀɢᴇ.\n❍ /announce ➠ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀɴɴᴏᴜɴᴄᴇ.\n\n✽ ᴀʟʟ ᴜsᴇʀs  ᴄᴏᴍᴍᴀɴᴅs ⏤͟͟͞͞★\n\n❍ /start ➠ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.\n❍ /ping ➠ ᴄʜᴋ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛs.\n❍ /repo ➠ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ.\n\n❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠  ʀ𝐀мяιт 𝐑ɑʝ  ࿐**"""

# ------------------------------------------------------------------------------- #

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
]

# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("roy_back"))
async def roy_back(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_STRING,
                                    reply_markup=InlineKeyboardMarkup(ROY_BTN),)

# ------------------------------------------------------------------------------- #
REPO_STRING = """**
❍ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ...

❍ ɪ ᴀᴍ ᴄᴏᴘʏʀɪɢʜᴛ sʜɪᴇʟᴅ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʙᴏᴛ.

❍ ɪғ ʏᴏᴜ ᴡᴀɴᴛ **ᴄᴏᴘʏʀɪɢʜᴛ sʜɪᴇʟᴅ** ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.**
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    REPO_BTN = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AMRIT_X_SUPPORTS"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/telegrambot622/COPYRIGHT_AMRIT-"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(REPO_BTN)
    
    await msg.reply_photo(photo="https://telegra.ph/file/1af24255ebc2ea08cd0b9.jpg", caption=REPO_STRING,reply_markup=reply_markup
                         )



# ------------------------------------------------------------------------------- #

start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"


# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"✦ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛs ✦\n\n"
        f"❅ ᴜᴘᴛɪᴍᴇ ➠ {uptime}\n"
        f"❅ ᴄᴘᴜ ➠ {cpu}%\n"
        f"❅ ᴛᴏᴛᴇʟ ꜱᴛᴏʀᴀɢᴇ ➠ {size_formatter(storage.total)}\n"
        f"❅ ᴜsᴇᴅ ➠ {size_formatter(storage.used)}\n"
        f"❅ ғʀᴇᴇ ➠ {size_formatter(storage.free)}\n"
        f"❅ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➠ {python_version}\n\n"
        f"✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠  ʀ ᴏ ʏ - ᴇ ᴅ ɪ ᴛ x ࿐"
    )

    await message.reply(reply_text, reply_markup=InlineKeyboardMarkup(EVAA), quote=True)

# -------------------------------------------------------------------------------------

FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"✦ ᴅᴇʟᴇᴛɪɴɢ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ɪᴅ {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"✦ ʜᴇʏ {user_mention}, ʙᴀʙʏ ᴅᴏɴ'ᴛ sᴇɴᴅ ɴᴇxᴛ ᴛɪᴍᴇ.")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"✦ ᴅᴇʟᴇᴛɪɴɢ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ɪᴅ {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"✦ ʜᴇʏ {user_mention}, ʙᴀʙʏ ᴅᴏɴ'ᴛ sᴇɴᴅ, ɴᴇxᴛ ᴛɪᴍᴇ.")
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 200

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"✦ ʜᴇʏ {user_mention} ʙᴀʙʏ, ᴘʟᴇᴀsᴇ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ sʜᴏʀᴛ.")
    

# -----------------------------------------------------------------------------------


    
#@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
#async def keep_reaction_message(client, message: Message):
  #  pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"✦ ʜᴇʏ {user_mention} ᴅᴏɴ'ᴛ sᴇɴᴅ ᴘᴅғ ғɪʟᴇs ʙᴀʙʏ, ғᴏʀ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʟɪᴍʙ."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# ----------------------------------------

@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/9235d57807362b4e227a3.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [close_button]
            ]
        ),
        )
close_button = InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")

@app.on_callback_query(filters.regex("close"))
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return
        
