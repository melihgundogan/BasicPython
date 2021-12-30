sayilar=[1,3,5,7,9,12,19,21]

#1: sayilar listesini while ile ekrana yazdırın

#i=0
#while (i<len(sayilar)):
#    print(sayilar[i])
#    i+=1

#2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın

#baslangic=int(input("Başlangıç Sayısı Girin: "))
#bitis=int(input("Bitiş Sayısını Girin: "))

#i=baslangic
#while i<bitis:
#    i+=1
#    if i%2==1:
#        print(i)

#3: 1-100 arasındaki sayıları azlan şekilde yazdırın

#i=100
#while i>0:
#    i-=1
#    print(i)

#4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın

#numbers = []

#i=0
#while i<5:
#    sayi=int(input("Sayı giriniz: "))
#    numbers.append(sayi)
#    i+=1
    
#print(numbers)

#5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde ürün sayısını kullanıcıya sorun
#dictionary listesi yapısı(name,price)şeklinde olsun
#ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler=[]

adet=int(input("kaç adet ürün eklemek istiyorsunuz: "))
i = 0 #kontrol değişkeni

while (i <adet):
    name=input("ürün ismi: ")
    price=input("fiyatı: ")
    urunler.append({
        "name":name,
        "price":price
    })
    i+=1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')