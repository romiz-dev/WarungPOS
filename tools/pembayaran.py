import main
from tools.libs import welcome_messege, insert_card, print_struk, input_integer, input_string, input_yesno

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
        try:
            for i, selection in enumerate(menu, 1):
                print(f'{i}. {selection}')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                utang()
            elif choose == 2:
                bayar()
            elif choose == 3:
                main_menu()
            else:
                print('Pilihan tidak tersedia!')
                continue
        except ValueError:
            print('Pilihan tidak tersedia!')

def cashless():
    welcome_messege('CASHLESS')
    print('Tempelkan kartu')
    insert_card()
    while True:
        pin = input_integer('PIN: ')
        if pin == '':
            print('\nHarap masukan password!')
            continue
        else:
            choose = input_yesno('Ingin melanjutkan pembayaran?[y/n]: ')
            if choose == 'y':
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

def bayar():
    while True:
        welcome_messege('BAYAR')
        total = input_integer('Total belanja: ')
        if total == ' ':
            print('\nHarap masukkan angka yang valid!')
        else:
            print('\nPembayaran berhasil dilakukan!')
            print_struk()
            print('\n1. Kembali')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                main_menu()

def utang():
    welcome_messege('UTANG')
    pengutang = input_string('Nama: ')
    total_belanja = input_integer('Total belanja: ')
    print('\nData berhasil di masukkan!')

    while True:
        print('\n1. Kembali')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            main_menu()
        else:
            print('Pilihan tidak tersedia!')

def start():
    main_menu()

if __name__ == '__main__':
    start()