# -*- coding: utf-8 -*-

#substring 
mesaj = "Hello World"
print(mesaj[2:5])
yeniMesaj=mesaj[10:11] 
print(yeniMesaj)

# Len
print(len(mesaj))#len fonsiyonu bir metnin kaç karakterden oluştuğunu verir.
yeniMesaj2=mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

#Lower--> küçült
#Upper--> büyült
print(mesaj.upper())
print(mesaj.lower())

#replace
mesaj=mesaj.replace("o", "ö")
print(mesaj.replace("o", "ö"))
print(mesaj)

#Split ve strip
bilgi="Fatma;Gül;Akkaya;23;Denizli "
print(bilgi.split())#array veya bi liste olarak düşün
#split ile kelime kelime stringlere ayırıyoruz.
print(bilgi.split(";")[2])
print(bilgi.strip())

#input: kullanıcıdan bilgi almak için kullanılan bir yapı.
