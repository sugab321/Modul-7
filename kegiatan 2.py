# membuat fungsi dengan parameter

# fungsi dengan 1 parameter
def halo(nama):
    print('Halo', nama)

# fungsi dengan 2 parameter
def luas_segitiga(alas, tinggi):
    luas = int((alas * tinggi) / 2)
    print('Luas Segitiga:', luas)

# fungsi membandingkan 2 nilai
def banding(a, b):
    if a > b:
        print('%s > %s' % (a, b))
    else:
        print('%s < %s' % (a, b))

# memanggil fungsi
halo('budi')
halo('Informatika')
print('------------------------------')
luas_segitiga(8, 6)
print('------------------------------')
banding(4, 5)
banding(5, 4)
