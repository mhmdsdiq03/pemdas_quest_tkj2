print("1. persegi panjang")

panjang= int(input("masukan nilai panjang: "))
lebar= int(input("masukan nilai lebar: "))
luas_pp= panjang * lebar

print("luas persegi panjang adalah:  ", luas_pp)
 
print("2. segitiga")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi "))
luas_s = alas * tinggi / 2 # or 1/2 * alas * tinggi 
print("luas segitiga adalah", luas_s)

print("3.lingkaran")

r = int(input("masukan jari-jari: "))
keliling = 2 * 3.14 * r 
luas = 3.14 * r * r 
print("keliling =", keliling)
print("luas =", luas)

print("\n4.jajar genjang")

alas = float(input("masukan nilai alas: "))
tinggi = float(input("masukan nilai tinggi "))
luas_jg = alas * tinggi

print("luas jajargenjang adalah", luas_jg)

