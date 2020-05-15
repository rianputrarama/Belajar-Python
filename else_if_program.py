# Menentukan bilangan terbesar, diantara inputan pertama dan kedua
# dengan else if

nilai1 = input("Nilai pertama = ")
nilai2 = input("Nilai kedua = ")
# jadikan str ke int nilai1 dan nilai2
bil1 = int(nilai1)
bil2 = int(nilai2)

# menentukan bilangan terbesar
if bil1 > bil2:
    bil_terbesar = bil1
else:
    bil_terbesar = bil2

print("Bilangan terbesar adalah : ", bil_terbesar)