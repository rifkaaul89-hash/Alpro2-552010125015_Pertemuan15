print("\nNama      : Rifka Aulia Putri")
print("NIM       : 552010125015")
print("Prodi     : Teknik Informatika")
print("Semester  : 2")
print("Tugas     : Final Mini Project")
print("Materi    : Presentasi dan Evaluasi Mini Project")
print("Pertemuan : 15")
print("=========================================")

# ==========================================
# MINI PROJECT ALGORITMA DAN PEMROGRAMAN 2
# PROGRAM ABSENSI KELAS
# ==========================================

import os
import random
from datetime import datetime

NAMA_FILE = "absensi.txt"

def buat_file_awal():
    if not os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "w") as file:
            pass

def baca_file():
    data = {}
    try:
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                baris = baris.strip()

                if baris == "":
                    continue

                bagian = baris.split(",")

                if len(bagian) != 3:
                    continue

                nim, nama, status = bagian
                data[nim] = {
                    "Nama": nama,
                    "Status": status
                }

    except FileNotFoundError:
        print("File absensi tidak ditemukan.")
        print("Membuat file baru...")
        buat_file_awal()

    return data

def simpan_file(data):
    with open(NAMA_FILE, "w") as file:
        for nim, isi in data.items():
            file.write(f"{nim},{isi['Nama']},{isi['Status']}\n")


# ==========================================
# FUNGSI LAPORAN HARIAN
# ==========================================

def simpan_laporan_harian(data):
    tanggal = datetime.now().strftime("%Y%m%d")
    nama_file = f"laporan_{tanggal}.txt"

    hadir = izin = sakit = alpha = 0

    with open(nama_file, "w") as file:

        file.write("=" * 55 + "\n")
        file.write("             LAPORAN ABSENSI HARIAN\n")
        file.write("=" * 55 + "\n")
        file.write("Tanggal : " +
                   datetime.now().strftime("%d-%m-%Y") + "\n\n")

        file.write("{:<4}{:<12}{:<25}{}\n".format(
            "No", "NIM", "Nama", "Status"))
        file.write("-" * 55 + "\n")

        no = 1

        for nim, isi in data.items():

            file.write("{:<4}{:<12}{:<25}{}\n".format(
                no,
                nim,
                isi["Nama"],
                isi["Status"]
            ))

            if isi["Status"] == "Hadir":
                hadir += 1
            elif isi["Status"] == "Izin":
                izin += 1
            elif isi["Status"] == "Sakit":
                sakit += 1
            elif isi["Status"] == "Alpha":
                alpha += 1

            no += 1

        total = len(data)

        file.write("\n")
        file.write("=" * 55 + "\n")
        file.write("STATISTIK\n")
        file.write("=" * 55 + "\n")
        file.write(f"Total Mahasiswa : {total}\n")
        file.write(f"Hadir           : {hadir}\n")
        file.write(f"Izin            : {izin}\n")
        file.write(f"Sakit           : {sakit}\n")
        file.write(f"Alpha           : {alpha}\n")

        if total > 0:
            file.write("\nPersentase Kehadiran\n")
            file.write(f"Hadir : {hadir/total*100:.2f}%\n")
            file.write(f"Izin  : {izin/total*100:.2f}%\n")
            file.write(f"Sakit : {sakit/total*100:.2f}%\n")
            file.write(f"Alpha : {alpha/total*100:.2f}%\n")

    print(f"\nLaporan berhasil disimpan ke file '{nama_file}'")

    def tampil_header():
        print("\n==========================================================")
        print("{:<4}{:<12}{:<25}{}".format("No", "NIM", "Nama", "Status"))
        print("-" * 58)


def tampilkan_menu():
    print("\n======================================")
    print("         PROGRAM ABSENSI KELAS")
    print("======================================")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Cari Data")
    print("4. Edit Data")
    print("5. Hapus Data")
    print("6. Urutkan Data")
    print("7. Statistik")
    print("8. Pengujian Data")
    print("9. Simpan Laporan Hari Ini")
    print("10. Keluar")
    print("======================================")


def pilih_status():
    print("\nPilih Status Kehadiran")
    print("1. Hadir")
    print("2. Izin")
    print("3. Sakit")
    print("4. Alpha")

    while True:
        pilihan = input("Pilih (1-4): ").strip()

        if pilihan == "1":
            return "Hadir"
        elif pilihan == "2":
            return "Izin"
        elif pilihan == "3":
            return "Sakit"
        elif pilihan == "4":
            return "Alpha"
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")


