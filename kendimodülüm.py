"""
sozluk.py dosyası bizim yazdığımız bir moduldür.Bu modul 3. şahıs modulleri diye geçer.
Diğer standart moduller gibi kullanılabilir. sozluk.py dosyası aynı dizinde yer aldığı için kullanabiliriz.
eğer diğer dosyalarda da kullanmak istersek pythonun diğer modülleri koyduğu dizine atmamız yeterli olur.
böylece sozluk.py dosyasındaki fonksiyonları kullanabiliriz.Aksi halde hata alırız.
modul dizini için python kabuğumuza
>>> import sys
>>>sys.path
yazarak dizinlere ulaşabiliriz. ulaştığımız bir dizine sozluk.py kopyalayalım.
istersek kendimodülüm.py dosyasıyla aynı dizindeki sozluk.py dosyasını sildiğimiz zaman da hata almayız.
"""
import sozluk

sonuc=sozluk.ara("kitap")
print(sonuc)
