def program_selanjutnya():
    print("\n--- Selamat datang Deny ---")

def input_data_pengguna():
    # Data user yang sudah terdaftar
    Nama_terdaftar = "Deny"
    Pin_terdaftar = "024"

    while True:
        # Meminta input Nama dan PIN dari pengguna
        nama = input("Masukkan Nama Anda: ")
        pin = input("Masukkan PIN Anda: ")

        # Menampilkan hasil login
        if nama == Nama_terdaftar and pin == Pin_terdaftar:
            print("Login berhasil")
            program_selanjutnya()
            return True
        else:
            print("Login gagal, coba lagi.")

        # Meminta input apakah ingin login lagi
        if input("Login lagi? (iya/tidak): ").lower() != "iya":
            print("Terima kasih!")
            return False

def hitung_total_pembelian():
    while True:
        try:
            harga = float(input("Masukkan harga perbarang: Rp. "))
            jumlah = int(input("Masukkan jumlah barang: "))
        except ValueError:
            print("Input tidak valid, coba lagi.")
            continue

        total = harga * jumlah
        if total > 250000:
            total -= 0.25 * total
            print(f"Anda mendapat diskon 25%. Total setelah diskon: Rp. {total:.2f}")
        else:
            print(f"Total harga: Rp. {total:.2f}")
            print("Anda tidak mendapatkan diskon 25%")

        if input("Hitung lagi? (iya/tidak): ").lower() != "iya":
            print("Terima kasih!")
            break

# Memanggil fungsi input_data_pengguna
if __name__ == "__main__":
    if input_data_pengguna():
        hitung_total_pembelian()
