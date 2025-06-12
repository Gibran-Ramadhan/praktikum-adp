import time
import os
from termcolor import cprint

# Pola gelombang buatan sendiri (bisa diperpanjang atau dimodifikasi)
pola_gelombang = [0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1]

def animasi_bendera(lebar, tinggi):
    for gerak in range(60):  # jumlah frame animasi
        os.system("cls" if os.name == "nt" else "clear")  # bersihkan layar terminal

        # Gambar bagian merah (atas) dari bendera
        for i in range(tinggi // 2):
            offset = pola_gelombang[(gerak + i) % len(pola_gelombang)]
            maju_mundur = " " * (5 + offset)
            cprint(maju_mundur + " " * lebar, "white", "on_red")

        # Gambar bagian putih (bawah) dari bendera
        for i in range(tinggi // 2):
            offset = pola_gelombang[(gerak + i + 1) % len(pola_gelombang)]
            maju_mundur = " " * (5 + offset)
            cprint(maju_mundur + " " * lebar, "white", "on_white")

        # Gambar tiang bendera di bawahnya
        for i in range(10):
            cprint("||", "grey", "on_white")
        time.sleep(0.1)  # jeda waktu antar frame agar terlihat animasinya
animasi_bendera(15, 6)