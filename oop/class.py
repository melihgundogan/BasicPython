#class

class Person:
    #pass   #yer tutucu olarak tanımladık
    #class attributes  => tanımlanacak olan ifadeler bu ikisidir
    address="no information"
    #constructor(yapıcı method)
    def __init__(self,name,year):  #self anlamı class tan üretilen bir objeyi belirtmektedir
        #object attributes
        self.name=name
        self.year=year
        print("init metodu çalıştı")

    #methods    => tanımlanacak olan ifadeler bu ikisidir


#object , (instance)

p1=Person(name="ali",year=1999)  #p1 objesi tanımlamış olduk bu sayede attributes ve methodlara ulaşabileceğiz
p2=Person(name="yağmur",year=1998)

#updating
p1.name="melih"
p1.address="İstanbul"

#accessing object attributes
print(f"p1 = name: {p1.name} year: {p1.year} address: {p1.address} ")
print(f"p2 = name: {p2.name} year: {p2.year} address: {p2.address} ")
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)