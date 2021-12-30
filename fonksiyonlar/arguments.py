# def changeName(n):
#     n="ada"

# name="yiğit"

# changeName(name)
# print(name)

# def change(n):
#     n[0]="istanbul"

# sehirler=["ankara","izmir"]
# #n=sehirler[:]  #slicing yani parçalama işlemi yapılıyor
# change(sehirler[:])

# print(sehirler)

# def add(a,b,c=0):
#     return sum((a,b,c))  #soldan sağa doğru bir toplam almak için kullanılır

# print(add(10,20))    
# print(add(10,20,30))

#-----Bu ifadeyi çoklu işlemlerde kullanmak istersek nasıl kullanırız

# def add(*params):
#     print(params)  
#     return sum((params))  

# print(add(10,20))    
# print(add(10,20,30,22,45,85,1))


# def add(*params):
#     sum=0
#     for n in params:
#         sum=sum+n
#     return sum    
     
# print(add(10,20,25))    
# print(add(10,20,30,22,45,85,1))

def displayUser(**args):
    print(type(args))
    for key , value in args.items():
        print("{} is {}".format(key,value))

displayUser(name="melih",age=20,city="sakarya")
displayUser(name="emir",age=10,city="bitlis",phone="123456")
displayUser(name="muhammed",age=38,city="istanbul",phone="123456",email="muhammed@gmail.com")

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1="value1",key2="value2")   