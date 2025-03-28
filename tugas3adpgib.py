print("Selamat datang di sistem reservasi tiket konser!")
m = 16  
n = 5  
total_kursi = m * n


print("\nTampilan Layout Kursi")
for i in range(1, total_kursi+1):
    print(i, end=" ")
    if i % n == 0:
        print()  
        i += 1

print("\nHarga Tiket:")
print("VVIP    Rp 1.500.000")
print("VIP     Rp 1.000.000")
print("Reguler Rp   750.000")
print("Ekonomi Rp   500.000")

jumlah_pemesanan=int(input("\nMasukkan jumlah tiket yang ingin dipesan : "))

terpesan_vvip = 0
terpesan_vip = 0
terpesan_reguler = 0
terpesan_ekonomi = 0
kosong = ","
for i in range(1, jumlah_pemesanan + 1):
    print(f"\nPemesanan ke-{i}")
    nama = input("Masukkan nama Anda: ")
    no_kursi = int(input("Masukkan nomor kursi yang ingin dipesan : "))
    password = input("Buat password untuk akses konser : ")
    if 1 <= no_kursi <= 10:
        kategori = "VVIP"
        harga_tiket = 1500000
        terpesan_vvip += 1
    elif 11 <= no_kursi <= 25:
        kategori = "VIP"
        harga_tiket = 1000000
        terpesan_vip += 1
    elif 26 <= no_kursi <= 75:
        kategori = "Reguler"
        harga_tiket = 750000
        terpesan_reguler += 1
    elif 76 <= no_kursi <= 80 :
        kategori = "Ekonomi"
        harga_tiket = 500000
        terpesan_ekonomi += 1
    else : 
        print("Kursi Tidak Tersedia")
    kosong += str(no_kursi) + ","
    print("\n=== Struk Pemesanan Tiket ===")
    print("Nama:",nama)
    print("Nomor Kursi:",no_kursi)
    print("Kategori:",kategori)
    print("Harga: Rp",harga_tiket)
    print("Password:",password)
    print("--------------------------------")

print("\nSisa kursi per kategori")
sisa_vvip = 10 - terpesan_vvip
sisa_vip = 15 - terpesan_vip
sisa_reguler = 50 - terpesan_reguler
sisa_ekonomi = 5 - terpesan_ekonomi
print("VVIP : ",sisa_vvip)
print("VIP : ",sisa_vip)
print("Reguler : ",sisa_reguler)
print("Ekonomi : ",sisa_ekonomi)

print("\nLayout Kursi Setelah Pemesanan:")
for j in range(1, 81):
    if f",{j},"  in kosong :
        print("0", end=" ")
    else:
        print(j, end=" ")
    if j % n == 0 :
        print()
    