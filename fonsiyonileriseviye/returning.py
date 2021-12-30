# def usalma(number):
#     #two= usalma(2)
#     #three= usalma(3)

#     def inner(power):
#         return number ** power

#     return inner    

# two= usalma(2)
# print(two(3))   # 2^3

# three= usalma(3)
# print(three(6))     # 3^6


# def yetki_sorgula(page):
#     def inner(role):
#         if role=="Admin":
#             return "{0} rolünün {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolünün {1} sayfasına ulaşamaz.".format(role,page)
#     return inner
# user1=yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))
            

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi=="toplama":
        return toplam
    else:
        return carpma

toplama=islem("toplama")
carpma=islem("çarpma")

print(toplama(1,2,3,4,5,8))                            
print(carpma(1,2,3,4,5,8)) 