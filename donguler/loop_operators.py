#range
# for item in range(50,100,20):
#     print(item)

# print(list(range(50,100,20)))  
# 
# #enumerate


# greeting="Hello"
# for index,letter in enumerate(greeting):    2 şekilde kullanılır)
# for item in enumerate(greeting):
#     print(item)
#     # print(f"index: {index} letter: {letter}")
#     for index,letter in enumerate(greeting):


list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]      
print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)    

