from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "USER_BOT_TOKEN_HERE"

app = Client("userbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("💰 Balance", callback_data="bal"),
         InlineKeyboardButton("🎁 Refer", callback_data="ref")],
        [InlineKeyboardButton("📤 Withdraw", callback_data="wd")]
    ])
    await message.reply("Welcome to your bot!", reply_markup=btn)

app.run()
