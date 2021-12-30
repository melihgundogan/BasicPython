#x=5
#y=10
#z=20

#x, y, z = 5, 10, 20

#x,y=y,x
#x=x+5
#x += 5  # x=x+5
#x -= 5  # x=x-5
#x *= 5  #çarpma işlemi
#x /= 5  #bölme işlemi
#x %= 5  #mod değeri alma
#x //= 5 #tam bölme
#y **= 5 #üssü alma

#print(x, y, z)

#values= 1,2,3   #eğer 3 ü silersek hata alırız fazla olursa da yine hata alırız
values=1,2,3,4,5
print(values)
print(type(values))

#x,y,z=values    #eğer *z yazarsak values de fazla eleman varsa toplu olarak bir liste şeklinde ele alınır
x,y,*z=values
print(x,y,z)


