# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

#a= int(input("Herhangi bir sayı girin: "))
#result = 0<a<100
#print(f"Girdiğiniz sayı {a} ve bu sayı 0 ile 100 arasındamıdır: {result}")

#**********Hocanın Yaptığı**************
# sayi = float(input('sayı: '))
# result = (sayi > 0) and (sayi<=100)
# print(f'sayı 0-100 arasındamı: {result}')


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

#a= int(input("Herhangi bir sayı girin: "))
#result = (0<a) and (a%2==0)
#print(f"Girdiniz sayı {a} ve bu sayı pozitif midir: {result}")

#**********Hocanın Yaptığı**************
# sayi = int(input('sayı: '))
# result = (sayi > 0) and (sayi % 2 ==0)
# print(f'girilen sayı pozitif çift sayı mı: {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

#email= "melih@gmail.com"
#password= "1907"
#girilenEmail=input("email giriniz: ")
#girilenPassword=input("parolanızı giriniz: ")
#result=(girilenEmail==email) and (girilenPassword==password)
#print(f"Girdiğiniz email ve password uyumlu mu: {result}")

#**********Hocanın Yaptığı**************
# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# result = (girilenEmail == email) and (girilenPassword == password)
# print(f'uygulamaya giriş başarılı mı: {result}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

#a=int(input("1.sayı: "))
#b=int(input("2.sayı: "))
#c=int(input("3.sayı: "))

#result = (a > b) and  (a > c)
#print(f'a en büyük sayıdır : {result}')

#result = (b > a) and (b > c)
#print(f'b en büyük sayıdır : {result}')

#result = (c > a) and (c > b)
#print(f'c en büyük sayıdır : {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
# a-) Ortalama 50 olsa bile final notu 50 olmalıdır
# b-) Finalden 70 alındığında ortalamanın önemi olmasın

#vize1=float(input("1.Vize Notu: "))
#vize2=float(input("2.Vize Notu: "))
#final=float(input("Final Notu: "))

#ortalama = ((((vize1+vize2)/2) *0.6) + (final * 0.4))
#result = (ortalama>=50) and (final>=50)
#result = (ortalama>=50) or (final>=70)
#print(f"Öğrencinin ortalaması : {ortalama} ve geçme durumu :{result}")


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül Kilo / boyun karesi
# 0-18.4  Zayıf
# 18.5-24.9  Normal
# 25.0-29.9  Fazla Kilolu
# 30.0-34.9  Şişman(Obez)

name=input("adınız: ")
weight=float(input("kilonuz: "))
high=float(input("boyunuz: "))

index = (weight) / (high ** 2)

zayif = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")

