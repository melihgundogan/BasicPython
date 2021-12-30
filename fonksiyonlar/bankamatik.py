# Bankamatik Uygulaması  (Para yatırmalı halini halini yapabilirsin.) Ek hesapta faiz de ekleyebilirsin. örneğin 20 günlük kullanımdan sonra para yatırıldı o parayı 20 günlük faiz uygulayarak bakiye den düşürülebilir

SadikHesap={
    "ad":"Sadık Turan",
    "hesapNo":"13245678",
    "bakiye":3000,
    "ekHesap":2000
}

AliHesap={
    "ad":"Ali Turan",
    "hesapNo":"13245456",
    "bakiye":2000,
    "ekHesap":1000
}

def paraCek(hesap,miktar):      #hesap para çekmek istediğimiz hesap miktar ise ne kadar çekmek istediğimizi içeriyor
    print(f"Merhaba{hesap['ad']}")

    if(hesap["bakiye"]>=miktar):
        hesap["bakiye"]-=miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']    
        
        if (toplam>=miktar):
            ekHesapKullanimi=input("Ek hesap  kullanılsın mı(e/h)")

            if ekHesapKullanimi=="e":
                ekHesapKullanilacakMiktar=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"]-=ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz")
                bakiyeSorgula(hesap)

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}bulunmaktadır")   

        else:
            print("Üzgünüz bakiye yetersiz.")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} tl bulunmaktadır")            

paraCek(SadikHesap,3000)

print("**************")

paraCek(SadikHesap,2000)

