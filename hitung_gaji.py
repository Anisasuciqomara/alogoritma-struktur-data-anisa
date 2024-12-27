def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0
    for _ in range(hari_kerja):
        if jam_kerja_per_hari > 8:
            lembur = jam_kerja_per_hari - 8
            total_gaji += (8 * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            total_gaji += jam_kerja_per_hari * tarif_per_jam
    return total_gaji

if __name__ == "__main__":
    try:
        tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
        jam_kerja_per_hari = float(input("Masukkan jam kerja per hari: "))
        hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
        total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
        print(f"Total gaji bulanan: {total_gaji}")
    except ValueError:
        print("Silakan masukkan angka yang valid.")
