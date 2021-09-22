
try:
    rehber=open("C:\\müşteriler\\nisan\\yeniisimler.txt","w")   #yeni isimler adlı dosya oluşturuyoruz w modu ile yazma moduna geçiyoruz.
    kayitlar="""Ahmet Yilmaz  : 0555 111 11 11\n
Murat Can     : 0555 222 22 22\n
Vildan Poyraz : 0555 333 33 33
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

with open("C:\\müşteriler\\nisan\\yeniisimler2.txt","a") as dosya:
    dosya.write(kayitlar)
    dosya.write("\nMustafa Yıldız\t: 0555 555 55 55\n")

with open("C:\\müşteriler\\nisan\\yeniisimler2.txt","+r") as dosya:
    dosya.read()    #dosyayı okumak için çünkü sadece okuyabildiğimiz dosyanın ilk satırına gelebiliriz.
    dosya.seek(0)   #dosyanın ilk satırına ulaşmak için
    dosya.write("\nHasan Hüseyin\t: 0555 5555 55\n")
    
with open("C:\\müşteriler\\nisan\\yeniisimler2.txt","+r") as dosya:
    okunanlar=dosya.readlines()
    okunanlar.insert(2,"\nVeli Ahmet\t: 0555 555 55 55\n")  #inser() fonk. kullanılarak listeye yeni bir öğe eklenir.
    dosya.seek(0)   #dosyanın başına gelir.
    dosya.writelines(okunanlar) #Listeyi dosyaya yazmak için kullanılır.            
