def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

if __name__ == "__main__":
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(f"Hasil: {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"Hasil: {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"Hasil: {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"Hasil: {bagi(angka1, angka2)}")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Silakan masukkan angka yang valid.")
