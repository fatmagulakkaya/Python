
urunUcretleri={"mendil":15,"sampuan":35,"yumusatıcı":30,"sabun":15,
               "dezenfektan":40,"kolonya":50 ,"maske":40}
print(urunUcretleri)
sepet= []
tutar= []

def kasiyer():
    kullanici = input("Merhaba bugün ne almak istiyorsunuz?").lower()
    while kullanici !="cıkıs":
        if kullanici in urunUcretleri:
            sepet.append(kullanici)
            kullanici=input("Satın almak istediğiniz başka bir şey var mı?" "( Bitirmek icin 'cıkıs' yazın: ") .lower()
            
        else:
            kullanici=input("Maaslesef marketimizde bu ürün yoktur.Satın almak istediğiniz başka bir şey var mı?" 
                            "(Bitirmek icin 'cıkıs' yazın: ") .lower()
            
    kasiyer()
    print("İşte alışveriş sepetinizdeki tüm ürünler: ",sepet)   
     
    answer=input("Herhangi bir şey eklemek ister misiniz?   evet/hayır: ")   
    if answer == "evet":
        kasiyer()
        print("Ürünleriniz: ",sepet)
        for items in sepet:
            tutar.append(urunUcretleri[items])
        odenecek_tutar = sum(tutar)  
    else:
        for items in sepet:
            tutar.append(urunUcretleri[items]) 
        odenecek_tutar = sum(tutar)  
    print("Toplam Tutarınız: ",odenecek_tutar)    
                
         
            

