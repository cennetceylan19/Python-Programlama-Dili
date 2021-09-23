#Tkinter modülünü içeri aktarıyoruz.
import tkinter as tk

#bir pencere oluşturalım.
pencere=tk.Tk()

#bu pencereye bir düğme ve etiket ekleyelim.
dugme=tk.Button(text="Düğme")
etiket=tk.Label(text="Etiket")

#şimdi de eklediklerimizi paketleyelim. Görünmesini sağlayalım.
dugme.pack()
etiket.pack()
