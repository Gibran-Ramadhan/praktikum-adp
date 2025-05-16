nomor_mahasiswa=[]
nama_mahasiswa=[]
nilai_mahasiswa =[]
while True :
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Tampilkan data")
    print("4. Keluar")
    print()
    pilihan = int(input("Inputkan pilihan : "))

    if pilihan == 1 :
        print("Tambahkan data mahasiswa")
        nomor = int(input("Nomor mahasiswa : "))
        nama = (input("Nama mahasiswa  : "))
        nilai = float(input("Nilai mahasiswa : "))
        nomor_mahasiswa.append(nomor)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("Data berhasil ditambahkan")
        print()

    elif pilihan == 2:
        nomor_hapus = int(input("Masukkan nomor mahasiswa yang ingin dihapus :"))
        if nomor_hapus in nomor_mahasiswa :
            index = nomor_mahasiswa.index(nomor_hapus)
            nomor_mahasiswa.pop(index)
            nama_mahasiswa.pop(index)
            nilai_mahasiswa.pop(index)
            print("Data berhasil dihapuskan")
        else :
            print("Nomor mahasiswa tidak valid")
        print()

    elif pilihan == 3 :
        if len(nomor_mahasiswa) == 0 :
            print("Belum ada data.\n")
        else :
            gabungan = []
            for i in range(len(nomor_mahasiswa)):
                gabungan.append((nomor_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]))
            n = len(gabungan)
            batas = n
            while batas > 1 :
                for i in range(batas - 1) :
                    if gabungan[i][2] < gabungan[i+1][2]:
                        temp = gabungan[i]
                        gabungan[i] = gabungan[i+1]
                        gabungan[i+1] = temp
                batas -= 1
            print("No Mahasiswa     Nama Mahasiswa     Nilai Mahasiswa")
            for data in gabungan :
                print(f" {data[0]:<18}  {data[1]:<18}  {data[2]:<18}")
            print()

    elif pilihan == 4 :
        print("Terima kasih")
        break
    else :
        print("Pilihan tidak valid, silahkan coba lagi")  