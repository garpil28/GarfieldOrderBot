import sqlite3
import os

os.makedirs("data", exist_ok=True)

def connect_db():
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS owners (
        user_id INTEGER PRIMARY KEY,
        shop_name TEXT,
        payment_method TEXT,
        payment_account TEXT,
        Payment_qris
        payment_name TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER,
        name TEXT,
        price INTEGER,
        description TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buyer_id INTEGER,
        owner_id INTEGER,
        product_id INTEGER,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    conn.commit()
    conn.close()

def add_owner(user_id, shop_name, payment_method, payment_account, payment_qr, payment_name):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO owners VALUES (?, ?, ?, ?, ?)",
                   (user_id, shop_name, payment_method, payment_account,payment_qr, payment_name))
    conn.commit()
    conn.close()
