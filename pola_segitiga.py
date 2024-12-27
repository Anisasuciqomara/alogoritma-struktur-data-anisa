def cetak_pola(baris):
    for i in range(1, baris + 1):
        print('*' * i)

if __name__ == "__main__":
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
        cetak_pola(jumlah_baris)
    except ValueError:
        print("Silakan masukkan angka yang valid.")
