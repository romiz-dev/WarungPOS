from time import sleep
import re

def welcome_messege(nama):
    style = '=' * (len(nama) + 6)
    print(style)
    print(f'== {nama} ==')
    print(style)
    
def logout():
    print('Program akan dihentikan dalam:')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program dihentikan.')
    exit()

def insert_card():
    sleep(2)
    print('Memproses...')
    sleep(3)

def print_struk():
    print('Printing struk...\n')
    sleep(3)
    print('Struk berhasil di print!')

def input_alfabet(prompt):
    while True:
        try:
            data = input(prompt).strip() #fungsi strip() untuk menghapus spasi di awal dan akhir input

            if data == '':
                print('INPUT TIDAK VALID!!!')
                continue
            elif not data.replace(' ', '').isalpha(): #fungsi replace() untuk menghapus spasi di dalam string, fungsi isalpha() untuk mengecek apakah string hanya terdiri dari huruf
                raise ValueError('INPUT TIDAK VALID!!!')
            
        except ValueError as error_message:
            print(error_message)
            continue
        return data

def input_string(prompt):
    while True:
        data = input(prompt).strip()

        if data == '':
            print('INPUT TIDAK BOLEH KOSONG!!!')
            continue
        return data

def input_integer(prompt):
    while True:
        data = input(prompt).strip() #fungsi strip() untuk menghapus spasi di awal dan akhir input

        if data == '':
            print('INPUT TIDAK BOLEH KOSONG!!!')
            continue
        try:
            return int(data)
        except ValueError:
            print('INPUT HARUS BERUPA ANGKA!!!')

def input_yesno(prompt):
    while True:
        try:
            data = input(prompt).strip()

            if data == '':
                print('INPUT TIDAK BOLEH KOSONG!!!')
                continue
            elif data == 'y':
                return data
            elif data == 'n':
                return data
            else:
                raise ValueError('PILIHAN TIDAK TERSEDIA!!!')
            
        except ValueError as error_message:
            print(error_message)
            continue

def input_kode(prompt):
    # Pola regex untuk 3 huruf - 3 huruf - sisa karakter bebas (huruf/angka)
    pola = r'^[A-Za-z]{3}-[A-Za-z]{3}-[A-Za-z0-9]+$'

    while True:
        data = input(prompt).strip()

        if data == '':
            print('INPUT TIDAK BOLEH KOSONG!!!')
            continue
        
        elif not re.match(pola, data):
            print('INPUT TIDAK SESUAI FORMAT!!!')
            continue
        return data