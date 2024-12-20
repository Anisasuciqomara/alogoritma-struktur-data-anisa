# Variabel global untuk menyimpan data buku
buku = []

# Fungsi untuk menampilkan data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")

# Fungsi menambah data
def insert_data():
    buku_baru = input("Judul buku: ")
    buku.append(buku_baru)

# Fungsi untuk edit data
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            judul_baru = input("Judul baru: ")
            buku[indeks] = judul_baru
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    try:
        indeks = int(input("Masukkan ID buku: "))
        if indeks < 0 or indeks >= len(buku):
            print("ID SALAH")
        else:
            buku.pop(indeks)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("------ MENU ------")
    print("[1] Show data")
    print("[2] Insert data")
    print("[3] Edit data")
    print("[4] Delete data")
    print("[5] Exit")

    menu = input("PILIH MENU> ")
    print("\n")

    if menu == '1':
        show_data()
    elif menu == '2':
        insert_data()
    elif menu == '3':
        edit_data()
    elif menu == '4':
        delete_data()
    elif menu == '5':
        print("Keluar dari program")
        exit()
    else:
        print("SALAH PILIH")

# Menjalankan program
if __name__ == "__main__":
    while True:
        show_menu()