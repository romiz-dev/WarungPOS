# initializing
import main
from tools.libs import welcome_message, input_string, input_integer, input_kode, input_yesno
from time import sleep
from services import db
import mysql.connector

def main_menu():
    while True:
        welcome_message('INVENTORY')
        main_menu = ['Input Barang', 'Kelola Barang', 'Kembali']

        for i, menu in enumerate(main_menu, 1):
            print(f'{i}. {menu}')

        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            input_barang()
        elif choose == 2:
            kelola_barang()
        elif choose == 3:
            main.main_menu()
        else:
            print('Pilihan tidak tersedia')
            continue

def input_barang():
    # gimana caranya agar database menjadi sensitif
    # sehingga jika ada barang dengan nama barang dan kode barang yang sama 
    # database tidak menerimanya
    welcome_message('INPUT BARANG')
    while True:
        print('Tekan n untuk batal')
        nama_barang = input_string('Nama Barang: ').title()
        if nama_barang == 'N':
            return
        kode_barang = input_kode('Kode Barang\n(Formatnya 3 huruf dari jenis barang-3 huruf dari merek barang-atribut tambahan. Contoh format: MGO-BIM-2L): ').upper()
        harga_barang = input_integer('Harga Barang: ')
        stok_barang = input_integer('Stok Barang: ')
        
        # error handling untuk duplikasi barang
        try:
            db.simpan_barang(kode_barang, nama_barang, harga_barang, stok_barang)
            print('\nBarang berhasil di input!\n')
        except mysql.connector.Error as err:
            if err.errno == 1062: # 1062 kode error untuk duplikasi barang
                print('Input gagal, kode atau nama barang sudah terdaftar!!!')
            else:
                print(f'Terjadi kesalahan: {err}')

        print('1. Input Barang\n2. Kembali')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            continue
        elif choose == 2:
            break

def kelola_barang():
    main_menu = ['Cari Barang', 'Tampilkan Semua Barang', 'Kembali']
    while True:
        welcome_message('PENGELOLAAN BARANG')
        for i, menu in enumerate(main_menu, 1):
            print(f'{i}. {menu}')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            cari_barang()
        elif choose == 2:
            tampilkan_barang()
        elif choose == 3:
            main.main_menu()
        else:
            print('Pilihan tidak tersedia!')
            continue

def tampilkan_barang():
    while True:
        hasil = db.tampilkan_semua_barang()
        welcome_message('DATA BARANG')
        for i, tbl_barang in enumerate(hasil, 1):
            print(f'{i}. [{tbl_barang['kode']}] {tbl_barang['nama']} - Rp{tbl_barang['harga']} ({tbl_barang['stok']})')

        pilih = input_integer('\nPilih nomor barang yang ingin diedit (0 untuk kembali): ')
        if pilih == 0 or pilih > len(hasil):
            return

        barang_terpilih = hasil[pilih - 1]
        edit_barang(barang_terpilih)

def cari_barang():
    while True:
        keyword = input_string('Masukkan merek atau kategori barang: ')
        hasil = db.cari_barang(keyword)

        if not hasil:
            print('Barang tidak ditemukan!\n')
            return
        
        print('\nHasil pencarian: ')
        for i, tbl_barang in enumerate(hasil, 1):
            print(f'{i}. [{tbl_barang['kode']}] {tbl_barang['nama']} - Rp{tbl_barang['harga']} (Stok: {tbl_barang['stok']})')

        pilih = input_integer('\nPilih nomor barang yang ingin diedit: ')
        if pilih == 0 or pilih > len(hasil):
            return

        barang_terpilih = hasil[pilih - 1]
        edit_barang(barang_terpilih)

def edit_barang(barang):
    while True:
        main_menu = ['Nama Barang', 'Kode Barang', 'Harga Barang', 'Stok Barang', 'Hapus Barang', 'Kembali']

        print(f'\nBarang terpilih: [{barang['kode']}] {barang['nama']} - Rp{barang['harga']} (Stok: {barang['stok']})')
        print('\nApa yang ingin anda ubah?\n')

        for i, menu in enumerate(main_menu, 1):
            print(f'{i}. {menu}')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            nama_baru = input_string('Masukkan nama baru: ').title()
            print('Mengganti nama...')
            db.update_data_barang(barang['kode'], 'nama', nama_baru)
            barang['nama'] = nama_baru
            sleep(2)
            print('\nNama berhasil diubah!')
        elif choose == 2:
            kode_baru = input_kode('Masukkan kode baru: ').upper()
            try:
                print('Mengganti kode...')
                db.update_data_barang(barang['kode'], 'kode', kode_baru)
                barang['kode'] = kode_baru
                sleep(2)
                print('\nKode berhasil diubah!')
            except mysql.connector.Error:
                print('GAGAL! Kode barang sudah dipakai!')
        elif choose == 3:
            harga_baru = input_integer('Masukkan harga baru: ')
            print('Mengganti harga...')
            db.update_data_barang(barang['kode'], 'harga', harga_baru)
            barang['harga'] = harga_baru
            sleep(2)
            print('Harga berhasil diubah!')
        elif choose == 4:
            stok_baru = input_integer('Masukkan stok baru: ')
            print('Mengganti stok...')
            db.update_data_barang(barang['kode'], 'stok', stok_baru)
            barang['stok'] = stok_baru
            sleep(2)
            print('Stok berhasil diubah!')
        elif choose == 5:
            choose = input_yesno('Apakah anda yakin ingin menghapus barang ini? [y/n]: ')

            if choose == 'y':
                print('Menghapus barang...')
                db.hapus_barang(barang['kode'])
                sleep(2)
                print('Barang berhasil dihapus!!!\n')
                break
        elif choose == 6:
            kelola_barang()
        else:
            print('Pilihan tidak tersedia!!!')
            continue

def hapus_barang():
    while True:
        choose = input_yesno('Apakah anda yakin ingin menghapus barang ini? [y/n]: ')

        if choose == 'y':
            print('Menghapus barang...')
            sleep(3)
            print('Barang berhasil dihapus!!!\n\n1. Kembali')
            select = input_integer('Pilihanmu: ')
            
            if select == 1:
                kelola_barang()
            else:
                print('Pilihan tidak tersedia!!!')
                continue

        elif choose == 'n':
            print('Proses dibatalkan...')
            sleep(2)
            kelola_barang()
        else:
            print('Pilihan tidak tersedia!!!')
            continue

def start():
    main_menu()

if __name__ == '__main__':
    start()