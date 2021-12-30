# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
A=["Bmw","Mercedes","Opel","Mazda"]

# 2-  Liste Kaç elemanlıdır ?
result=len(A)

# 3-  Listenin ilk ve son elemanı nedir ?
result= A[0]
result= A[3]

# 4-  Mazda değerini Toyota ile değiştirin.
A[-1]= 'Toyota'
result= A

# 5-  Mercedes listenin bir elemanı mıdır ?
result= "Mercedes" in A

# 6-  Listenin -2 indeksindeki değer nedir ?
result= A[-2]

# 7-  Listenin ilk 3 elemanını alın.
result= A[:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
A[-2:]=["Toyota","Renault"]
result= A

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result=A+["Audi","Nissan"]

# 10- Listenin son elemanını silin.
del A[-1]
result= A

# 11- Liste elemanlarını tersten yazdırınız.
result= A[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

result=studentA[0]
result=studentC[3][1]

result= f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)      