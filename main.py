async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        "💳 *Metode Pembayaran:*\n\n"
        f"🏧 *DANA:* {DEFAULT_PAYMENT['dana']} (a/n {DEFAULT_PAYMENT['name']})\n"
        f"📱 *QRIS:* [Klik di sini untuk QRIS]({DEFAULT_PAYMENT['qris']})",
        parse_mode="Markdown",
        disable_web_page_preview=False
    )
    write_log(f"{user.id} membuka menu /payment.")

# =====================================
# COMMAND /logs (khusus owner)
# =====================================
async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("❌ Kamu tidak punya izin melihat log.")
        return

    if not os.path.exists(LOG_FILE):
        await update.message.reply_text("📂 Belum ada log order yang tercatat.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        log_content = f.read()[-4000:]  # kirim 4000 karakter terakhir agar tidak terlalu panjang

    await update.message.reply_text(
        f"📜 *Log Order Terbaru:*\n\n`\n{log_content}\n```",
        parse_mode="Markdown"
    )

# =====================================
# MAIN
# =====================================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("payment", payment))
    app.add_handler(CommandHandler("logs", logs))
    app.add_handler(CallbackQueryHandler(button))

    logging.info("🚀 GarfieldOrderBot aktif dengan sistem log order.")
    app.run_polling()

if name == "main":
    main()
