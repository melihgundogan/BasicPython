numbers= [1,10,15,25,35,10]
letters= ["a","g","e","a","s","z"]

val= min(numbers)
val= max(numbers)
val= max(letters)
val= min(letters)

val= numbers[3:6]
val= numbers[:3]

numbers[4]= 50

numbers.append(49)      #listeye ekleme append en sona ekler
numbers.insert(3,78)    #insert ile istediğimiz yere bir eleman ekleyebiliriz
numbers.insert(-1,52)

#numbers.pop()
#numbers.pop(0)
#numbers.remove(1)
numbers.sort()  #listeyi küçükten büyüğe sıralar
#letters.sort()  
numbers.reverse()  #sort tan sonra bu ifade ile büyükten küçüğe sıralarız

print(len(numbers)) #kaç eleman olduğu
print(numbers.count(10)) #o elemanın kaç tane olduğuu buldurur

numbers.clear() #listeyi silmeye yarar

print(numbers)
print(letters)