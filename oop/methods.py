# #class

# class Person:
#     #pass   #yer tutucu olarak tanımladık
#     #class attributes  => tanımlanacak olan ifadeler bu ikisidir
#     address="no information"
#     #constructor(yapıcı method)
#     def __init__(self,name,year):  #self anlamı class tan üretilen bir objeyi belirtmektedir
#         #object attributes
#         self.name=name
#         self.year=year
        

#     #instance methods    => tanımlanacak olan ifadeler bu ikisidir
#     def intro(self):
#         print("Hello There I am " + self.name)

#     #instance methods
#     def calculateAge(self):
#         return 2021 - self.year

# #object , (instance)

# p1=Person(name="ali",year=1999)  #p1 objesi tanımlamış olduk bu sayede attributes ve methodlara ulaşabileceğiz
# p2=Person(name="yağmur",year=1998)

# p1.intro()
# p2.intro()

# print(f"adım: {p1.name} ve yaşım: {p1.calculateAge()}")
# print(f"adım: {p2.name} ve yaşım: {p2.calculateAge()}")

class Circle:
    #class object attributes  #class seviyesindedir
    pi=3.14

    def __init__(self,yariCap=1):
        self.yariCap=yariCap  #selften sonra farklı bir ifade kullanabliriz kullanımı kolay olsun diye aynı şekilde yazdık

    def cevre_hesapla(self):
        return 2*self.pi * self.yariCap

    def alan_hesapla(self):
        return self.pi * (self.yariCap**2)

c1=Circle() #yarıçapı 1
c2=Circle(5)

print(f" c1 : alan = {c1.alan_hesapla()} ve çevre : {c1.cevre_hesapla()}")
print(f" c2 : alan = {c2.alan_hesapla()} ve çevre : {c2.cevre_hesapla()}")
