import main
from tools.libs import welcome_messege, insert_card, print_struk, input_integer, input_string, input_yesno
from services import db
import mysql.connector

def main_menu():
    main_menu = ['Cash', 'Cashless', 'Kembali']
    welcome_messege('METODE PEMBAYARAN')
    while True:
        try:
            for i, menu in enumerate(main_menu, 1):
                print(f'{i}. {menu}')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                cash()
            elif choose == 2:
                cashless()
            elif choose == 3:
                main.main_menu()
            else:
                print('Pilihan tidak tersedia!')
                continue
        except ValueError:
            print('Pilihan tidak tersedia!')


def cash():
    menu = ['Utang', 'Bayar', 'Kembali']
    welcome_messege('CASH')
    while True:
        total = input_integer('Masukkan total belanja: ')
        try:
            for i, selection in enumerate(menu, 1):
                print(f'{i}. {selection}')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                pengutang = input_string('Nama: ')
                db.simpan_utang(pengutang, total)
                print('Data berhasil dimasukkan!')
                print('\n1. Kembali')
                choose = input_integer('\nPilihanmu: ')

                if choose == 1:
                    main_menu()
                else:
                    print('Pilihan tidak tersedia!')
            elif choose == 2:
                db.simpan_pendapatan(total)
                print('\nPembayaran berhasil dilakukan!')
                print_struk()
                print('\n1. Kembali')
                pilih = input_integer('\nPilihanmu: ')

                if pilih == 1:
                    main_menu()
            elif choose == 3:
                main_menu()
            else:
                print('Pilihan tidak tersedia!')
                continue
        except ValueError:
            print('Pilihan tidak tersedia!')


def cashless():
    while True:
        welcome_messege('CASHLESS')
        total = input_integer('Masukkan total belanja: ')
        print('Tempelkan kartu')
        insert_card()
        pin = input_integer('PIN: ')
        choose = input_yesno('Ingin melanjutkan pembayaran?[y/n]: ')
        if choose == 'y':
            db.simpan_pendapatan(total)
            print('\nPembayaran berhasil dilakukan!')
            # total belanja akan masuk ke database pendapatan
            print_struk()
            print('\n1. Kembali')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                main_menu()
        elif choose == 'n':
            print('Pembayaran dibatalkan!')
            print('\n1. Kembali')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                main_menu()


def start():
    main_menu()


if __name__ == '__main__':
    start()
