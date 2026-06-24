import main
from tools.libs import welcome_messege, input_integer, input_string


def main_menu():
    
    main_menu = ['Tampilkan Utang', 'Kelola Utang', 'Kembali']
    welcome_messege('UTANG PIUTANG')
    while True:
        try:
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
        except ValueError:
            print('Pilihan tidak tersedia!')


def tampilkan_utang():
    # menampilkan data pengutang dari database utang
    # data pengutang berasal dari fitur pembayaran.
    # jika sang pembeli berutang, data rincian belanja akan dimasukkan ke database utang
    welcome_messege('DAFTAR UTANG')
    print('COMING SOON!\n')
    while True:
        try:
            print('1. Kembali\n')
            choose = input_integer('Pilihanmu: ')

            if choose == 1:
                break
            else:
                print('Pilihan tidak tersedia!')
                continue
        except ValueError:
            print('Pilihan tidak tersedia!')


def kelola_utang():
    # mengupdate status pengutang, lunas atau belum lunas
    # dengan cara mencari pengutang berdasarkan nama atau tanggal berutang
    # jika lunas akan diprint struk utang lunas yang berisi rincian belanja
    menu = ['Kelola Utang', 'Kembali']
    welcome_messege('KELOLA UTANG')
    while True:
        
        pengutang = input('Cari pengutang (nama/tanggal berutang): ')
        print('\nPengutang berhasil ditemukan!\n')
        status = input_string('Status utang: ')
        print('\nStatus berhasil diubah!')

        #Gimana caranya agar error handling di baris bawah ini gk ngulang dari baris 56???
        for i, menu in enumerate(menu, 1):
            print(f'{i}. {menu}')
        choose = input_integer('\nPilihanmu: ')

        if choose == 1:
            continue
        elif choose == 2:
            main_menu()

def start():
    main_menu()


if __name__ == '__main__':
    start()