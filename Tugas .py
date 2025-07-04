def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol!"

# Menu kalkulator
def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    pilihan = input("Pilih operasi (1/2/3/4): ")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        print("Hasil:", tambah(a, b))
    elif pilihan == "2":
        print("Hasil:", kurang(a, b))
    elif pilihan == "3":
        print("Hasil:", kali(a, b))
    elif pilihan == "4":
        print("Hasil:", bagi(a, b))
    else:
        print("Pilihan tidak valid.")

# Contoh penggunaan
kalkulator()
