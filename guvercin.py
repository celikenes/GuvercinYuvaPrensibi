"""
guvercin: guvercin prensibi hesaplayan fonksiyon
giris, adet: klavyeden girilen iskambil kagit sayisi
out: islem sonucu
mod: mod sonucunu tutar
"""

def guvercin (adet):
    
    mod = adet % 4

    if (mod!=0):
        out = int (adet / 4 ) + 1
        return out
    else:
        out = int (adet / 4 )
        return out

giris = input("iskambil kagit sayisi (5,9,13...): ")
adet = int (giris)
out = guvercin (adet)
print("en az ", str(out), "adet ayni turden kagit vardir")
