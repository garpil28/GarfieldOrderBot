def get_desc(msg, name, price):
    desc = msg.text
    bot.send_message(msg.chat.id, "⚙️ Masukkan command akses (contoh: addprem3):")
    bot.register_next_step_handler(msg, save_new_product, name, price, desc)

def save_new_product(msg, name, price, desc):
    command = msg.text
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, description, access_command) VALUES (?, ?, ?, ?)",
                (name, price, desc, command))
    conn.commit()
    conn.close()
    bot.send_message(msg.chat.id, f"✅ Produk '{name}' berhasil ditambahkan!")
    bot.send_message(OWNER_ID, f"Produk baru ditambahkan:\n📦 {name}\n💰 Rp{price}\n⚙️ Command: {command}")

# === CEK STATUS ORDER === #
@bot.message_handler(func=lambda m: m.text == "📊 Order Status")
def order_status(msg):
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()
    cur.execute("SELECT o.id, p.name, o.status, o.timestamp FROM orders o JOIN products p ON o.product_id = p.id WHERE o.user_id=? ORDER BY o.id DESC", (msg.from_user.id,))
    orders = cur.fetchall()
    conn.close()
    if not orders:
        bot.send_message(msg.chat.id, "📭 Belum ada pesanan aktif.")
        return
    text = "📦 <b>Daftar Pesananmu:</b>\n\n"
    for o in orders:
        oid, pname, status, ts = o
        text += f"• {pname} — <b>{status}</b>\n   🕒 {ts}\n"
    bot.send_message(msg.chat.id, text)

print("🤖 GarfieldOrderBot berjalan...")
bot.infinity_polling()
