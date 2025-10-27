import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import *
from database import *
import os

logging.basicConfig(level=logging.INFO)
connect_db()

# Cek folder data
os.makedirs("data", exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍️ Lihat Produk", callback_data="produk")],
        [InlineKeyboardButton("💸 Cek Harga", callback_data="harga")],
        [InlineKeyboardButton("🧾 Cara Order", callback_data="order")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Selamat datang di *{SHOP_NAME}*!\nSilakan pilih menu:", parse_mode="Markdown", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "produk":
        await query.edit_message_text("📦 *Produk yang tersedia:*\n1️⃣ Paket A - Userbot Basic 1 Bulan\n💰 Harga: Rp15.000", parse_mode="Markdown")
    elif data == "harga":
        await query.edit_message_text("💰 *Daftar Harga:*\n- Paket A: Rp15.000", parse_mode="Markdown")
    elif data == "order":
        await query.edit_message_text("🧾 *Cara Order:*\n1️⃣ Pilih produk\n2️⃣ Kirim bukti pembayaran DANA ke 081219623569\n3️⃣ Tunggu verifikasi otomatis", parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    logging.info("Bot GarfieldOrderBot aktif...")
    app.run_polling()

if __name__ == "__main__":
    main()
