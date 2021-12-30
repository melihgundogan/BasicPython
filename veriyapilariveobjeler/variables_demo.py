"""
    1-) Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik no
    Müşteri doğum yılı
    Müşteri adres bilgileri
    Müşteri yaşı
"""
# Cevap
musteriAdi = "Ali"
musteriSoyad = "Yılmaz"
musteriAdSoyad = musteriAdi+' '+musteriSoyad
musteriCinsiyet = True #Erkek veya kadın yazılabilir ama kadın veya erkek varsayılarak true false denilebilir.Zaten alacağı 2 değişken vardır.
musteriTcKimlik = '13525135138'
musteriDogumYili = 1989
musteriAdres = 'Istanbul/Kadıköy'
musteriYasi = 2020 - musteriDogumYili #Herhangi birine printlersek yazdırır.

"""
    2-) Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Sipariş 1 => 110 TL
    Sipariş 2 => 1110.5
    Sipariş 3 => 356.95

"""

order1 = 110 #str bir ifade olarak yazılamaz matematiksel bir işlem yapılmaz
order2 = 1110.5
order3 = 356.95

total = order1 + order2 + order3

print("Total;", total)