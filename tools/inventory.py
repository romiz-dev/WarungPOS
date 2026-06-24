# initializing
import main
from tools.libs import welcome_messege, input_string, input_integer, input_kode, input_yesno
from time import sleep

def main_menu():
    while True:
        welcome_messege('INVENTORY')
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
    welcome_messege('INPUT BARANG')
    while True:
        nama_barang = input_string('Nama Barang: ').title()
        kode_barang = input_kode('Kode Barang\n(Formatnya 3 huruf dari jenis barang-3 huruf dari merek barang-atribut tambahan. Contoh format: MGO-BIM-2L): ').upper()
        harga_barang = input_integer('Harga Barang: ')
        stok_barang = input_integer('Stok Barang: ')
        print('\nBarang berhasil di input!\n\n1. Input Barang\n2. Kembali')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            continue
        elif choose == 2:
            break

def kelola_barang():
    main_menu = ['Cari Barang', 'Edit Barang', 'Kembali']
    while True:
        welcome_messege('PENGELOLAAN BARANG')
        for i, menu in enumerate(main_menu, 1):
            print(f'{i}. {menu}')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            cari_barang()
        elif choose == 2:
            edit_barang()
        elif choose == 3:
            main.main_menu()
        else:
            print('Pilihan tidak tersedia!')
            continue

def cari_barang():
    while True:
        data = input_string('Masukkan merek atau kategori barang: ')
        print('Barang ditemukan!')
        edit_barang()

def edit_barang():
    # gimana caranya agar ketika user mengedit data barang misalnya nama barang, 
    # user bisa mengedit data barang yang sama tanpa harus memasukkan kembali kodenya 
    # kecuali jika kodenya sudah diganti
    while True:
        main_menu = ['Nama Barang', 'Kode Barang', 'Harga Barang', 'Stok Barang', 'Hapus Barang']

        kode = input_kode('Masukkan kode barang: ').upper()
        print('\nApa yang ingin anda ubah?\n')

        for i, menu in enumerate(main_menu, 1):
            print(f'{i}. {menu}')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            ganti_nama()
        elif choose == 2:
            ganti_kode()
        elif choose == 3:
            ganti_harga()
        elif choose == 4:
            ganti_stok()
        elif choose == 5:
            hapus_barang()
        else:
            print('Pilihan tidak tersedia!!!')
            continue

def ganti_nama():
    while True:
        nama_baru = input_string('Masukkan nama baru: ')
        print('Mengganti nama...')
        sleep(3)
        print('Nama berhasil diubah!\n\n1. Kembali')
        select = input_integer('Pilihanmu: ')
        
        if select == 1:
            kelola_barang()
        else:
            print('Pilihan tidak tersedia!!!')
            continue

def ganti_kode():
    while True:
        kode_baru = input_kode('Masukkan kode baru: ')
        print('Mengganti kode...')
        sleep(3)
        print('Kode berhasil diubah!\n\n1. Kembali')
        select = input_integer('Pilihanmu: ')
        
        if select == 1:
            kelola_barang()
        else:
            print('Pilihan tidak tersedia!!!')
            continue

def ganti_harga():
    while True:
        harga_baru = input_integer('Masukkan harga baru: ')
        print('Mengganti harga...')
        sleep(3)
        print('Harga berhasil diubah!\n\n1. Kembali')
        select = input_integer('Pilihanmu: ')
        
        if select == 1:
            kelola_barang()
        else:
            print('Pilihan tidak tersedia!!!')
            continue

def ganti_stok():
    while True:
        stok_baru = input_integer('Masukkan stok baru: ')
        print('Mengganti stok...')
        sleep(3)
        print('Stok berhasil diubah!\n\n1. Kembali')
        select = input_integer('Pilihanmu: ')
        
        if select == 1:
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