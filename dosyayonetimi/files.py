# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) Yazma Modu => Dosyayı konumda oluşturur
# Mevcutta dosya varsa içeriği siler ve yeniden ekleme yapar

# file=open("newfile.txt","w")
# file=open("C:/users/MELIHGUNDOGAN/desktop/newfile.txt","w")

# file.close()

# file=open("newfile.txt","w",encoding="utf-8")
# file.write("Melih Gündoğan")
# file.close()

# "a": (Append) ekleme => Dosya konumunda yoksa oluşturur

# file=open("newfile.txt","a",encoding="utf-8")
# file.write("\nMelih")
# file.write("Melih\n")
# file.close()

# "x": (Create) oluşturma => Dosya zaten varsa hata verir

# file=open("newfile2.txt","x",encoding="utf-8")
