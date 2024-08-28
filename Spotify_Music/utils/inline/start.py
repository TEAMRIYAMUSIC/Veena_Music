from pyrogram.types import InlineKeyboardButton

import config
from Spotify_Music import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=" ʜᴇʟᴘ ", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text=" sᴇᴛ ", callback_data="settings_helper"
            ),
        ],
      [
             InlineKeyboardButton(text=" 🗑️ ", callback_data="close"),
    ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" ʜᴇʟᴘ ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text=" ꧁•⊹٭𝙺𝙾𝚄𝚂𝙷𝙰𝙻٭⊹•꧂ ", url=f"https://t.me/koushals84"),
            ],
                    [
                    InlineKeyboardButton(text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source"),
             InlineKeyboardButton(text=" 🗑️ ", callback_data="close"),
    ],
    ]
    return buttons
    
    
