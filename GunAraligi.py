__author__="Cennet Ceylan"

print("Merhaba Dünya")

while True:
    print("Sabah (1)")
    print("Öğle (2)")
    print("Akşam (3)")
    print("Gece(4)")
    print("-----------------------")
    print

    secim= input("Gün içerisindeki zaman dilimini giriniz...:")
    isim= input(" İsminiz:")

    if secim=="1":
        print("Günaydın", isim)
        print

    elif secim == "2":
        print("Tünaydın", isim)
        print

    elif secim == "3":
        print("İyi Akşamlar", isim)
        print

    elif secim == "4":
        print("İyi Geceler", isim)
        print
    else:
        print("Gün aralığı geçersiz.Program sonlandırılıyor.....")
        break



