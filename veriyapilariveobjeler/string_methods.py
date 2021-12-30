message = "Hello There. My name is Melih Gündoğan."

#message = message.upper() Hepsini büyük harf yapar
#message = message.lower() Hepsini küçük harf yapar
#message = message.title() Hepsinin baş harfi büyük olur
#message = message.capitalize() Sadece ilk harf büyük olur.

#message = message.strip()
#message = message.split(".") Kelimeleri ayırır. Ama eğer splitten sonraki () yerine ifadedeki gibi olursa noktalardan itibaren ayırmaktadır.
#message = "---".join(message)

#index = message.find("Melih") 24 çıkar yani 24. satırdan itibaren bu ifade bulunmaktadır.

#isFound = message.startswith("M") Bu ifade ile başlayıp başlamadığını test eder
#sFound = message.endswith("n") Hangi harfle bittiğini test eder

#message = message.replace("Melih","Muhammed")  Melih yerine Muhammed yazar.
#message = message.replace("ç","c").replace("ö","o").replace("i","ı").replace("ü","u")  Türkçe karakterleri yok etme
#message = message.center(100) İlgili mesajı 100 karakterlik bir yere yerleştirir.Genellikle tam ortalar açıklama kısmını hazırlarken işimize yaramaktadır.

print(message)

