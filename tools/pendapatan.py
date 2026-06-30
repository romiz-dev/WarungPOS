import main
from tools.libs import welcome_message, input_integer
from services import db
import mysql.connector

def main_menu():
    main_menu = ['Cek Pendapatan', 'Kembali']
    
    while True:
        welcome_message('PENDAPATAN')
        try:
            for i, menu in enumerate(main_menu, 1):
                print(f'{i}. {menu}')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                pendapatan()
            elif choose == 2:
                main.main_menu()
            else:
                print('Pilihan tidak tersedia!')
                continue
        except ValueError:
            print('Pilihan tidak tersedia!')


def pendapatan():
    # menampilkan pendapatan harian dan pendapatan bulanan dari database pendapatan
    while True:
        hasil = db.tampilkan_pendapatan()
        welcome_message('DATA PENDAPATAN')

        for i, tbl_pendapatan in enumerate(hasil, 1):
            print(f'{i}. Total Belanja: Rp{tbl_pendapatan['total_belanja']:,} | {tbl_pendapatan['tanggal']}')
        print('\n1. Kembali')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            break
        else:
            print('Pilihan tidak tersedia!')
            continue


def start():
    main_menu()


if __name__ == '__main__':
    start()
