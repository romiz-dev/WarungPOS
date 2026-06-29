# WarungPOS (Barokah Mart) 🛒

Aplikasi Point of Sales (POS) / Kasir berbasis teks (CLI) yang dirancang untuk membantu pengelolaan inventaris barang, pencatatan transaksi pendapatan, serta manajemen utang piutang secara terintegrasi dengan database MySQL.

## ✨ Fitur Utama
- **Inventory:** Input barang baru dengan format kode otomatis (Regex), edit detail barang (nama, harga, stok), dan hapus barang dengan validasi database anti-duplikasi.
- **Pembayaran:** Simulasi metode pembayaran Cash, Cashless, serta fitur pencatatan Utang jika pembeli kasbon.
- **Utang Piutang:** Melacak daftar pelanggan yang berutang dan mengubah status menjadi "Lunas".
- **Pendapatan:** Menampilkan total statistik keuangan toko dari database secara *real-time*.

## 🚀 Teknologi yang Digunakan
- **Python 3** (Bahasa Pemrograman Utama)
- **MySQL** (Penyimpanan Data Server)
- **Regex (Regular Expression)** (Validasi standarisasi kode barang)
- **Pustaka Eksternal:** `mysql-connector-python`, `python-dotenv`

## 🛠️ Cara Menjalankan Proyek di Lokal

Jika Anda ingin mencoba menjalankan proyek ini di komputer Anda, ikuti langkah-langkah berikut:

## Cara Menjalankan Proyek Ini:
1. Clone repositori ini ke laptop Anda.
2. Install dependensi dengan perintah: `pip install -r requirements.txt`.
3. Import file `database.sql` ke server MySQL lokal Anda.
4. Salin file `.env.example` menjadi `.env`, lalu sesuaikan `DB_USER` dan `DB_PASSWORD` dengan MySQL Anda.
5. Jalankan program dengan perintah: `python main.py`.
