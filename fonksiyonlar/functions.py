def sayHello(name="user"):
    return "Hello "+ name

msg= sayHello("Melih")

print(msg)

def total(num1,num2):
    return num1+num2

result=total(10,20) 
print(result)   


def yasHesapla(dogumYili):
    return 2021-dogumYili

ageMelih=yasHesapla(2000)
ageEmir=yasHesapla(2011)    

print(ageEmir,ageMelih)

def EmekliligeKacYilKaldi(dogumYili,isim):
    """
    DOCSTRING: Doğum yiliniza gore emekliliğinize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas =yasHesapla(dogumYili)
    emeklilik=65-yas

    if emeklilik>0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Emekli oldunuz") 

EmekliligeKacYilKaldi(1983, "Ali")           
EmekliligeKacYilKaldi(1953, "Ali")        

print(help(EmekliligeKacYilKaldi))

list=[1,2,3]

print(help(list.append))