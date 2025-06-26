# ========= SISTEM ANTRIAN RSUD PANTAI CERMIN =========
# Terminal CLI Version | BPJS & Non-BPJS | 500+ Baris

from collections import deque
from datetime import datetime
from termcolor import cprint
import time
import threading
import csv
import os

# ========== GLOBAL VARIABLE ==========
data_bpjs = deque()
data_nonbpjs = deque()
riwayat_dipanggil = []
nomor_bpjs = 0
nomor_nonbpjs = 0
file_riwayat = "riwayat_pasien.txt"
file_export = "data_export.csv"
stop_simulasi = False
BATAS_ANTRIAN = 100

# ========== UTILITAS ==========
def header():
    cprint("\n" + "="*74,"white","on_red")
    cprint("🏥  SISTEM ANTRIAN RSUD PANTAI CERMIN ".center(73), "green", "on_red")
    cprint("="*74,"white","on_red")

def pause():
    input("\n🔘 Tekan ENTER untuk kembali ke menu...")

def garis():
    print("-"*75)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def waktu_sekarang():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def valid_bpjs(nomor):
    return nomor.isdigit() and len(nomor) >= 8

# ========== TAMBAH PASIEN ==========
def tambah_pasien():
    global nomor_bpjs, nomor_nonbpjs
    if len(data_bpjs) + len(data_nonbpjs) >= BATAS_ANTRIAN:
        print("❌ Antrian penuh. Silakan tunggu beberapa saat.")
        return

    print("\n📋 PENDAFTARAN PASIEN BARU")
    nama = input("🧍 Nama pasien: ").strip()
    keluhan = input("🤒 Keluhan penyakit: ").strip()
    bpjs = input("📄 Nomor BPJS (kosongkan jika tidak ada): ").strip()

    waktu = waktu_sekarang()
    if bpjs:
        if not valid_bpjs(bpjs):
            print("⚠ Nomor BPJS tidak valid. Harus minimal 8 digit angka.")
            return
        nomor_bpjs += 1
        pasien = {
            "No": f"B{nomor_bpjs}",
            "Nama": nama,
            "Keluhan": keluhan,
            "BPJS": bpjs,
            "Waktu": waktu,
            "Jenis": "BPJS"
        }
        data_bpjs.append(pasien)
    else:
        nomor_nonbpjs += 1
        pasien = {
            "No": f"N{nomor_nonbpjs}",
            "Nama": nama,
            "Keluhan": keluhan,
            "BPJS": "-",
            "Waktu": waktu,
            "Jenis": "Non-BPJS"
        }
        data_nonbpjs.append(pasien)

    print(f"\n✅ Pasien '{nama}' telah didaftarkan dengan nomor antrian {pasien['No']} ({pasien['Jenis']}).")
    cetak_struk(pasien)

# ========== CETAK STRUK ==========
def cetak_struk(pasien):
    print("\n🧾 STRUK ANTRIAN")
    garis()
    cprint(f" Nomor Antrian : {pasien['No']} ({pasien['Jenis']})", "black",  attrs=["bold"])
    cprint(f" Nama Pasien   : {pasien['Nama']}", "black")
    cprint(f" Keluhan       : {pasien['Keluhan']}", "black")
    cprint(f" No. BPJS      : {pasien['BPJS']}", "black")
    cprint(f" Waktu Daftar  : {pasien['Waktu']}", "black")
    garis()
# ========== PANGGIL PASIEN ==========
def panggil_pasien():
    print("\n🔔 PEMANGGILAN PASIEN")
    if not data_bpjs and not data_nonbpjs:
        print("📭 Tidak ada pasien dalam antrian.")
        return

    print("⏳ Memanggil pasien...\n")
    time.sleep(1.5)

    if data_bpjs:
        pasien = data_bpjs.popleft()
    else:
        pasien = data_nonbpjs.popleft()

    riwayat_dipanggil.append(pasien)
    

    cprint(f"🎤 Pasien nomor {pasien['No']} ({pasien['Jenis']}) atas nama {pasien['Nama']} silakan masuk.", "black", "on_white", attrs=["bold"])
    cprint(f"📝 Keluhan       : {pasien['Keluhan']}", "white")
    cprint(f"🕒 Waktu Daftar  : {pasien['Waktu']}", "white")
