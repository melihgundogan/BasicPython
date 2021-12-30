user="user"
password="1234"
amount=200
A=input('UserId Giriniz: ')
B=input('Password Giriniz: ')
if A==user and B==password:
    print('Giriş Başarılı')
  
    while True:
        print("Para Çekmek İçin 1 e Basınız")
        print("Para Yatırmak İçin 2 ye Basınız")
        print("Bakiye Görüntülemek İçin 3 e Basınız")
        print("Çıkış İçin 4 e Basınız")
        secim=input()
    
        if secim=="1":
            tutar=input("Çekmek İstediğiniz Tutarı Giriniz")
            tutar=int(tutar)
        
            if tutar>=200:
                print('Yetersiz Bakiye')
        
            elif tutar<=200:
                amount=amount-tutar
                print(amount)

        elif secim=="2":
            tutar=input("Yatırmak İstediğiniz Tutarı Giriniz")  
            tutar=int(tutar)
            amount=amount+tutar
            print(amount)
        
        elif secim=="3":
            print("Bakiyeniz",amount)  
        
        elif secim=="4":
            print('Çıkış Gerçekleştirildi')
            break

        else:
            print("Yanlış Bir İşlem Gerçekleştirildi")

else:
  print('Giriş Başarısız')