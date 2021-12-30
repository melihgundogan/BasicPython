# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

#isim=input("İsminizi ve Soyisminizi Giriniz: ")
#yas=int(input("Yaşınızı Giriniz: "))
#egitim=input("Eğitim Durumunuzu Giriniz: ")

#if (yas>=18):
#    if (egitim=="lise" or egitim=="üniversite"):
#        print(f"{isim} ehliyet alabilirsiniz")
#    else:
#        print(f"{isim} ehliyet alamazsınız çünkü eğitim durumunuz yetersiz")    
#else:
#    print(f"{isim} Ehliyet alamazsınız çünkü yaşınız tutmuyor")    


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

#yazili_1=float(input("1.Yazılı Notunuz: "))
#yazili_2=float(input("2.Yazılı Notunuz: "))
#sozlu=float(input("Sözlü Notunuz: "))

#ortalama=(yazili_1+yazili_2+sozlu)/3

#if (ortalama >= 0) and (ortalama < 25):
#    print(f"ortalamanız: {ortalama} notunuz: 0")
#elif (ortalama >= 25) and (ortalama < 44):
#    print(f"ortalamanız: {ortalama} notunuz: 1")   
#elif (ortalama >= 45) and (ortalama < 54):
#    print(f"ortalamanız: {ortalama} notunuz: 2")
#elif (ortalama >= 55) and (ortalama < 69):
#    print(f"ortalamanız: {ortalama} notunuz: 3")
#elif (ortalama >= 70) and (ortalama < 84):
#    print(f"ortalamanız: {ortalama} notunuz: 4")
#elif (ortalama >= 85) and (ortalama < 100):
#    print(f"ortalamanız: {ortalama} notunuz: 5") 
#else:
#    print("Yanlış bilgi girdiniz")       


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor. (bunu araştırmalıyız)  
#    (simdi) - (2018/8/1) => gün

#days=int(input("aracınız kaç gündür trafiktedir: "))

#if days<=365:
#    print("1.servis aralığı")
#elif days>365 and days<=365*2:
#    print("2.servis aralığı")
#elif days>365*2 and days<=365*3:
#    print("3.servis aralığı")    
#else:
#    print("Hatalı süre")

#datetime

import datetime

tarih=input("aracınız hangi tarihte trafiğe çıktı (2019/8/9):")
tarih=tarih.split("/")
#print(tarih[0])
#print(tarih[1])
#print(tarih[2])
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days

if days<=365:
    print("1.servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı")
elif days>365*2 and days<=365*3:
    print("3.servis aralığı")    
else:
    print("Hatalı süre")