# ========== SIMPAN RIWAYAT ==========
def simpan_riwayat(pasien):
    with open(file_riwayat, "a") as f:
        f.write(f"{pasien['No']},{pasien['Nama']},{pasien['Keluhan']},{pasien['BPJS']},{pasien['Waktu']},{pasien['Jenis']}\n")

# ========== CETAK TABEL ==========
def print_tabel(deque_data):
    print("╔═════╦════════════════════╦════════════════╦════════════╦══════════════════════╗")
    print("║ No  ║ Nama               ║ Keluhan        ║ BPJS       ║ Waktu Daftar         ║")
    print("╠═════╬════════════════════╬════════════════╬════════════╬══════════════════════╣")
    for d in deque_data:
        print("║ {:<3} ║ {:<18} ║ {:<14} ║ {:<10} ║ {:<20} ║".format(
            d['No'], d['Nama'][:18], d['Keluhan'][:14], d['BPJS'][:10], d['Waktu']
        ))
    print("╚═════╩════════════════════╩════════════════╩════════════╩══════════════════════╝")

# ========== TAMPILKAN ANTRIAN ==========
def tampilkan_antrian():
    print("\n📊 DAFTAR ANTRIAN SAAT INI")
    if not data_bpjs and not data_nonbpjs:
        print("📭 Antrian kosong.")
        return

    print("📌 Antrian BPJS")
    if data_bpjs:
        print_tabel(data_bpjs)
    else:
        print("❌ Tidak ada pasien BPJS")

    print("\n📌 Antrian Non-BPJS")
    if data_nonbpjs:
        print_tabel(data_nonbpjs)
    else:
        print("❌ Tidak ada pasien Non-BPJS")

# ========== TAMPILKAN RIWAYAT ==========
def tampilkan_riwayat():
    print("\n📂 RIWAYAT PASIEN YANG TELAH DIPANGGIL")
    if not os.path.exists(file_riwayat):
        print("❌ Riwayat belum tersedia.")
        return

    with open(file_riwayat, "r") as f:
        lines = f.readlines()
        if not lines:
            print("📭 Riwayat masih kosong.")
            return
        print("{:<5} {:<20} {:<15} {:<10} {:<20} {:<10}".format("No", "Nama", "Keluhan", "BPJS", "Waktu", "Jenis"))
        print("-"*85)
        for line in lines[-15:]:
            no, nama, keluhan, bpjs, waktu, jenis = line.strip().split(",")
            print("{:<5} {:<20} {:<15} {:<10} {:<20} {:<10}".format(no, nama, keluhan, bpjs, waktu, jenis))
# ========== HAPUS PASIEN ==========
def hapus_pasien():
    print("\n🗑 HAPUS PASIEN DARI ANTRIAN")
    if not data_bpjs and not data_nonbpjs:
        print("📭 Antrian kosong.")
        return

    tampilkan_antrian()
    target = input("Masukkan nomor antrian pasien yang ingin dihapus (contoh B1 atau N2): ").upper()
    for antrean in [data_bpjs, data_nonbpjs]:
        for pasien in list(antrean):
            if pasien["No"] == target:
                antrean.remove(pasien)
                print(f"✅ Pasien '{pasien['Nama']}' telah dihapus dari antrian.")
                return
    print("❌ Pasien tidak ditemukan.")

# ========== CARI PASIEN ==========
def cari_pasien():
    print("\n🔎 CARI PASIEN BERDASARKAN NAMA")
    nama_cari = input("Masukkan nama pasien (atau sebagian): ").strip().lower()
    hasil = []
    for antrean in [data_bpjs, data_nonbpjs]:
        for pasien in antrean:
            if nama_cari in pasien['Nama'].lower():
                hasil.append(pasien)

    if hasil:
        print(f"\n✅ Ditemukan {len(hasil)} pasien:")
        print_tabel(hasil)
    else:
        print("❌ Tidak ditemukan pasien dengan nama tersebut.")

