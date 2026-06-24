import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='online_canteen_apps'
)


def insert_item(kode, nama, kategori, harga):
    cursor = db.cursor()

    query = "INSERT INTO tbl_menu_kantin (kode, nama, kategori, harga) VALUES (%s, %s, %s, %s)"
    values = (kode, nama, kategori, harga)

    cursor.execute(query, values)
    db.commit()

    if cursor.rowcount > 0:
        print('\nBarang berhasil ditambahkan!')

    else:
        print('\nBarang gagal ditambahkan')


def fetch_item():
    cursor = db.cursor()

    query = "SELECT * FROM tbl_menu_kantin"

    cursor.execute(query)
    hasil = cursor.fetchall()
    return hasil
