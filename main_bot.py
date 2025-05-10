from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import API_ID, API_HASH, BOT_TOKEN
from database import save_user_bot
from deployer import deploy_user_bot

app = Client("MainBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("🆕 Create New Bot", callback_data="create_bot")]])
    await message.reply("Welcome to Bot Maker!", reply_markup=btn)

@app.on_callback_query(filters.regex("create_bot"))
async def ask_token(_, callback_query):
    await callback_query.message.reply("Send me your **Bot Token** to create your bot.")
    await callback_query.answer()
    app.set_parse_mode("markdown")

@app.on_message(filters.private & ~filters.command("start"))
async def receive_token(client, message):
    token = message.text.strip()
    user_id = message.from_user.id
    success = await deploy_user_bot(user_id, token)
    if success:
        save_user_bot(user_id, token)
        await message.reply("✅ Your bot is deployed and ready!")
    else:
        await message.reply("❌ Invalid or broken bot token.")

app.run()
