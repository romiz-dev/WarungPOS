import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# membuka koneksi ke MySQL
def get_connection():    
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "warung_apps")
    )

# ==================== LOGIKA INVENTORY ====================
# fungsi simpan barang
def simpan_barang(kode, nama, harga, stok):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO tbl_barang (kode, nama, harga, stok) VALUES (%s, %s, %s, %s)"
    values = (kode, nama, harga, stok)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()

# fungsi cari barang
def cari_barang(keyword):
    db = get_connection()
    cursor = db.cursor(dictionary = True) # menggunakan dictionary=True agar hasil SELECT mudah dibaca
    query = "SELECT * FROM tbl_barang WHERE nama LIKE %s or kode LIKE %s"
    values = (f"%{keyword}%", f"%{keyword}%")
    cursor.execute(query, values)
    hasil = cursor.fetchall()
    cursor.close()
    db.close()
    return hasil

def tampilkan_semua_barang():
    db = get_connection()
    cursor = db.cursor(dictionary = True)
    query = "SELECT * FROM tbl_barang"
    cursor.execute(query)
    hasil = cursor.fetchall()
    cursor.close()
    db.close()
    return hasil

# fungsi update data barang
def update_data_barang(kode, kolom, value):
    kolom_valid = ["nama", "harga", "stok"]
    
    # 2. Validasi input, jika kolom yang diminta tidak ada di whitelist, batalkan!
    if kolom not in kolom_valid:
        raise ValueError(f"Celah Keamanan Terdeteksi: Kolom '{kolom}' tidak valid!")
    
    db = get_connection()
    cursor = db.cursor()
    query = f"UPDATE tbl_barang SET {kolom} = %s WHERE kode = %s"
    values = (value, kode)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()

# fungsi hapus barang
def hapus_barang(kode):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM tbl_barang WHERE kode = %s"
    cursor.execute(query, [kode])
    db.commit()
    cursor.close()
    db.close()

# ==================== LOGIKA PENDAPATAN ====================
# fungsi simpan pendapatan
def simpan_pendapatan(total):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO tbl_pendapatan (total_belanja) VALUES (%s)"
    cursor.execute(query, [total])
    db.commit()
    cursor.close()
    db.close()

def tampilkan_pendapatan():
    db = get_connection()
    cursor = db.cursor(dictionary = True)
    query = "SELECT * FROM tbl_pendapatan"
    cursor.execute(query)
    hasil = cursor.fetchall()
    cursor.close()
    db.close()
    return hasil

# ==================== LOGIKA UTANG PIUTANG ====================
def simpan_utang(nama, total):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO tbl_utang (nama_pengutang, total_utang) VALUES (%s, %s)"
    cursor.execute(query, (nama, total))
    db.commit()
    cursor.close()
    db.close()

def tampilkan_utang():
    db = get_connection()
    cursor = db.cursor(dictionary = True)
    query = "SELECT * FROM tbl_utang"
    cursor.execute(query)
    hasil = cursor.fetchall()
    cursor.close()
    db.close()
    return hasil

def cari_utang(keyword):
    db = get_connection()
    cursor = db.cursor(dictionary = True)
    query = "SELECT * FROM tbl_utang WHERE nama_pengutang LIKE %s or tanggal LIKE %s"
    values = (f"%{keyword}%", f"%{keyword}%")
    cursor.execute(query, values)
    hasil = cursor.fetchall()
    cursor.close()
    db.close()
    return hasil

def ganti_status_utang(id_utang, status_baru):
    db = get_connection()
    cursor = db.cursor()
    query = "UPDATE tbl_utang SET status = %s WHERE id_utang = %s"
    cursor.execute(query, (status_baru, id_utang))
    db.commit()
    cursor.close()
    db.close()