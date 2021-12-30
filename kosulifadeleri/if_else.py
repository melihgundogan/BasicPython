#if 3>2:
#    print("HOŞ GELDİNİZ")

#if 3>4:
#    print("HOŞ GELDİNİZ")

username= "melih"
password="1234"

#isLoggedin = (username== "melih") and (password=="124")    #bunu direkt if ten sonra da yazabiliriz illa bir ifadenin içine yazdırmamıza gerek yoktur

#if isLoggedin:     # Doğru olunca hoş geldiniz mesajıı bize yazdırır ama eğer false ise bize hiçbir şey yazdırmaz
    #print("Hoş geldiniz")
#else :
   #print("username ya da password yanlış")    

if (username== "melih"):
    if (password=="1234"):
        print("Hoş geldiniz")
    else:
        print("password yanlış")   
else:
    print("username yanlış")         