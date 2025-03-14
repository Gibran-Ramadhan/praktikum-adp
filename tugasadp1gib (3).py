#Daftar Menu Paket Makanan
print("                                   '-' SELAMAT DATANG '-'                    ")
print("------------------------------------------------------------------------------------------------------")
print("                                     LIST PAKET MAKANAN                                               ")
print("------------------------------------------------------------------------------------------------------")
print("PAKET                                           ISI                                      HARGA        ")
print("a                                       Nasi Goreng, Es Teh                           Rp. 30.000      ")
print("b                               Ayam Bakar, Nasi Putih,  Es Jeruk                     Rp. 50.000      ")
print("c                               Ayam Geprek, Nasi Putih,  Es Teh                      Rp. 45.000      ")
print("d                                      Gulai Ikan, Nasi Putih                         Rp. 35.000      ")
print("e                               Ayam Penyet, Nasi Putih,  Jus Pokat                   Rp. 55.000      ")
print("------------------------------------------------------------------------------------------------------")
print()
print()

#Masukkan Detail Pemesanan
print("               ^^^Detail Pemesanan Anda^^^              ")
nama = input("Nama : ")
no_telepon = int(input("Nomor telepon : "))
alamat = input("Alamat : ")
pesanan = input("Paket yang ingin dipesan : ")
jumlah = int(input("Jumlah paket yang ingin dipesan : "))

#Harga Tiap Paket
a = 30000
b = 50000
c = 45000
d = 35000
e = 55000

#Menentukan Pesanan dan Harga
if pesanan == "a" : 
  p = ("Nasi Goreng, Es Teh")
  harga = jumlah*a
elif pesanan == "b" : 
  p = ("Ayam Bakar, Nasi Putih,  Es Jeruk")
  harga = jumlah*b
elif pesanan == "c" :
  p = ("Ayam Geprek, Nasi Putih,  Es Teh")
  harga = jumlah*c
elif pesanan == "d" :
  p = ("Gulai Ikan, Nasi Putih")
  harga = jumlah*d
else : #pesanan == e
  p = ("Ayam Penyet, Nasi Putih,  Jus Pokat")
  harga = jumlah*e
#Menghitung Pajak
pajak = harga*(10/100)
#Menghitung Harga setelah pajak
harga_total= harga+pajak

#Menentukan Biaya Pengiriman
if harga<150000 :
  biaya_pengiriman=25000
else : #harga>=150000
  biaya_pengiriman = 0

#Menentukan Total Biaya
total_biaya = harga_total+biaya_pengiriman
  
#Menampilkan Hasil
print ("***  Struk Pemesanan  ***")
print("Nama                        :", nama)
print("Nomor Telepon               :", no_telepon)
print("Alamat Pengiriman           :", alamat)
print("Detail Pesanan              : Paket",pesanan,"{",p,"}")
print("Jumlah paket yang dipesan   :", jumlah)
print("Total Harga                 :", harga)
print("Pajak (10%)                 :", pajak)
print("Biaya Pengiriman            :", biaya_pengiriman)
print("Total Biaya                 :", total_biaya)
print("-----------------------Terima Kasih--------------------------")

