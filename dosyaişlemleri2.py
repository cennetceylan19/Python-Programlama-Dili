
try:
    rehber=open("C:\\müşteriler\\nisan\\yeniisimler.txt","w")   #yeni isimler adlı dosya oluşturuyoruz w modu ile yazma moduna geçiyoruz.
    kayitlar="""Ahmet Yilmaz  : 0555 111 11 11\n
Murat Can     : 0555 222 22 22\n
Vildan Poyraz : 0555 333 33 33\n
    """
    rehber.write(kayitlar)
except IOError:
    print("bir hata oluştu!!")  #herhangi bir hata durumunda alınabilecek mesaj. 

finally:
    rehber.close()

""" try except finally dosya açık kalmaması için kullanıldı. Açık kalan dosya işletim sistemini meşgul eder."""

#diğer bir dosya kapatma yöntemi aşağıdaki gibidir.
with open("C:\\müşteriler\\nisan\\yeniisimlerbir.txt","w") as dosya:
    dosya.write(kayitlar)
