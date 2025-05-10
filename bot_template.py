from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 24202621
API_HASH = "55ad49020e800a10d9f41536269c3d3e"
BOT_TOKEN = "8083857067:AAG7VMkfR61XSyEXV8hHX69H19LYbIQQ014"

app = Client("userbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("💰 Balance", callback_data="bal"),
         InlineKeyboardButton("🎁 Refer", callback_data="ref")],
        [InlineKeyboardButton("📤 Withdraw", callback_data="wd")]
    ])
    await message.reply("Welcome to auto pay bot!", reply_markup=btn)

app.run()
