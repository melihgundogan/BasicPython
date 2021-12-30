# def cube():
#     for i in range(5):
#         yield i**3  # Bir yerde saklanmıyor sadece üretildiği anda saklanıyor bu da generator oluyor bellekte yer tutmuyor

# for i in cube():
#     print(i)


liste=[i*3 for i in range(5)]
print(liste)

liste=(i*3 for i in range(5))
print(liste)

for i in liste:
    print(i)

# print(next(liste))
# print(next(liste))
# print(next(liste))