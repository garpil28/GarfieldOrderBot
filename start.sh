async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍️ Lihat Produk", callback_data="produk")],
        [InlineKeyboardButton("💸 Cek Harga", callback_data="harga")],
        [InlineKeyboardButton("💳 Metode Pembayaran", callback_data="payment")],
        [InlineKeyboardButton("🧾 Cara Order", callback_data="order")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Selamat datang di *{SHOP_NAME}*!\nSilakan pilih menu:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )
