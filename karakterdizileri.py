"""
karakter dizileri
"""
kelime="Mutluluk"
tekkelime="huzur"
cokkelime="sen çok yaşa"

print(len(kelime)) #kelime karater dizisinin uzunluğunu verir.

print(kelime[3]) #0'dan başlayarak kelime karakter dizisindeki 3. harfin çıktısını verir.

print(kelime[1:3]) #aralık belirterek kelime karter dizisindeki harflerin çıktısını verir.

print(sorted(kelime)) #kelime karakter dizisindeki karakterleri alfabetik sıralar.

print(tekkelime.replace("h","H")) #replace fonksiyonuyla h karakterini H ile değiştirdi.

print(cokkelime.split())    #karakter dizisini böler.

dortsatir=""" Alp Er Tunga öldü mü?
Issız ajun kaldı mı?
ödlek öçin aldı mu?
Emdi yürek yırtılır."""

print(dortsatir)

print(dortsatir.splitlines())#Satırlara ayırma fonksiyonudur.

print(dortsatir.lower())        # Karakterlerin hepsini küçük harfle yazar.

print(dortsatir.upper())        # Karakterlerin hepsini büyük harfle yazar.

