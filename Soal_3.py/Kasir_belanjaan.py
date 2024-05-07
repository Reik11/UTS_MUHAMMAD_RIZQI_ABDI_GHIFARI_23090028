def hitung_total_harga(jumlah_barang):
    total = 0
    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
        total += harga
    return total

jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = hitung_total_harga(jumlah_barang)
print("Total harga belanjaan Kamu:", total_harga)