def tambah_data(data):
    print("\n===== TAMBAH DATA =====")

    nim = input("Masukkan NIM  : ").strip()

    if nim == "":
        print("NIM tidak boleh kosong.")
        return

    if not nim.isdigit():
        print("NIM harus berupa angka.")
        return

    if nim in data:
        print("NIM sudah terdaftar.")
        return

    nama = input("Masukkan Nama : ").strip()

    if nama == "":
        print("Nama tidak boleh kosong.")
        return

    if not nama.replace(" ", "").isalpha():
        print("Nama hanya boleh berisi huruf.")
        return

    status = pilih_status()

    data[nim] = {
        "Nama": nama.title(),
        "Status": status
    }

    simpan_file(data)
    print("\nData berhasil ditambahkan.")


def tampilkan_data(data):
    if not data:
        print("\nData masih kosong.")
        return

        tampil_header()

    no = 1

    for nim, isi in data.items():
        print("{:<4}{:<12}{:<25}{}".format(
            no,
            nim,
            isi["Nama"],
            isi["Status"]
        ))
        no += 1


def cari_data(data):
    if not data:
        print("\nData masih kosong.")
        return

    print("\n======================================")
    print("          MENU PENCARIAN")
    print("======================================")
    print("1. Cari Berdasarkan NIM")
    print("2. Cari Berdasarkan Nama")
    print("======================================")

    pilihan = input("Pilih : ").strip()

    if pilihan == "1":

        nim = input("Masukkan NIM : ").strip()

        if nim == "":
            print("NIM tidak boleh kosong.")
            return

        if nim in data:
            print("\n===== DATA DITEMUKAN =====")
            print("NIM    :", nim)
            print("Nama   :", data[nim]["Nama"])
            print("Status :", data[nim]["Status"])
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "2":

        nama = input("Masukkan Nama : ").strip().lower()

        if nama == "":
            print("Nama tidak boleh kosong.")
            return

        ditemukan = False

        print("\n===== HASIL PENCARIAN =====")

        for nim, isi in data.items():

            if nama in isi["Nama"].lower():

                print("NIM    :", nim)
                print("Nama   :", isi["Nama"])
                print("Status :", isi["Status"])
                print("-" * 30)

                ditemukan = True

        if not ditemukan:
            print("Data tidak ditemukan.")

    else:
        print("Pilihan tidak valid.")

def edit_data(data):
    if not data:
        print("\nData masih kosong.")
        return

    print("\n===== EDIT DATA =====")
    nim = input("Masukkan NIM yang akan diedit : ").strip()

    if nim == "":
        print("NIM tidak boleh kosong.")
        return

    if nim not in data:
        print("NIM tidak ditemukan.")
        return

    print("\nData Saat Ini")
    print("Nama   :", data[nim]["Nama"])
    print("Status :", data[nim]["Status"])

    print("\nPilihan Edit")
    print("1. Edit Nama")
    print("2. Edit Status")
    print("3. Edit Nama dan Status")

    pilihan = input("Pilih : ").strip()

    if pilihan == "1":
        nama = input("Masukkan Nama Baru : ").strip()

        if nama == "":
            print("Nama tidak boleh kosong.")
            return

        if not nama.replace(" ", "").isalpha():
            print("Nama hanya boleh berisi huruf.")
            return

        data[nim]["Nama"] = nama.title()

    elif pilihan == "2":
        data[nim]["Status"] = pilih_status()

    elif pilihan == "3":
        nama = input("Masukkan Nama Baru : ").strip()

        if nama == "":
            print("Nama tidak boleh kosong.")
            return

        if not nama.replace(" ", "").isalpha():
            print("Nama hanya boleh berisi huruf.")
            return

        data[nim]["Nama"] = nama.title()
        data[nim]["Status"] = pilih_status()

    else:
        print("Pilihan tidak valid.")
        return

    simpan_file(data)
    print("\nData berhasil diperbarui.")


def hapus_data(data):
    if not data:
        print("\nData masih kosong.")
        return

    print("\n===== HAPUS DATA =====")
    nim = input("Masukkan NIM yang akan dihapus : ").strip()

    if nim == "":
        print("NIM tidak boleh kosong.")
        return

    if nim not in data:
        print("NIM tidak ditemukan.")
        return

    print("\nData yang akan dihapus")
    print("NIM    :", nim)
    print("Nama   :", data[nim]["Nama"])
    print("Status :", data[nim]["Status"])

    konfirmasi = input("\nYakin ingin menghapus data? (Y/T) : ").strip().lower()

    if konfirmasi == "y":
        del data[nim]
        simpan_file(data)
        print("Data berhasil dihapus.")

    elif konfirmasi == "t":
        print("Penghapusan dibatalkan.")

    else:
        print("Pilihan tidak valid.")

