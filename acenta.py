ASGARI_UCRET = 2324.70
IKRAMIYE = ASGARI_UCRET/2
danisman_sayisi = int(input("Acentaya bağlı olarak çalışan danışman sayısını giriniz(0'dan büyük): "))
while danisman_sayisi <= 0:
    danisman_sayisi = int(input("hatalı veri, lütfen tekrar giriniz: "))

genel_satilan_konut = 0
genel_satilan_isyeri = 0
genel_satilan_arsa = 0
genel_kiralanan_konut = 0
genel_kiralanan_isyeri = 0
genel_kiralanan_arsa = 0
genel_satilan_konut_bedeli = 0
genel_satilan_isyeri_bedeli = 0
genel_satilan_arsa_bedeli = 0
MAX_bedel = 0
MAX_bedel_danisman = ''
MAX_genel_kiralanan_konut_bedeli = 0
MAX_konut_kiralayan_danisman = ''
asgari_ucretten_yuksek_kira = 0
satis_yapamayan_danisman = 0
MAX_satis_adedi = 0
MAX_satan_danisman = ''
MAX_satan_toplam_bedel = 0
MAX_toplam_bedel = 0
MAX_bedel_satis_adedi = 0
MAX_toplam_bedel_danisman = ''
kota_dolduran_danisman = 0
primi_maasindan_yuksek = 0
yuksek_kiralama_danisman = 0
MAX_prim = 0
MAX_prim_danisman = ''
MAX_prim_maas = 0
MAX_prim_toplam_maas = 0
genel_aylik_toplam_ucret = 0
genel_kazanilan_toplam_komisyon = 0
MIN_prim = 9999999999999999999999
MIN_prim_danisman = ''
MIN_prim_maas = 0
MIN_prim_toplam_maas = 0
MAX_emlak_tipi = ''
for danisman in range(1, danisman_sayisi+1):
    ad_soyad = input("danışmanın adını ve soyadını giriniz: ")
    maas = float(input("danışmanın maaşını giriniz: "))
    while maas < ASGARI_UCRET:
        maas = float(input("hatalı veri,danışmanın maaşını yeniden giriniz: "))
    kota = float(input("danışmanın kotasını giriniz: "))
    while kota < maas*10:
        kota = float(input("hatalı veri,danışmanın kotasını yeniden giriniz: "))
    islem_durumu = "e"
    satilan_konut = 0
    kiralanan_konut = 0
    satilan_isyeri = 0
    kiralanan_isyeri = 0
    satilan_arsa = 0
    kiralanan_arsa = 0
    toplam_satilan_konut_bedeli = 0
    toplam_kiralanan_konut_bedeli = 0
    toplam_satilan_isyeri_bedeli = 0
    toplam_kiralanan_isyeri_bedeli = 0
    toplam_satilan_arsa_bedeli = 0
    toplam_kiralanan_arsa_bedeli = 0
    MAX_kiralanan_konut_bedeli = 0
    kota_durumu = False
    while islem_durumu == "e" or islem_durumu == "E":
        emlak_tipi = input("Emlak tipini giriniz (K/k/İ/i/A/a): ")
        while emlak_tipi not in ['K', 'k', 'İ', 'i', 'A', 'a']:
            emlak_tipi = input("hatalı veri,Emlak tipini yeniden giriniz (K/k/İ/i/A/a): ")
        islem_turu = input("Yapılan işlem türünü giriniz (S/s/K/k):")
        while islem_turu not in ['S', 's', 'K', 'k']:
            islem_turu = input("hatalı veri,Yapılan işlem türünü yeniden giriniz (S/s/K/k):")
        satis_kira_bedeli = float(input("satış/kiralama için alınan bedeli giriniz: "))
        while satis_kira_bedeli <= 0:
            satis_kira_bedeli = float(input("hatalı veri,satış/kiralama için alınan bedeli yeniden giriniz: "))
        satilan_konut_bedeli = 0
        kiralanan_konut_bedeli = 0
        satilan_isyeri_bedeli = 0
        kiralanan_isyeri_bedeli = 0
        satilan_arsa_bedeli = 0
        kiralanan_arsa_bedeli = 0
        if emlak_tipi == 'k' or emlak_tipi == 'K':
            if islem_turu == 's' or islem_turu == 'S':
                satilan_konut += 1
                satilan_konut_bedeli = satis_kira_bedeli
                toplam_satilan_konut_bedeli += satilan_konut_bedeli

            else:
                kiralanan_konut += 1
                kiralanan_konut_bedeli = satis_kira_bedeli
                toplam_kiralanan_konut_bedeli += kiralanan_konut_bedeli

        elif emlak_tipi == 'i' or emlak_tipi == 'İ':
            if islem_turu == 's' or islem_turu == 'S':
                satilan_isyeri += 1
                satilan_isyeri_bedeli = satis_kira_bedeli
                toplam_satilan_isyeri_bedeli += satilan_isyeri_bedeli

            else:
                kiralanan_isyeri += 1
                kiralanan_isyeri_bedeli = satis_kira_bedeli
                toplam_kiralanan_isyeri_bedeli += kiralanan_isyeri_bedeli
        else:
            if islem_turu == 's' or islem_turu == 'S':
                satilan_arsa += 1
                satilan_arsa_bedeli = satis_kira_bedeli
                toplam_satilan_arsa_bedeli += satilan_arsa_bedeli
            else:
                kiralanan_arsa += 1
                kiralanan_arsa_bedeli = satis_kira_bedeli
                toplam_kiralanan_arsa_bedeli += kiralanan_arsa_bedeli

        if kiralanan_konut_bedeli > MAX_kiralanan_konut_bedeli:
            MAX_kiralanan_konut_bedeli = kiralanan_konut_bedeli
        elif satilan_konut_bedeli > MAX_bedel:
            MAX_bedel = satilan_konut_bedeli
            MAX_bedel_danisman = ad_soyad
            if emlak_tipi == 'k' or emlak_tipi == 'K':
                MAX_emlak_tipi = "konut"
        elif satilan_isyeri_bedeli > MAX_bedel:
            MAX_bedel = satilan_isyeri_bedeli
            MAX_bedel_danisman = ad_soyad
            if emlak_tipi == "i" or emlak_tipi == "İ":
                MAX_emlak_tipi = "iş yeri"
        elif satilan_arsa_bedeli > MAX_bedel:
            MAX_bedel = satilan_arsa_bedeli
            MAX_bedel_danisman = ad_soyad
            if emlak_tipi == "a" or emlak_tipi == "A":
                MAX_emlak_tipi = "arsa"

        if kiralanan_konut_bedeli > ASGARI_UCRET:
            asgari_ucretten_yuksek_kira += 1

        islem_durumu = input("danışmanın o ay sattığı/kiraladığı başka emlak var mı? (E/e/H/h): ")
        while islem_durumu not in ['E', 'e', 'H', 'h']:
            islem_durumu = input("Hatalı veri,danışmanın o ay sattığı/kiraladığı başka emlak var mı? (E/e/H/h): ")

    satis_komisyon = (toplam_satilan_konut_bedeli + toplam_satilan_isyeri_bedeli + toplam_satilan_arsa_bedeli) * 4 / 100
    kira_komisyon = toplam_kiralanan_konut_bedeli + toplam_kiralanan_isyeri_bedeli + toplam_kiralanan_arsa_bedeli
    toplam_komisyon = satis_komisyon + kira_komisyon
    prim = toplam_komisyon * 10 / 100
    satilan_emlak = satilan_konut + satilan_isyeri + satilan_arsa
    kiralanan_emlak = kiralanan_konut + kiralanan_isyeri + kiralanan_arsa
    toplam_emlak = satilan_emlak + kiralanan_emlak
    toplam_satilan_emlak_bedeli = toplam_satilan_konut_bedeli + toplam_satilan_isyeri_bedeli + toplam_satilan_arsa_bedeli
    toplam_kiralanan_emlak_bedeli = kira_komisyon
    aylik_toplam_ucret = maas + prim

    if MAX_kiralanan_konut_bedeli > MAX_genel_kiralanan_konut_bedeli:
        MAX_genel_kiralanan_konut_bedeli = MAX_kiralanan_konut_bedeli
        MAX_konut_kiralayan_danisman = ad_soyad
    if satilan_emlak > MAX_satis_adedi:
        MAX_satis_adedi = satilan_emlak
        MAX_satan_danisman = ad_soyad
        MAX_satan_toplam_bedel = toplam_satilan_emlak_bedeli
    if toplam_satilan_emlak_bedeli > MAX_toplam_bedel:
        MAX_toplam_bedel = toplam_satilan_emlak_bedeli
        MAX_bedel_satis_adedi = satilan_emlak
        MAX_toplam_bedel_danisman = ad_soyad

    if prim > maas:
        primi_maasindan_yuksek += 1
    if satilan_emlak <= 0:
        satis_yapamayan_danisman += 1
    if kiralanan_emlak >= 10 or toplam_kiralanan_emlak_bedeli >= 25000:
        yuksek_kiralama_danisman += 1
    if toplam_komisyon >= kota:
        aylik_toplam_ucret += IKRAMIYE
        kota_dolduran_danisman += 1
        kota_durumu = True

    genel_satilan_konut += satilan_konut
    genel_satilan_isyeri += satilan_isyeri
    genel_satilan_arsa += satilan_arsa
    genel_kiralanan_konut += kiralanan_konut
    genel_kiralanan_isyeri += kiralanan_isyeri
    genel_kiralanan_arsa += kiralanan_arsa
    genel_satilan_konut_bedeli += toplam_satilan_konut_bedeli
    genel_satilan_isyeri_bedeli += toplam_satilan_isyeri_bedeli
    genel_satilan_arsa_bedeli += toplam_satilan_arsa_bedeli
    genel_aylik_toplam_ucret += aylik_toplam_ucret
    genel_kazanilan_toplam_komisyon += toplam_komisyon

    if prim > MAX_prim:
        MAX_prim = prim
        MAX_prim_danisman = ad_soyad
        MAX_prim_maas = maas
        MAX_prim_toplam_maas = aylik_toplam_ucret
    if prim < MIN_prim:
        MIN_prim = prim
        MIN_prim_danisman = ad_soyad
        MIN_prim_maas = maas
        MIN_prim_toplam_maas = aylik_toplam_ucret

    print(danisman, ".danışmanın adı soyadı:", ad_soyad)
    print(danisman, ".danışmanın o ay; sattığı emlak adedi:", satilan_emlak, ',', "kiraladığı emlak adedi:", kiralanan_emlak, "ve oranları:%", satilan_emlak*100/toplam_emlak, ',', "%", kiralanan_emlak*100/toplam_emlak)
    print(danisman, ".danışmanın o ay sattığı konutların toplam bedeli:", toplam_satilan_konut_bedeli, "TL")
    print(danisman, ".danışmanın o ay sattığı isyerlerinin toplam bedeli:", toplam_satilan_isyeri_bedeli, "TL")
    print(danisman, ".danışmanın o ay sattığı arsaların toplam bedeli:", toplam_satilan_arsa_bedeli, "TL")
    print(danisman, ".danışmanın o ay kiraladığı konutların ortalama kira bedeli:", toplam_kiralanan_konut_bedeli/kiralanan_konut, "TL")
    print(danisman, ".danışmanın o ay en yüksek bedelle kiraladığı konutun kira bedeli:", MAX_kiralanan_konut_bedeli, "TL")
    print(danisman, ".danışmanın o ayki maaşı:", maas, "TL")
    print(danisman, ".danışmanın o ayki primi:", prim, "TL")
    print(danisman, ".danışmanın o ayki kotası:", kota, "TL")
    print(danisman, ".danışmanın o ay acenteye kazandırdığı toplam komisyon tutarı:", toplam_komisyon, "TL")
    if kota_durumu:
        print(danisman, ".Danışman,kotasını doldurmuştur.")
        print(danisman, ".Danışmanın aldığı ikramiye miktarı:", IKRAMIYE, "TL")
    else:
        print(danisman, ".Danışman,kotasını doldurmamıştır.")
    print(danisman, ".danışmanın o ayki toplam ücreti:", aylik_toplam_ucret, "TL")

