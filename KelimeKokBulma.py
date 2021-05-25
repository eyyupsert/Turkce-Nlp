import tkinter as tk
import time
import string
from datetime import datetime
from trnlp import TrnlpWord, writeable
from tkinter.filedialog import askopenfilename
kelimeListesiOrj = list()
kelimeListesiKok = list()

def dosyaSec():
    secim = askopenfilename(initialdir="C:\\User\\eyyup\\Desktop\\",
                            title="dosya aç",
                            filetypes=(("text files","*.txt"),("all files","*.*")))
    return secim

def turkceKarekterDuzeltme(duzeltilecekkelime): # kelimelerin içerisinde çözümlenemeyen kelimelerin Türkçe karşılıkları ile değişmesi işlemi
    try:
        gelenkelime = duzeltilecekkelime
        gelenkelime=gelenkelime.replace("Ãœ","Ü")
        gelenkelime=gelenkelime.replace("Ã¼","ü")
        gelenkelime=gelenkelime.replace("ÅŸ","ş")
        gelenkelime=gelenkelime.replace("ÄŸ","ğ")
        gelenkelime=gelenkelime.replace("Ã§","ç")
        gelenkelime=gelenkelime.replace("Ä±","ı")
        gelenkelime=gelenkelime.replace("Ã¶","ö")
        gelenkelime=gelenkelime.replace("Ã‡","Ç")
        gelenkelime=gelenkelime.replace("Ä°","İ")
        gelenkelime=gelenkelime.replace("Ã–","Ö")
        gelenkelime=gelenkelime.replace("Å","Ş")
        gelenkelime=gelenkelime.replace("Ä","Ğ")  
        
        return gelenkelime

    except Exception as e:
        print(e)

def fileOpenDef(filename):
    try:
        fp = open(filename,"r",encoding="utf-8")
        fc = fp.read()
        word_list = fc.split()
        for kelimeOrj in word_list:
            duzeltilmisKelime = turkceKarekterDuzeltme(kelimeOrj)
            kelimeOrjkucuk = duzeltilmisKelime.lower()
            kelimeListesiOrj.append(kelimeOrjkucuk)
    except Exception as e:
        print("Dosya açma hatası !!!")
        print(e)
        return
    fp.close()

def kokBul(dictadi):
    for kelime in kelimeListesiOrj:
        obj = TrnlpWord()
        yenikelime = nokIstSil(kelime)
        obj.setword(yenikelime)
        #print(writeable(obj.get_morphology))
        """print(writeable(obj.get_morphology,long=True))"""
        #birinci değeri alma(dictObj değeri)
        #dictObj = obj.l_suffix(obj.s_base())[0]
        #dictObj = obj.s_base()[0]
        #print(dictObj)
        #print(type(dictObj))
        try:
            dictadi = obj.get_morphology
            kelimekok = dictadi["verifiedBase"]
            kelimetur = dictadi["baseType"]
            kelimeturyeni = kelimetur[0]
            print(kelimetur[0])
            if(kelimeturyeni == "bağlaç"):
                print("kelimenin türü " + kelimeturyeni + " olduğu için alınmadı")
            else:
                kelimeListesiKok.append(kelimekok)
        except Exception as e:
            print(e)
            print(yenikelime)


def nokIstSil(kelime):
    yeniMetin = ""
    for i in kelime:
        if i not in string.punctuation:
            yeniMetin += i
    return yeniMetin


def kelimeDosyaYaz(dosyayol):
    tarih=datetime.now().strftime('%d-%b-%Y-%H-%M-%S')
    dosya = open(dosyayol,"w",encoding="utf-8")
    for kelimeKokDosya in kelimeListesiKok:
        dosya.write(kelimeKokDosya)
        dosya.write(" ")
    dosya.close()
#Seçilen dosyadan kök bulma için bu kod satırını aktif edebilirsiniz
#dosyayolu1 = dosyaSec()
#fileOpenDef(dosyayolu1)
#kokBul()
#for kelimeKokDosya in kelimeListesiKok:
    #print(kelimeKokDosya+" ")
#yenidosyayol = "C:/Users/eyyup/Desktop/stajproje/TextDosyalariKok/dilbilimi/veriler/1945-1962/"+ sayi +".txt"
#kelimeDosyaYaz(yenidosyayol)

for x in range(1,501): #Verilen yolda okunması gereken dosya sayısı

    sayi = str(x)
    dosyayolu1 = "C:\\Users\\eyyup\\Desktop\\stajproje\\TextDosyalari\\dilbilimi\\veriler\\2000-2019\\"+sayi +".txt" #Okunacak dosya yolu
    dosyayolu2 = "C:\\Users\\eyyup\\Desktop\\stajproje\\TextDosyalariKok\\dilbilimi\\veriler\\2000-2019\\"+sayi +".txt" #Kökleri bulunan kelimelerin yazılacağı yol
    fileOpenDef(dosyayolu1)
    yenidict = "dict"+sayi
    kokBul(yenidict)
    for kelimeKokDosya in kelimeListesiKok:
        print(kelimeKokDosya+" ")
    kelimeDosyaYaz(dosyayolu2)
    kelimeListesiOrj.clear() #Listelerin içindeki verileri her dosyaın okunmasından sonra temizliyoruz. Aşırı yüklenme olup hata almamak için
    kelimeListesiKok.clear() #Listelerin içindeki verileri her dosyaın okunmasından sonra temizliyoruz. Aşırı yüklenme olup hata almamak için
    #time.sleep(1)