def urutkan_data(data):
    if not data:
        print("\nData masih kosong.")
        return

    print("\n===== URUTKAN DATA =====")
    print("1. Berdasarkan NIM")
    print("2. Berdasarkan Nama")

    pilihan = input("Pilih : ").strip()

    hasil = list(data.items())
    n = len(hasil)

    # Bubble Sort berdasarkan NIM
    if pilihan == "1":
        for i in range(n - 1):
            for j in range(n - i - 1):
                if hasil[j][0] > hasil[j + 1][0]:
                    hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    # Bubble Sort berdasarkan Nama
    elif pilihan == "2":
        for i in range(n - 1):
            for j in range(n - i - 1):
                if hasil[j][1]["Nama"].lower() > hasil[j + 1][1]["Nama"].lower():
                    hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    else:
        print("Pilihan tidak valid.")
        return

        tampil_header()
    no = 1

    for nim, isi in hasil:
        print("{:<4}{:<12}{:<25}{}".format(
            no,
            nim,
            isi["Nama"],
            isi["Status"]
        ))
        no += 1

def statistik(data):
    if not data:
        print("\nData masih kosong.")
        return

    hadir = izin = sakit = alpha = 0

    for isi in data.values():

        if isi["Status"] == "Hadir":
            hadir += 1

        elif isi["Status"] == "Izin":
            izin += 1

        elif isi["Status"] == "Sakit":
            sakit += 1

        elif isi["Status"] == "Alpha":
            alpha += 1

    total = len(data)

    print("\n========== STATISTIK ABSENSI ==========")
    print("Total Mahasiswa :", total)
    print("Hadir           :", hadir)
    print("Izin            :", izin)
    print("Sakit           :", sakit)
    print("Alpha           :", alpha)

    print("\nPersentase Kehadiran")
    print("Hadir : {:.2f}%".format(hadir / total * 100))
    print("Izin  : {:.2f}%".format(izin / total * 100))
    print("Sakit : {:.2f}%".format(sakit / total * 100))
    print("Alpha : {:.2f}%".format(alpha / total * 100))

def generate_data(data):
    print("\n===== GENERATE DATA DUMMY =====")

    try:
        jumlah = int(input("Jumlah data yang ingin dibuat : "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    status_list = ["Hadir", "Izin", "Sakit", "Alpha"]

    nomor_awal = len(data) + 1

    for i in range(jumlah):
        nim = f"552010125{nomor_awal+i:03d}"

        while nim in data:
            nomor_awal += 1
            nim = f"552010125{nomor_awal+i:03d}"

        data[nim] = {
            "Nama": f"Mahasiswa {nomor_awal+i}",
            "Status": random.choice(status_list)
        }

    simpan_file(data)
    print(f"\n{jumlah} data berhasil ditambahkan.")


def hapus_banyak_data(data):
    if not data:
        print("\nData masih kosong.")
        return

    try:
        jumlah = int(input("Jumlah data yang akan dihapus : "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    if jumlah > len(data):
        jumlah = len(data)

    daftar_nim = list(data.keys())

    for i in range(jumlah):
        del data[daftar_nim[i]]

    simpan_file(data)
    print(f"\n{jumlah} data berhasil dihapus.")


def menu_pengujian(data):
    while True:
        print("\n======================================")
        print("        MENU PENGUJIAN DATA")
        print("======================================")
        print("1. Generate Banyak Data")
        print("2. Hapus Banyak Data")
        print("3. Kembali")
        print("======================================")

        pilihan = input("Pilih Menu (1-3): ").strip()

        if pilihan == "1":
            generate_data(data)

        elif pilihan == "2":
            hapus_banyak_data(data)

        elif pilihan == "3":
            break

        else:
            print("Pilihan tidak valid.")


def main():
    buat_file_awal()
    data = baca_file()

    while True:
        tampilkan_menu()

        pilihan = input("Pilih Menu (1-10) : ").strip()

        if pilihan == "1":
            tambah_data(data)

        elif pilihan == "2":
            tampilkan_data(data)

        elif pilihan == "3":
            cari_data(data)

        elif pilihan == "4":
            edit_data(data)

        elif pilihan == "5":
            hapus_data(data)

        elif pilihan == "6":
            urutkan_data(data)

        elif pilihan == "7":
            statistik(data)

        elif pilihan == "8":
            menu_pengujian(data)

        elif pilihan == "9":
            simpan_laporan_harian(data)

        elif pilihan == "10":
            print("\n=================================")
            print(" Terima kasih telah menggunakan")
            print(" Program Absensi Kelas")
            print("=================================")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
