"""
Diyelim ki bir program yazdınız ve sadece windows ta çalışmasını istiyorsunuz
ve aksi durumda kullanıcıya uyarı vermek istiyorsunuz. Bu senaryoya göre yazacağımız kod bu şekildedir.
"""

import os

if os.name!='nt':      #işletim sistemi windows değilse
    print("Bu programı yalnızca Windows'ta kullanabilirisniz.")
else:
    print("Bu program Windows'ta çalışıyor.")
