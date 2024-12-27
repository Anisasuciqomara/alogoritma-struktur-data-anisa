if __name__ == "__main__":
    try:
        usia = int(input("Masukkan usia Anda: "))

        if 0 <= usia <= 5:
            kategori = "Balita"
        elif 6 <= usia <= 12:
            kategori = "Anak-anak"
        elif 13 <= usia <= 17:
            kategori = "Remaja"
        elif 18 <= usia <= 59:
            kategori = "Dewasa"
        elif usia >= 60:
            kategori = "Lansia"
        else:
            kategori = "Usia tidak valid"

        print(f"Kategori usia: {kategori}")
    except ValueError:
        print("Silakan masukkan angka yang valid.")
