# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def yazdir(kelime,adet):
#     print(kelime*adet)

# yazdir("Merhaba\n",10)    

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

# def listeyeCevir(*params):    # * olursa sınırsız sayıda parametre olduğu ifade eilir
#     liste=[]

#     for param in params:
#         liste.append(param)

#     return liste

# result=listeyeCevir(10,20,30,"Merhaba")
# print(result)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun. 

# sayi1=int(input("sayı 1 : "))
# sayi2=int(input("sayı 2 : "))

# def asalSayıBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi %i==0):
#                     break
#                 else:
#                     print(sayi)

# asalSayıBul(sayi1,sayi2)                  
                
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def tamBolenBul(sayi):
    tamBolen=[]

    for i in range(2,sayi):
        if (sayi%i==0):
            tamBolen.append(i)
    return tamBolen        

print(tamBolenBul(20))