# ========== URUTKAN PASIEN BERDASARKAN WAKTU ==========
def urutkan_antrian():
    print("\n📅 MENGURUTKAN ANTRIAN BERDASARKAN WAKTU DAFTAR")
    semua = list(data_bpjs) + list(data_nonbpjs)
    if not semua:
        print("📭 Tidak ada antrian.")
        return
    semua.sort(key=lambda x: x["Waktu"])
    print_tabel(semua)

# ========== STATISTIK PASIEN ==========
def tampilkan_statistik():
    print("\n📈 STATISTIK PASIEN")
    total = len(riwayat_dipanggil)
    total_bpjs = len([p for p in riwayat_dipanggil if p["Jenis"] == "BPJS"])
    total_nonbpjs = total - total_bpjs
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    hari_ini_total = len([p for p in riwayat_dipanggil if p["Waktu"].startswith(hari_ini)])

    print(f"📊 Total pasien dilayani     : {total}")
    print(f"📄 Jumlah pasien BPJS        : {total_bpjs}")
    print(f"💰 Jumlah pasien Non-BPJS    : {total_nonbpjs}")
    print(f"🕒 Pasien hari ini           : {hari_ini_total}")
    print(f"📥 Antrian saat ini          : {len(data_bpjs) + len(data_nonbpjs)}")
def export_csv():
    """
    Menyimpan semua data (antrian + riwayat) ke file CSV.
    """
    semua_data = list(data_bpjs) + list(data_nonbpjs) + riwayat_dipanggil
    if not semua_data:
        print("❌ Tidak ada data untuk diekspor.")
        return

    with open(file_export, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["No", "Nama", "Keluhan", "BPJS", "Waktu", "Jenis"])
        for pasien in semua_data:
            writer.writerow([
                pasien['No'], pasien['Nama'], pasien['Keluhan'],
                pasien['BPJS'], pasien['Waktu'], pasien['Jenis']
            ])
    print(f"✅ Semua data berhasil diekspor ke file '{file_export}'.")

# ========== MENU UTAMA ==========
def menu():
    while True:
        clear()
        header()
        cprint("📋 MENU UTAMA                                                             ", "white", "on_white", attrs=["bold"])
        cprint("1️⃣  Tambah Pasien ke Antrian                                               ", "white", "on_white")
        cprint("2️⃣  Panggil Pasien (Manual)                                                ", "white", "on_white")
        cprint("3️⃣  Tampilkan Antrian Saat Ini                                             ", "white", "on_white")
        cprint("4️⃣  Tampilkan Riwayat Pemanggilan                                          ", "white", "on_white")
        cprint("5️⃣  Hapus Pasien dari Antrian                                              ", "white", "on_white")
        cprint("6️⃣  Urutkan Antrian Berdasarkan Waktu                                      ", "white", "on_white")
        cprint("7️⃣  Cari Pasien Berdasarkan Nama                                           ", "white", "on_white")
        cprint("8️⃣  Tampilkan Statistik Pasien                                             ", "white", "on_white")
        cprint("9️⃣  Export Semua Data ke CSV                                               ", "white", "on_white")
        cprint("0️⃣  Keluar dari Program                                                    ", "white", "on_white", attrs=["bold"])
        garis()

        try:
            pilihan = input("📥 Pilih menu (0–10): ").strip()
            if pilihan == "1":
                tambah_pasien()
            elif pilihan == "2":
                panggil_pasien()
            elif pilihan == "3":
                tampilkan_antrian()
            elif pilihan == "4":
                tampilkan_riwayat()
            elif pilihan == "5":
                hapus_pasien()
            elif pilihan == "6":
                urutkan_antrian()
            elif pilihan == "7":
                cari_pasien()
            elif pilihan == "8":
                tampilkan_statistik()
            elif pilihan == "9":
                export_csv()
            elif pilihan == "0":
                print("👋 Terima kasih telah menggunakan sistem antrian RSUD Pantai Cermin.")
                print("💖 Semoga lekas sembuh dan sehat selalu.")
                break
            else:
                print("⚠ Pilihan tidak tersedia.")
        except Exception as e:
            print(f"⚠ Terjadi kesalahan: {e}")
        pause()

# ========== JALANKAN PROGRAM ==========

try:
    menu()
except KeyboardInterrupt:
    print("\n🛑 Program dihentikan oleh pengguna.")