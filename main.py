#initializing
from tools import inventory, libs, pendapatan, utang_piutang, pembayaran

#main menu function
def main_menu():
    while True:
        libs.welcome_message('BAROKAH MART')
        main_menu = ['Inventory', 'Pendapatan', 'Utang Piutang', 'Pembayaran', 'Logout']

        for i, item in enumerate(main_menu, 1):
            print(f'{i}. {item}')

        choose = libs.input_integer('\nPilihanmu: ')

        if choose == 1:
            inventory.start()
        elif choose == 2:
            pendapatan.start()
        elif choose == 3:
            utang_piutang.start()
        elif choose == 4:
            pembayaran.start()
        elif choose == 5:
            libs.logout()
        else:
            print('\nPilihan tidak tersedia!\n')
            continue
#main function
def main():
    main_menu()

if __name__ == '__main__':
    main()