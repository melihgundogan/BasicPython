#1-100 e kadar

#x=1

#while x<=100:
#    if x%2==1:  #tekleri yazdırmak için 1 çiftleri yazdırmak için 0
#       print(f"sayı tek: {x}")
#    else:
#        print(f"sayı çift {x}")    
#    x += 1
#print("bitti")    

name="" #false
while not name.strip():    #strip boşluk ifadeleri silmektedir
    name=input("isminizi giriniz: ")

print(f"Merhaba {name}")
