# Data
mahasiswa = [
    {"nama": "C.Ronaldo", "waktu": 120, "data": 600, "sesi": 4},
    {"nama": "Messi", "waktu": 60, "data": 800, "sesi": 2},
    {"nama": "Neymar", "waktu": 0, "data": 300, "sesi": 3},
    {"nama": "G.Bale", "waktu": 200, "data": 500, "sesi": 10},
    {"nama": "Benzema", "waktu": 30, "data": 900, "sesi": 1},
    {"nama": "Modric", "waktu": 180, "data": 200, "sesi": 20},
    {"nama": "Toni Kroos", "waktu": 10, "data": 500, "sesi": 5}
]

# Fungsi klasifikasi
def klasifikasi(dpm, dps):
    if dpm > 20 or dps > 400:
        return "Sangat Mencurigakan"
    elif dpm > 10 or dps > 200:
        return "Mencurigakan"
    elif dpm > 5 or dps > 100:
        return "Berat"
    else:
        return "Normal"

# Hitung semua
i = 0
while i < len(mahasiswa):
    w = mahasiswa[i]["waktu"]
    d = mahasiswa[i]["data"]
    s = mahasiswa[i]["sesi"]

    if w > 0:
        dpm = d / w
    else:
        dpm = 0

    if s > 0:
        dps = d / s
    else:
        dps = 0

    mahasiswa[i]["dpm"] = dpm
    mahasiswa[i]["dps"] = dps
    mahasiswa[i]["status"] = klasifikasi(dpm, dps)

    i += 1

# Ranking manual
ranking = mahasiswa.copy()
n = len(ranking)

for i in range(n):
    for j in range(i+1, n):
        skor_i = ranking[i]["dpm"] + ranking[i]["dps"]
        skor_j = ranking[j]["dpm"] + ranking[j]["dps"]

        if skor_j < skor_i:
            ranking[i], ranking[j] = ranking[j], ranking[i]

# Tampilkan ranking
print("--- RANKING ---")
i = 0
while i < n:
    print(i+1, ranking[i]["nama"], ranking[i]["status"])
    i += 1

# Cari paling mencurigakan
terburuk = mahasiswa[0]
i = 1

while i < len(mahasiswa):
    skor_i = mahasiswa[i]["dpm"] + mahasiswa[i]["dps"]
    skor_t = terburuk["dpm"] + terburuk["dps"]

    if skor_i > skor_t:
        terburuk = mahasiswa[i]

    i += 1

print("\nPaling mencurigakan:", terburuk["nama"], terburuk["status"])