genel_satilan_kiralanan_emlak = genel_satilan_konut + genel_satilan_isyeri + genel_satilan_arsa + genel_kiralanan_arsa + genel_kiralanan_isyeri + genel_kiralanan_konut

print("o ay satılan toplam konut sayısı:", genel_satilan_konut, "ve satılma oranı:%", genel_satilan_konut*100/genel_satilan_kiralanan_emlak)
print("o ay satılan toplam iş yeri sayısı:", genel_satilan_isyeri, "ve satılma oranı:%", genel_satilan_isyeri*100/genel_satilan_kiralanan_emlak)
print("o ay satılan toplam arsa sayısı:", genel_satilan_arsa, "ve satılma oranı:%", genel_satilan_arsa*100/genel_satilan_kiralanan_emlak)
print("o ay kiralanan toplam konut sayısı:", genel_kiralanan_konut, "ve kiralama oranı:%", genel_kiralanan_konut*100/genel_satilan_kiralanan_emlak)
print("o ay kiralanan toplam iş yeri sayısı:", genel_kiralanan_isyeri, "ve kiralama oranı:%", genel_kiralanan_isyeri*100/genel_satilan_kiralanan_emlak)
print("o ay kiralanan toplam arsa sayısı:", genel_kiralanan_arsa, "ve kiralama oranı:%", genel_kiralanan_arsa*100/genel_satilan_kiralanan_emlak)
print("o ay satılan konutların toplam bedeli:", genel_satilan_konut_bedeli, "TL", "ve ortalaması:", genel_satilan_konut_bedeli/genel_satilan_konut)
print("o ay satılan iş yerlerinin toplam bedeli:", genel_satilan_isyeri_bedeli, "TL", "ve ortalaması:", genel_satilan_isyeri_bedeli/genel_satilan_isyeri)
print("o ay satılan arsaların toplam bedeli:", genel_satilan_arsa_bedeli, "TL", "ve ortalaması:", genel_satilan_arsa_bedeli/genel_satilan_arsa)
print("o ay en yüksek bedelle satılan emlağın tipi:", MAX_emlak_tipi, ',', "satış bedeli:", MAX_bedel, "TL,", "satışı yapan danışmanın adı soyadı:", MAX_bedel_danisman)
print("o ay en yüksek bedelle kiralanan konutun kira bedeli:", MAX_genel_kiralanan_konut_bedeli, 'TL,', "kiralayan danışmanın adı soyadı:", MAX_konut_kiralayan_danisman)
print("o ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı:", asgari_ucretten_yuksek_kira, "ve kiralanan konutlar içindeki oranı:%", asgari_ucretten_yuksek_kira*100/genel_kiralanan_konut)
print("o ay hiç satış yapamayan danışmanların sayısı:", satis_yapamayan_danisman, "ve tüm danışmanlar içindeki oranı:%", satis_yapamayan_danisman*100/danisman_sayisi)
print("o ay satış adeti olarak en çok satış yapan danışmanın adı soyadı:", MAX_satan_danisman, ',', "sattığı emlak sayısı:", MAX_satis_adedi, "toplam satış bedeli:", MAX_satan_toplam_bedel, "TL")
print("o ay satış bedeli olarak en çok satış yapan danışmanın adı soyadı:", MAX_toplam_bedel_danisman, ',', "sattığı emlak sayısı:", MAX_bedel_satis_adedi, "toplam satış bedeli:", MAX_toplam_bedel, "TL")
print("o ay kotasını dolduran danışmanların sayısı:", kota_dolduran_danisman, "ve tüm danışmanlar içindeki oranı:%", kota_dolduran_danisman*100/danisman_sayisi)
print("o ay primi maaşından yüksek olan danışmanların sayısı:", primi_maasindan_yuksek, "ve tüm danışmanlar içindeki oranı:%", primi_maasindan_yuksek*100/danisman_sayisi)
print("o ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:", yuksek_kiralama_danisman)
print("o ay en yüksek prim alan danışmanın adı soyadı:", MAX_prim_danisman, ",", "maaşı:", MAX_prim_maas, "TL", ",", "primi:", MAX_prim, "TL", "ve aylık toplam ücreti:", MAX_prim_toplam_maas, "TL")
print("o ay en düşük prim alan danışmanın adı soyadı:", MIN_prim_danisman, ",", "maaşı:", MIN_prim_maas, "TL", ",", "primi:", MIN_prim, "TL", "ve aylık toplam ücreti:", MIN_prim_toplam_maas, "TL")
print("o ay tüm emlak danışmanlarına ödenecek toplam ücretlerin toplamı", genel_aylik_toplam_ucret, "TL", "ve ortalaması:", genel_aylik_toplam_ucret/danisman_sayisi, "TL")
print("o ay acentenin kazandığı toplam komisyon:", genel_kazanilan_toplam_komisyon, "TL")
