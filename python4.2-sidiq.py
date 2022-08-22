print("============")
print("rumus bangun datar")
print("============\n")

print("1. persegi\n")

sisi = int(input("masukan nilai sisi:"))
luas_p = sisi * sisi
print("luas persegi panjang adalah", luas_p)
 
print("2. persegi panjang")
 
panjang= int(input("masukan nilai panjang: "))
lebar= int(input("masukan nilai lebar: "))
luas_pp= panjang * lebar
 
print("luas persegi panjang adalah:  ", luas_pp)
 
print("3. segitiga")
 
alas = int(input("masukan nilai alas: ")) 
tinggi = int(input("masukan nilai tinggi "))
luas_s = alas * tinggi / 2 # or 1/2 * alas * tinggi 
print("luas segitiga adalah", luas_s)