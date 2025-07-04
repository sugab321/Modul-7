# Fungsi nilai balik
def luas_persegi(sisi):
    luas = int(sisi * sisi)
    return luas

# Fungsi memanggil fungsi lain
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# Memanggil fungsi
a = volume_persegi(6)
print('Volume Persegi:', a)

# variabel global
a = 1

def fungsi1():
    print(a)

def fungsi2():
    # variabel lokal
    a = 2

def fungsi3():
    # variabel lokal
    a = 3
    print(a)

def fungsi4():
    global a
    # variabel lokal
    a = 4
    print(a)

print('Variabel global =', a)
fungsi1()
print('======================')
print('Variabel global =', a)
fungsi2()
print('======================')
print('Variabel global =', a)
fungsi3()
print('======================')
print('Variabel global =', a)
fungsi4()
print('======================')
print('Variabel global =', a)
