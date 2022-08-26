print("1.balok")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))

print("2.limas")

alas = int(input("masukan nilai luas alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_la = 1/3 * alas * tinggi
print("volume limas adalah", volume_la)

print("3\ntabung")

luas_alas_lingkaran = int(input("masukan luas alas lingkaran"))
tinggi = int(input("masukan nilai tinggi"))

volume_ling = luas_alas_lingkaran * tinggi
print("nilai volume tabung adalah", volume_ling)

kursDolar = 14000
rupiah = float(input("masukan uang rupipah= "))
rupToDol = rupiah/ kursDolar
dolDecimal = round(rupToDol, 2)
print("Rp.", rupiah, "==> US$", dolDecimal )