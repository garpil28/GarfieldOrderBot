import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load token dari .env
load_dotenv()
TOKEN = os.getenv("7978577832:AAHAHagcPe5Rigx-6qlE2u339i8zUzMgSlg")

# Fungsi start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot sudah aktif di VPS ✅")

# Buat bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot berjalan...")

# Jalankan bot
app.run_polling()
