""" Bu örnekte isimler.txt dosyası C diskinin altındaki müşteriler dizinin içindeki nisan dizini onin içindedir.
içeriği ise

Ahmet Yilmaz  : 0555 111 11 11
Murat Can     : 0555 222 22 22
Vildan Poyraz : 0555 333 33 33

bu şekildedir.
"""

rehber=open("C:\\müşteriler\\nisan\\isimler.txt","r")
"""
sonuc=rehber.read()       #isimler adlı dosyayı okumak için gerekli fonk.
print(sonuc)

alttaki satırla aynı anda çalışmıyor. bu nedenle yorum satırı olarak kullandım."""

"""
sonucbir=rehber.readline()   #ilk satırını yazdırır.

print(sonucbir)
 """

sonuciki=rehber.readlines()   #liste halinde yazdırır.

print(sonuciki)
 
