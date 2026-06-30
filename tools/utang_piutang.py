import main
from tools.libs import welcome_message, input_integer, input_string, input_yesno
from time import sleep
from services import db
import mysql.connector

def main_menu():
    while True:
        main_menu = ['Tampilkan Utang', 'Kelola Utang', 'Kembali']
        welcome_message('UTANG PIUTANG')
        
        for i, menu in enumerate(main_menu, 1):
            print(f'{i}. {menu}')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            tampilkan_utang()
        elif choose == 2:
            kelola_utang()
        elif choose == 3:
            main.main_menu()
        else:
            print('Pilihan tidak tersedia!')
            continue

def tampilkan_utang():
    # menampilkan data pengutang dari database utang
    # data pengutang berasal dari fitur pembayaran.
    # jika sang pembeli berutang, data rincian belanja akan dimasukkan ke database utang
    while True:
        welcome_message('DAFTAR UTANG')
        hasil = db.tampilkan_utang()

        for tbl_utang in hasil:
            print(f'{tbl_utang['nama_pengutang']} Total Utang: Rp{tbl_utang['total_utang']} [{tbl_utang['status']}] | {tbl_utang['tanggal']}')
        print('\n1. Kembali\n')
        choose = input_integer('Pilihanmu: ')

        if choose == 1:
            break
        else:
            print('Pilihan tidak tersedia!')
            continue

def kelola_utang():
    # mengupdate status pengutang, lunas atau belum lunas
    # dengan cara mencari pengutang berdasarkan nama atau tanggal berutang
    # jika lunas akan diprint struk utang lunas yang berisi rincian belanja
    welcome_message('KELOLA UTANG')
    
    pengutang = input('Cari pengutang (nama/tanggal berutang): ').title()
    hasil = db.cari_utang(pengutang)

    if not hasil:
        print('\nPengutang tidak ditemukan!\n')

    print('Daftar Pengutang:')
    for i, tbl_utang in enumerate(hasil, 1):
        print(f'{i}. {tbl_utang['nama_pengutang']} Total Utang: Rp{tbl_utang['total_utang']} [{tbl_utang['status']}] | {tbl_utang['tanggal']}')
    
    while True:
        pilih = input_integer('\nPilih nomor pengutang (0 untuk kembali): ')
        if pilih == 0:
            main_menu()
        elif 0 > pilih > len(hasil):
            continue

        utang_terpilih = hasil[pilih - 1]

        status = input_yesno(f'Ubah status utang {utang_terpilih['nama_pengutang']} menjadi Lunas [y/n]: ')
        
        if status == 'y':
            print('Mengganti status...')
            db.ganti_status_utang(utang_terpilih['id_utang'], 'Lunas')
            sleep(2)
            print('\nStatus berhasil diubah!')
            main_menu()
        
        print('Program di batalkan!')
        main_menu()

def edit_utang(hasil_utang):
    while True:
        pilih = input_integer('\nPilih nomor pengutang (0 untuk kembali): ')
        if pilih == 0:
            main_menu()
        elif 0 > pilih > len(hasil_utang):
            continue

        utang_terpilih = hasil_utang[pilih - 1]

        status = input_string('Status utang: ')
        print('Mengganti status...')
        db.ganti_status_utang(utang_terpilih['id_utang'], status)
        sleep(2)
        print('\nStatus berhasil diubah!')
        main_menu()

def start():
    main_menu()


if __name__ == '__main__':
    start()