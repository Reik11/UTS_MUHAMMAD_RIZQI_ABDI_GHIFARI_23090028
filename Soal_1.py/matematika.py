def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def modulus(a, b):
    return a % b

def tampilan_menu():
    print("Tentukan Pilihan matematika anda")
    print("1.penjumlahan")
    print("2.pengurangan")
    print("3.modulus")

def operasi():
    while True:
        tampilan_menu()
        pilihan = input('masukan pilihan anda: ')
        if pilihan in ('1', '2', '3'):
            a = int(input('masukan bilangan pertama : '))
            b = int(input('masukan bilangan kedua : '))
            if pilihan == '1':
                print("Hasil penjumlahan:", penjumlahan(a, b))
            elif pilihan == '2':
                print("Hasil pengurangan:", pengurangan(a, b))
            elif pilihan == '3':
                print("Hasil modulus:", modulus(a, b))
        else:
            print("Pilihan tidak valid")
        
        ulangi = input("Apakah Anda ingin melakukan operasi lainnya? (y/n): ")
        if ulangi.lower() != 'y':
            break

operasi()
