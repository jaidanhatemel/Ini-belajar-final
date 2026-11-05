import pandas as pd
import csv
import os

# Fungsi penjumlahan
def tambah(a, b):
    return a + b

# Fungsi pengurangan
def kurang(a, b):
    return a - b

# Fungsi perkalian
def kali(a, b):
    return a * b

# Fungsi pembagian
def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi nol"
    return a / b

# Menyimpan hasil ke CSV
def simpan_csv(a, b, operasi, hasil):
    file = "riwayat_kalkulator.csv"

    file_baru = not os.path.exists(file)

    with open(file, mode="a", newline="") as f:
        writer = csv.writer(f)

        if file_baru:
            writer.writerow(["angka1", "angka2", "operasi", "hasil"])

        writer.writerow([a, b, operasi, hasil])

# Menampilkan riwayat menggunakan pandas
def tampilkan_riwayat():
    file = "riwayat_kalkulator.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
        print("\n===== RIWAYAT PERHITUNGAN =====")
        print(df)
    else:
        print("Belum ada riwayat.")

# Program utama
while True:
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Tambah lagi ya maw brapa")
    print("2. Kurangi lagi yah")
    print("3. Kali")
    print("4. Bagi")
    print("5. Lihat Riwayat")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "5":
        tampilkan_riwayat()
        continue

    if pilihan == "6":
        print("Program selesai.")
        break

    if pilihan in ["1", "2", "3", "4"]:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == "1":
            hasil = tambah(a, b)
            operasi = "Tambah"

        elif pilihan == "2":
            hasil = kurang(a, b)
            operasi = "Kurang"

        elif pilihan == "3":
            hasil = kali(a, b)
            operasi = "Kali"

        elif pilihan == "4":
            hasil = bagi(a, b)
            operasi = "Bagi"

        print(f"Hasil = {hasil}")

        simpan_csv(a, b, operasi, hasil)

    else:
        print("Pilihan tidak valid!")
