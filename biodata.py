# Program to collect and display user biodata

def main():
    # Collect user information
    name = input("Masukkan nama Anda: ")
    age = input("Masukkan usia Anda: ")
    address = input("Masukkan alamat Anda: ")
    hobbies = input("Masukkan hobi Anda (pisahkan dengan koma): ")

    # Format and display the biodata
    print("\n--- Biodata Anda ---")
    print(f"Nama: {name}")
    print(f"Usia: {age} tahun")
    print(f"Alamat: {address}")
    print(f"Hobi: {hobbies}")

if __name__ == "__main__":
    main()
