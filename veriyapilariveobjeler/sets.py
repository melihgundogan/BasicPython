fruits = {"orange","apple","banana"}

#print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"])    #apple zaten var sadece 1 tane görünür 


fruits.remove("mango")
fruits.discard("apple")
fruits.pop()    #normalde son elemanı siler ama hangi elemanın son eleman olduğunu bilmediğimizden pek kullanışlı değildir
fruits.clear()
print(fruits)


#myList=[1,2,3,4,5,6]
#print(myList)
#print(set(myList))

