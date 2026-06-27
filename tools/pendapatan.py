import main
from tools.libs import welcome_messege, input_integer


def main_menu():
    main_menu = ['Cek Pendapatan', 'Kembali']
    
    while True:
        welcome_messege('PENDAPATAN')
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
    welcome_messege('DATA PENDAPATAN')
    print('COMING SOON!')
    while True:
        try:
            print('\n1. Kembali')
            choose = input_integer('\nPilihanmu: ')

            if choose == 1:
                break
            else:
                print('Pilihan tidak tersedia!')
                continue
        except ValueError:
            print('Pilihan tidak tersedia!')


def start():
    main_menu()


if __name__ == '__main__':
    start()
