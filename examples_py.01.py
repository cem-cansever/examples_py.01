# ism = input("İsim Girin ... ")
# def selam(isim):
#   return f"Merhaba {isim}"
# print(selam(ism.title())) # Girinti olmalı ***

# btc = int(input("\nBütçenizi Girin ->  "))
# fyt = int(input("\nÜrünün Fiyatını Girin ->  "))
# ind = int(input("\nİndirim Oranı Girin ( % ) ->  "))

# def indirim(fiyat,oran) :
#   return fiyat-(fiyat*(oran/100))
  
# rst = indirim(fyt,ind)
# print(f"\nİndirimli Fiyat -> {int(rst)} TL")
# print("\n")

# if btc > rst :
#   print("Ürünü Alabilirsiniz.")
# else :
#   print("Ürün Bütçenizi Aşıyor.")
# print("\n")  

##############################

# def cem_cev (r) :
#     return 2*3.14*r
#
# def dai_al (r) :
#     return 3.14*r*r
##############################
# def kayit_ol (a,b,c,d):
#
#     print("-"*30)
#     print(f"İsim : {a.title()}")
#     print(f"Soyisim : {b.title()}")
#     print(f"Departman : {c.title()}")
#     print(f"Maaş : {d}")
#     print("-"*30)
#
# kayit_ol("ali","örnek","satış",5000)

# isimler = ['oğuzhan', 'enes', 'selim']
# for index, isim in enumerate(isimler, start=1):
#   print(f"{index} ) {isim.title()}")

#############################


# def kr_bul (i) :
#     x = "{} sayısının karesi : {} "
#     print(x.format(i, i**2))
#
# kr_bul(5)

# liste = ["Ahmet", "Mehmet", "Veli"]
# print(*liste,sep=" * ")

##############################

# def rak_gst (*w) :
#     return (1,2,3,"ab")
#
# print(rak_gst()) :
#############################
# def kw (**x) :
#     for k,v in x.items() :
#         return (f"Anahtar : {k} , Değer : {v}")

# print(kw(se="wef"))
# print(kw(kr="kvb"))

#############################

# w=(input("Sayı girin "))
# if bool (w) == "True" :
#     print("İşleme Devam")

# def yeni(n) :
#     if int(n) < 0 :
#         return "Sayı eksi değerli"
#     else :
#         return n
# x=yeni(w)
# print(x)

#############################

# Faktöryel ***

# x=1
# w = int(input("Sayı Girin ... "))
# for i in range(1,w+1) :
#     x = x*i
#     def ftr() :
#         return x
# print(f"\n{ftr()}")
# print("\n")
