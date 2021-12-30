class Hekim:
    '''Hekim sınıfı oluşturup,özellikleri atanmıştır.'''

    def __init__(self, hekimNo, tcNo, isim, soyisim, telefon_numarası, email):
        self.hekimNo = hekimNo
        self.tcNo = tcNo
        self.isim = isim
        self.soyisim = soyisim
        self.telefon_numarası = telefon_numarası
        self.email = email


class Hasta:
    '''Hasta sınfı oluşturup,özellikleri atanmıştır.'''

    def __init__(self, tcNo, isim, soyisim, telefon_numarası, email):
        self.tcNo = tcNo
        self.isim = isim
        self.soyisim = soyisim
        self.telefon_numarası = telefon_numarası
        self.email = email

    def bilgiler(self):
        return self.tcNo + ' ' + self.isim + ' ' + self.soyisim + ' ' + self.telefon_numarası +' '+ self.email


Hekimler = open('Hekimler.txt', 'w')
RandevuD = open('RandevuD.txt', 'w')
HastaD = open('HastaD.txt', 'w')
RandevuD.close()
HastaD.close()
H1 = '123 23232323232 Ali KUL 507 234 34 34 ali@kul.com\n'
H2 = '124 24242424242 Alper KUL 506 234 34 34 alper@kul.com'
Hekimler.write(H1)
Hekimler.write(H2)
Hekimler.close()


def HastaKontrolEt(tc):
    HastaD = open('HastaD.txt', 'r')
    icindekiler=HastaD.readlines()
    HastaD.close()
    if(len(icindekiler)!=0):
        for i in icindekiler:
            if i[0:12] == tc:
                return True
            else:
                return False
    else:
        return False


def RandevuKontrolEt(hekim,tarih):
    RandevuD = open('RandevuD.txt', 'r')
    icindekiler = RandevuD.readlines()
    RandevuD.close()

    if len(icindekiler)!=0:
        for i in icindekiler:
            bilgiler = i.split(' ')
            if bilgiler[1] == hekim and bilgiler[2]==tarih:
                return False
        else:
            return True
    else:
        return True

def hastaKayıt():
    isim = input("İsminizi giriniz:")
    soyisim = input("Soyisminizi giriniz:")
    telefon_numrasıı = input("Telefon numaranızı giriniz:")
    mail = input("E-mail giriniz:")
    f = Hasta(tc, isim, soyisim, telefon_numrasıı, mail)
    HastaD = open('HastaD.txt', 'a')
    HastaD.write(f.bilgiler())
    HastaD.close()

while True:

    hekim_no = input("Hekim numarasını giriniz:")
    randevu_günü = input("Randevu gününü giriniz:")

    if(RandevuKontrolEt(hekim_no,randevu_günü)):
        print('Randevu verilebilir.')
        tc = input("TC kimlik numaranızı giriniz:")
        if (HastaKontrolEt(tc)==False):
            hastaKayıt()
            RandevuD = open('RandevuD.txt', 'a')
            RandevuD.write(tc+' '+hekim_no+' '+randevu_günü)
            RandevuD.close()
            print('Randevu Bilgileriniz Kayıt edilmiştir.')

        else:
            print('Bilgileriniz sistemimizde kayıtlıdır')
    else:
        print('Hekimimiz o tarihte doludur')