sozluk = {"kitap":"book", "bilgisayar":"computer", "programlama":"programing"}

def ara(sozcuk):
    hata="{} kelimesi sözlükte yok!"
    return sozluk.get(sozcuk, hata.format(sozcuk))
