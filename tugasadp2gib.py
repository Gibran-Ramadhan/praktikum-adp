lamda_t = float(input("Masukkan nilai λt: "))
m = int(input("Masukkan nilai M : "))
e = 2.71828
n_faktorial = 1 
for n in range(m + 1):
    p = (e ** (-lamda_t)) * ((lamda_t) ** n) / n_faktorial
    n_faktorial *= (n + 1)  
    print(f"Nilai P(N(t) = {n}) = {p}")