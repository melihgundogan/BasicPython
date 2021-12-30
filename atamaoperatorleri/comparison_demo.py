#1-)Girilen 2 sayıdan hangisi büyüktür

#a=int(input("1.sayı: "))
#b=int(input("2.sayı: "))
#result = (a>b)
#print(f"a: {a} b: {b} den büyüktür: {result}")

#2-)Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın

#a=float(input("1.Vize Notu: "))
#b=float(input("2.Vize Notu: "))
#c=float(input("Final Notu: "))

#ortalama= (((a+b)/2) *60/100)+(c * 40/100)

#print(f"not ortalamanız {ortalama} ve dersten geçme durumunuz: {ortalama >=50}")

#3-)Girilen bir sayının tek mi çift mi olduğunu yazdırın

#sayı=int(input("sayı: "))

#tekcift=(sayı%2==0)

#print(f"girilen sayı çift olma durumu : {tekcift}")

#4-)Girilen bir sayının negatif veya pozitif durumun yazdırın

#sayı=int(input("sayı: "))

#pozitifmi=(sayı > 0)

#print(f"girilen sayının pozitif olma durumu: {pozitifmi}")

#5-)Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz (email: m.melih@gmail.com password: a123a)
email= "m.melih@gmail.com" 
password= "a123a"

girilenEmail=input("email: ")
girilenPassword=input("password: ")

isEmail= email == girilenEmail
isPassword= password ==girilenPassword
print(f"email bilgisi eşleşiyor mu : {isEmail} ve password eşleşiyor mu : {isPassword}")

