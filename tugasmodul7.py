def hitung_nilai_akhir(pretest, postest, tugas, bonus):
    return 0.25 * pretest + 0.25 * postest + 0.5 * tugas + bonus

def input_praktikan(n):
    data = []
    for i in range(n):
        print(f"\nPraktikan ke-{i+1}")
        nama = input("Nama: ")
        nim = input("NIM: ")
        pre = float(input("Nilai Pretest: "))
        post = float(input("Nilai Postest: "))
        tugas = float(input("Nilai Tugas/Makalah: "))
        bonus = float(input("Nilai Bonus: "))
        nilai = hitung_nilai_akhir(pre, post, tugas, bonus)
        data.append([nama, nim, nilai])
    return data

def urutkan_data(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][2] < data[j][2]:
                data[i], data[j] = data[j], data[i]
    return data 
def tampilkan(data):
    total = 0
    print(f"\n| {'Nama':<15} | {'NIM':<10} | {'Nilai Akhir':<12} | {'Peringkat':<9}|")
    print("----------------------------------------------------------")
    for i in range(len(data)):
        nama = data[i][0]
        nim = data[i][1]
        nilai = data[i][2]
        print(f"| {nama:<15} | {nim:<10} | {nilai:<12} | {i+1:<9}|")
        total += nilai
    rata2 = total / len(data)
    print("----------------------------------------------------------")
    print(f"| {'Rata-rata nilai akhir :':<15}      | {rata2:<12}            |")
    print("----------------------------------------------------------")

# Program Utama
jumlah = int(input("Masukkan jumlah praktikan: "))
praktikan = input_praktikan(jumlah)
praktikan = urutkan_data(praktikan)
tampilkan(praktikan)