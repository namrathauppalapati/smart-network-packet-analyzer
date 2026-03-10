import sqlite3

DB_NAME = "packets.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS packets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        src_ip TEXT,
        dst_ip TEXT,
        protocol TEXT,
        length INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_packet(src, dst, proto, length):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO packets (src_ip,dst_ip,protocol,length) VALUES (?,?,?,?)",
        (src, dst, proto, length)
    )

    conn.commit()
    conn.close()


def get_packets():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT src_ip,dst_ip,protocol,length FROM packets ORDER BY id DESC LIMIT 20")

    rows = cursor.fetchall()

    conn.close()

    return rows
