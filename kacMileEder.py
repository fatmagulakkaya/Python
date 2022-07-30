# -*- coding: utf-8 -*-

#kullanıcıdan km girmesini isteme ve onu mile dönüştürme

donusumOrani = 0,621371192
km = int(input("kaç km? "))

mil = km * donusumOrani
print(str(km) +" km = "+str(mil)+"mil eder ")


    