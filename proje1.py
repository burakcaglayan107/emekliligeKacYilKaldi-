
print('Merhaba, bu sistem emekli olmanıza kaç yıl kaldığını hesaplar. Emekli olma yaşı 65 alınmıştır.')

while True:
    try:
        kisinin_yasi = int(input('Yasiniz kactir? : '))
        emeklilik_yasi = 65
        emekliligeKalanYil = emeklilik_yasi - kisinin_yasi
        if emekliligeKalanYil <= 0:
            print('Zaten emekli oldunuz.')
            break
        elif emeklilik_yasi - kisinin_yasi > 0:
            print('Emekli olmaniza ' + str(emekliligeKalanYil) + ' yıl kaldı.' )
            break
    
    except ValueError:
        print('Lütfen geçerli bir ifade girin')
