"""
    Daire alanı : pi*r^2
    Daire çevresi : 2*pi*r

    * Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)
"""

pi = 3.14

r = float(input("yarı çap:"))

alan = pi * (r ** 2)
print(type(alan))
cevre = 2 * pi * r
print(type(cevre))
print("alan:" + str(alan) + "çevre:" + str(cevre))
