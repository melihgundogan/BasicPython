name="Melih"

#for letter in name:
#    print(letter)

#for letter in name:
#     if letter=="e":
#         break  #döngüyü durdurur
#     print(letter)

#for letter in name:
#    if letter=="e":
#        continue  #o anki döngüyü iptal edip devam eder
#    print(letter)

# x=0
# while x<5:
#     x=x+1  #x+=1 ile aynı ifadeyi verir
#     if x==2:
#         break
#     print(x)
#      #x+=1 ile aynı ifadeyi verir

x=0
result=0
while x<=100:
    x+=1
    if x%2==0:   #sadece tek sayıların toplamını almış olduk
        continue
    result+=x
    
print(f"toplam: {result}")
