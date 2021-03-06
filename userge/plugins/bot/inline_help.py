# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

"""Module that handles Inline Help"""

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from userge import Config, Message, userge

HELP_BUTTONS = None


COMMANDS = {
    "secret": {
        "help_txt": "**Send a secret message to a user**\n (only the entered user and you can view the message)\n\n>>>  `secret @username [text]`",
        "i_q": "secret @DeletedUser420 This is a secret message",
    },
    "alive": {
        "help_txt": "**Alive Command for PURPLE-X**\n\nHere You can view Uptime, Setting and Versions of your bot and when you change settings they are updated in Real-time UwU\n>>>  `alive`",
        "i_q": "alive",
    },
    "opinion": {
        "help_txt": "**Ask for opinion via inline**\n\nYou can now send multiple opinion messages at once\n**Note: **All button data is cleared as soon as you restart or update the bot\n>>>  `op [Question or Statement]`",
        "i_q": "op Are Cats Cute ?",
    },
    "repo": {
        "help_txt": "**Your PURPLE-X Github repo**\n\nwith direct deploy button\n>>>  `repo`",
        "i_q": "repo",
    },
    "gapps": {
        "help_txt": "**Lastest arm64 Gapps for <u>Android 10 Only !</u>**\n\nChoose from Niksgapps, Opengapps and Flamegapps\n>>>  `gapps`",
        "i_q": "gapps",
    },
    "ofox": {
        "help_txt": "**Lastest Ofox Recovery for supported device, Powered By offcial Ofox API v2**\n\n>>>  `ofox <device codename>`",
        "i_q": "ofox whyred",
    },
    "reddit": {
        "help_txt": '**Get Reddit Image post**\n\nGet Random Reddit meme or a post from specific subreddit, if you want post from specific subreddit do "reddit [subreddit]."\n>>> `reddit  or  reddit dankmemes.`',
        "i_q": "reddit nextfuckinglevel.",
    },
    "help": {
        "help_txt": "**Help For All Userbot plugins**\n\n**Note:** `You can also load and unload a plugin, and which chat types the commands is permitted`",
        "i_q": "",
    },
    "stylish": {
        "help_txt": "**Write it in Style**\n\nplugin to decorate text with unicode fonts.\n>>>  `stylish [text]`",
        "i_q": "stylish PURPLE-X",
    },
    "ytdl": {
        "help_txt": f"**Download YouTube Videos with Buttons**\n\nTo Download video from youtube with desired quality.\n>>>  `ytdl [link]` or `{Config.CMD_TRIGGER}iytdl`",
        "i_q": "ytdl https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    },
    "spoiler": {
        "help_txt": "**Send Saved Spoiler Via Inline**\n For more info see `.help spoiler`\n\n>>>  `spoiler [ID]`",
        "i_q": "spoiler",
    },
    "btn": {
        "help_txt": "**Get upto 15 of your most recently created inline messages in the inline query, so you can post it in any channel or group effortlessly**\n For Creating inline messages see `.help .ibutton`\n\n>>>  `btn`",
        "i_q": "btn",
    },
}


if userge.has_bot:

    def help_btn_generator():
        btn = []
        b = []
        for cmd in list(COMMANDS.keys()):
            name = cmd.capitalize()
            call_back = f"ihelp_{cmd}"
            b.append(InlineKeyboardButton(name, callback_data=call_back))
            if len(b) == 3:  # no. of columns
                btn.append(b)
                b = []
        if len(b) != 0:
            btn.append(b)  # buttons in the last row
        return btn

    if not HELP_BUTTONS:
        HELP_BUTTONS = help_btn_generator()

    BACK_BTN = InlineKeyboardButton(" ◀️  Back ", callback_data="backbtn_ihelp")

    inline_help_txt = " <u><b>INLINE COMMANDS</b></u>\n\nHere is a list of all available inline commands.\nChoose a command and for usage see:\n[ **📕  EXAMPLE** ]"

    @userge.bot.on_message(
        filters.user(list(Config.OWNER_ID))
        & filters.private
        & (filters.command("inline") | filters.regex(pattern=r"^/start inline$"))
    )
    async def inline_help(_, message: Message):
        await userge.bot.send_message(
            chat_id=message.chat.id,
            text=inline_help_txt,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTONS),
        )

    @userge.bot.on_callback_query(
        filters.user(list(Config.OWNER_ID)) & filters.regex(pattern=r"^backbtn_ihelp$")
    )
    async def back_btn(_, c_q: CallbackQuery):
        await c_q.edit_message_text(
            text=inline_help_txt, reply_markup=InlineKeyboardMarkup(HELP_BUTTONS)
        )

    @userge.bot.on_callback_query(
        filters.user(list(Config.OWNER_ID))
        & filters.regex(pattern=r"^ihelp_([a-zA-Z]+)$")
    )
    async def help_query(_, c_q: CallbackQuery):
        command_name = c_q.matches[0].group(1)
        msg = COMMANDS[command_name]["help_txt"]
        switch_i_q = COMMANDS[command_name]["i_q"]
        buttons = [
            [
                BACK_BTN,
                InlineKeyboardButton(
                    " 📕  EXAMPLE ", switch_inline_query_current_chat=switch_i_q
                ),
            ]
        ]
        await c_q.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(buttons))
