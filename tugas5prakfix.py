print("-------- PROGRAM MENGHITUNG JARAK TITIK --------")
n = int(input("Masukkan jumlah titik : "))
titik = []
i = 0
while i < n:
    print("Titik ke-" + str(i+1))
    x = float(input("Masukkan nilai x : "))
    y = float(input("Masukkan nilai y : "))
    titik.append([x, y])
    i = i + 1

print("\nDaftar titik:")
i = 0
while i < n:
    print("  Titik", i+1, "=", titik[i])
    i = i + 1
print()

print("Jarak antar titik:")
i = 0
while i < n:
    j = i + 1
    while j < n:
        dx = titik[j][0] - titik[i][0]
        dy = titik[j][1] - titik[i][1]
        jarak = (dx*dx + dy*dy)**0.5
        print(f"  Jarak titik 0{i+1} ke 0{j+1} = {jarak}")
        j = j + 1
    i = i + 1
print()
print("Program selesai.")