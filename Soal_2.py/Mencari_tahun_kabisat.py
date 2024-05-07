def chek_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False
    
def tampilan_menu():
    print("Selamat Datang Di Pengecheckan Tahun Kabisat")

tahun = int(input("Masukkan tahun: "))

if chek_kabisat(tahun):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukanlah tahun kabisat.")
