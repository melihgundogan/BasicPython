# Yöntem 1
# import math

# import math as islem

# value=dir(math)
# value=help(math)
# value=help(math.factorial)
# value=math.sqrt(49)
# value=math.factorial(5)
# value=math.ceil(5.9)
# value=math.floor(5.9)

# value=islem.factorial(5)

# Yöntem 2
# from math import *

def sqrt(x):    #def eğer import un üstündeyse sqrt bunu kullanır ama import un altındaysa importu kullanır
    print("x :"+ str(x))

from math import factorial,sqrt   # * koyarsak sadece math in tüm işlemlerini kullanabiliriz

value=factorial(5)
value=sqrt(9)

print(value)