"""
Soru: Girilen bir sayının asal olup olmadığını bulun.
"""

sayi=int(input("Asal olup olmadığını öğrenmek istediğiniz sayı: "))

asalmi=True

if sayi==1:
    print("1 sayısı asal sayı değildir.")

for i in range(2,sayi):
    if (sayi%i==0):
        asalmi=False
        break 

if asalmi:
    print("Sayı asal bir sayıdır")       
else:
    print("Sayı asal sayı değildir")    