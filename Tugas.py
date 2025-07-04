def konversi_suhu(celcius):
    reamur = (4/5) * celcius
    fahrenheit = (9/5) * celcius + 32
    kelvin = celcius + 273.15

    print(f"Celcius    : {celcius}°C")
    print(f"Reamur     : {reamur:.2f}°Re")
    print(f"Fahrenheit : {fahrenheit:.2f}°F")
    print(f"Kelvin     : {kelvin:.2f}K")

# Contoh penggunaan
suhu = float(input("Masukkan suhu dalam Celcius: "))
konversi_suhu(suhu)
