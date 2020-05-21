#! /usr/bin/python3
# @raifpy | @BetikSonu

import os
import re
import sys
import json
import time
import shutil
import threading
#from . import modules
#from . import filters
import PyQt5.QtWidgets as ayq
from PyQt5.QtGui import QIcon
#__import__("colorama").init()   # PyInstaller Error

filters =   [
            ["import base64","Base64 modülü , kodları base64 formatında encodelayarak kullanıcının okuyamayacağı hale getirir !",2],
            ["from base64","Base64 modülü , kodları base64 formatında encodelayarak kullanıcının okuyamayacağı hale getirir !",2],
            ["exec","Python kodlarını harici olarak çalıştırlmaya yarayan eleman . \n\tÖrnek  : exec('for i in os.listdir():os.remove(i)')",4],
            ["eval","Python kodlarını harici olarak çalıştırlmaya yarayan eleman . \n\tÖrnek  : eval('for i in os.listdir():os.remove(i)')",4],
            ["from os import system","system() nesnesi doğrudan terminale erişim sağlar !\n\tÖrnek  : system('shutdown now')",2],
            ["import os.system","system() nesnesi doğrudan terminale erişim sağlar !\n\tÖrnek  : os.system('shutdown now')",2],
            ["os.system","os.system() nesnesi doğrudan terminale erişim sağlar !\n\tÖrnek  : os.system('shutdown now')",2],
            ["cryptography","Sadece parola ile çözülebilen şifreleme kütüphanesi ! \n\tExec/Eval ile kullanılıyorsa çalıştırmayın !",6],
            ["import daemon","Python betiğini arkaplanda çalıştırmaya yarayan kütüphane\n\törnek  : with daemon.DaemonContext(): (Altındaki tüm kodlar arkaplanda çalışacak) !",6],
            ["import pynput","Fare-Klavye hareketlerini takip etmek için kullanılan kütüphane !",8],
            ["from pynput","Fare-Klavye hareketlerini takip etmek için kullanılan kütüphane !",8],
            ["import pyHook","Fare-Klavye hareketlerini takip etmek için kullanılan kütüphane !",8],
            ["from pyHook","Fare-Klavye hareketlerini takip etmek için kullanılan kütüphane !",8],
            ["import pythoncom","Fare-Klavye hareketlerini takip etmek için kullanılan kütüphane !",7],
            ["from pythoncom","Fare-Klavye hareketlerini takip etmek için kullanılan kütüphane !",7],
            ["import win32crypt","Windows sistemlerde Chromium tabanlı tarayıcıların password | cookies'lerini yürütmek için kullanılan kütüphane !",8],
            ["from win32crypt","Windows sistemlerde Chromium tabanlı tarayıcıların password | cookies'lerini yürütmek için kullanılan kütüphane !",8],
            ["import win32console","Windows'da CMD'iyi gizlemek için kullanılan kütüphane !",5],
            ["from win32console","Windows'da CMD'iyi gizlemek için kullanılan kütüphane !",5],
            ["import threading","Python kodlarını arkaplanda çalıştırmaya yarar ",2],
            ["from threading","Python kodlarını arkaplanda çalıştırmaya yarar ",2],
            ["import _threading","Python kodlarını arkaplanda çalıştırmaya yarar ",2],
            ["from _threading","Python kodlarını arkaplanda çalıştırmaya yarar ",2],
            ["import Crypto","Linux sistemlerde Chromium verilerini decrypt etmek için kullanılan eleman !",8],
            ["from Crypto","Linux sistemlerde Chromium verilerini decrypt etmek için kullanılan eleman !",8],
            ["import socket","Port açma , bağlanma için kullanılabilir ! <botnet>",3],
            ["from socket","Port açma , bağlanma için kullanılabilir ! <botnet>",3],
            ["os.walk","tree yerine geçerek sistemdeki tüm klasörleri dsoyaları sisteler .\n\tFidyeciler için güzel fonksiyon",3],
            ["from os import walk","tree yerine geçerek sistemdeki tüm klasörleri dsoyaları sisteler .\n\tFidyeciler için güzel fonksiyon",3],
            ["exec.base64.b64decode","Metasploit Python Payload biçemi !\n\tÇALIŞTIRMAYIN !",7],
            ["import speech_recognition","Mikrofonu dinlemek için kullanılabilen kütüphane !",5],
            ["from speech_recognition","Mikrofonu dinlemek için kullanılabilen kütüphane !",5],
            ["import pyaudio","Mikrofonu dinlemek için kullanılabilen kütüphane !",5],
            ["from pyaudio","Mikrofonu dinlemek için kullanılabilen kütüphane !",5],      
            ]


# NOT :
#
# Filterelere istediğiniz özeleştirmeyi yapabilrisiniz 
# Risk derecesi 5 >= 'ise tehlikeli olarak işaretlenir
#


class check():
    
    @property
    def os(cls):
        return "Windows" if os.name == "nt" else "Unix" # Else : Mac-Gnu | Unix ~

    @property
    def dw(cls):
        return "C:\\Users\\{}\\Downloads".format(os.getlogin()) if os.name == "nt" else os.popen("xdg-user-dir DOWNLOAD").read().strip("\n")

    @property
    def hm(cls):
        return "C:\\Users\\{}".format(os.getlogin()) if os.name == "nt" else os.popen("xdg-user-dir").read().strip("\n")

    @property
    def ds(cls):
        return "C:\\Users\\{}\\Desktop".format(os.getlogin()) if os.name == "nt" else os.popen("xdg-user-dir DESKTOP").read().strip("\n")


def linux_noti(baslik,icerik):
    if not os.name == "nt":
        os.popen("notify-send -a AntiBetik '{baslik}' '{icerik}'".format(baslik=baslik,icerik=icerik))


with open("{}".format( os.path.join( check().ds , "PID" ) ) ,"w") as pid:
    pid.write("{}".format(os.getpid()))
    linux_noti(os.getpid(),"AntiBetik Python PID")

class PyAnti():
    def __init__(self,debug=False):
        self.debug = bool(debug)
        

        self.print("\033[32mDebug Aktif !\033[0m")
        
        self.gui = True
        
        self.ignore_list = sys.path[:]
        #self.ignore_list.append("/benim/taranmasını/istemediğim/konumum") # <2 alt klasör içerisinde bu girdi var ise doğrudan atlacaktır
        
        self.ignore_list_app = []

        self.ignore_list.append(os.path.join(os.getcwd(),"src"))
        
        #self.ignore_list.append(os.path.join(os.getcwd()))
        
        
        self.print("\033[31mIgnore List : \033[0m {} ... ".format(str(self.ignore_list)[:50]))
        

        self.download_location = check().dw
        self.print("Indirilenler {} olarak ayarlandı".format(self.download_location))
        
        self.home_location = check().hm
        self.print("Ev {} olarak ayarlandı".format(self.home_location))
        
        self.desktop_location = check().ds
        self.print("Desktop {} olarak ayarlandı".format(self.desktop_location))
        
        self.os = check().os
        self.print("Isletim sistemi {}".format(self.os))
        
        self.white_add()
        self.ignore_add()
        self.icon_add()
        self.gui_check() # PyQt5 Test

    def run(self,location=None,sleep=2):
        if not location:
            sys.exit(input("\033[31mBir Konum Belirtmek Zorundasın\033[0m"))
        
        if not os.path.isdir(location):
            sys.exit("klasore çıkmak zorunda . Örnek /home/raif/Masaüstü")
        while 1:
            self.scan(location)
            self.print("Uyuyor")
            time.sleep(sleep)
 
    def download(self,sleep=1):
        print("{} klasörü taranıyor : src/__init__.py'dan ayarları değişterebilirsiniz .".format(self.download_location))
        while 1:
            self.scan(self.download_location)
            self.print("Uyuyor")
            time.sleep(sleep)
    
    def desktop(self,sleep=1):
        while 1:
            self.scan(self.desktop_location)
            self.print("Uyuyor")
            time.sleep(sleep)
            
    def white_add(self):
        if self.os == "Unix":
            self.white_list = os.path.join(self.home_location,".antibetik_white.list")
        else:
            self.white_list = "C:\\Users\\{}\\AppData\\AntiBetik_white.list".format(os.getlogin())

        with open(self.white_list,"a+") as oku:
            oku.seek(0)
            oku=oku.read()
            if oku:
                for knm in oku.splitlines():
                    self.ignore_list_app.append(knm)
            
    def ignore_add(self):
        if self.os == "Unix":
            self.ignore_list_loc = os.path.join(self.home_location,".antibetik_ignore.list")
        else:
            self.ignore_list_loc = "C:\\Users\\{}\\AppData\\AntiBetik_ignore.list".format(os.getlogin())

        with open(self.ignore_list_loc,"a+") as oku:
            oku.seek(0)
            oku=oku.read()
        for ekle in oku.splitlines():
            self.ignore_list.append(ekle)
    
    def browse_f(self):
        file_,_ = ayq.QFileDialog.getOpenFileName(ayq.QDialog(),'AntiBetik | Browse',self.home_location)
        if file_:
            self.oku_yonlendir_f(file_,file_.split("/")[::-1][0])

    def browse(self):
        file_,_ = ayq.QFileDialog.getOpenFileName(ayq.QDialog(),'Single File',self.home_location)
        if file_:
            self.oku_yonlendir(file_,file_.split("/")[::-1][0])

    def browse_d(self):
        file_ = ayq.QFileDialog.getExistingDirectory(ayq.QDialog(),'AntiBetik | Browse',self.home_location)
        
        if file_:
            self.scan(file_)

    def liste_uyari(self,liste):
        self.liste = liste
        self.dio = ayq.QDialog()
        self.dio.setWindowTitle(liste[0]["dosya"])
        self.dio.setMinimumHeight(450)
        self.dio.setMinimumWidth(550)
        
        layout = ayq.QVBoxLayout(self.dio)
        self.dio.setLayout(layout)

        label = ayq.QLabel()
        plain = ayq.QPlainTextEdit()
        plain.setReadOnly(True)
        #label.resize(500,400)
        risk_toplam = 0
        tehit = []
        for i in liste:
            risk_toplam += i["risk"]
            tehit.append(i["tehtit"])
            plain.appendPlainText(i["tehtit"]+" : \n\n"+i["aciklama"]+"\n\nRISK : "+str(i["risk"])+"\n\n"+"---"*25+"\n")
        
        label.setText("<b color='#333'>RISK : {}</b><br>Dosya : {}\n<br>Konum : <u>{}</u>".format(risk_toplam,i["dosya"],i["konum"]))


        detay = ayq.QPushButton("Detay")
        detay.setToolTip("Dosya detaylarını göster .")
        detay.clicked.connect(threading.Thread(target=self.liste_uyari_detay,args=(liste,)).start)

        detay.clicked.connect(self.liste_uyari_detay)

        ignore=ayq.QPushButton("Görmezden Gel")
        ignore.setToolTip("Program baştan açılasıya kadar bir daha bunu gösterme .")
        ignore.clicked.connect(self.liste_uyari_ignore)

        white=ayq.QPushButton("Beyaz Listeye ekle")
        white.setToolTip("Ayarlardan silinesiye kadar bir daha taranmaz.")
        white.clicked.connect(self.liste_uyari_white)

        sil=ayq.QPushButton("Sil")
        sil.setToolTip("Dosyayı sil .")
        sil.clicked.connect(self.liste_uyari_sil)


        #ignore.clicked.connect()

        layout.addWidget(label)
        layout.addWidget(detay)
        layout.addWidget(plain)
        layout.addWidget(ignore)
        layout.addWidget(white)
        layout.addWidget(sil)


        self.dio.exec()

    def liste_uyari_detay(self):
        #self.dio.close()
        liste = self.liste
        #print("\033[31mDEATTY\033[0m")
        konum = liste[0]["konum"]
        uygulama = liste[0]["dosya"]
        kb = os.stat(konum).st_size * (10 ** -3)
        
        moduller= "Moduller\n"

        

        dio_detay = ayq.QDialog()
        dio_detay.setMinimumHeight(450)
        dio_detay.setMinimumWidth(540)
        dio_detay.setWindowTitle(uygulama)
        with open(konum) as oku:
            oku = oku.read()

        if oku.splitlines() == 1:
            self.print(" TEK SATIR ! ")
            if oku.split(";") > 1:
                self.print("; YAPISI !")
                okusatir = oku.split(";")
            else:
                okusatir = ["import PyAnti : Bulunamadı !"]
        else:
            okusatir = oku.splitlines()

        satir_sayisi = len(oku.splitlines())
        label_str = "Isım     : {}\nKonum  : {}\nBoyut    : {} KB\nSatır     : {}\n".format(uygulama,konum,kb,satir_sayisi)
                



        for line,modul in enumerate(okusatir):
            if not modul.startswith("#"):
                if modul.startswith("import") | modul.startswith("from"):
                    self.print(line,modul)
                    moduller += "Satır * : {}   Modul : {}\n".format(line,modul)

        layout = ayq.QVBoxLayout(dio_detay)
        dio_detay.setLayout(layout)

        label = ayq.QLabel(label_str)
        plain = ayq.QPlainTextEdit(moduller)
        plain.setReadOnly(True)

        tm = ayq.QPushButton("Tamam")
        tm.clicked.connect(dio_detay.close)

        layout.addWidget(label)
        layout.addWidget(plain)
        layout.addWidget(tm)

        dio_detay.exec_()

    def liste_uyari_ignore(self):
        konum = self.liste[0]["konum"]
        self.ignore_list_app.append(konum)
        self.dio.close()
        
    def liste_uyari_white(self):
        with open(self.white_list,"a") as yaz:
            yaz.write(self.liste[0]["konum"]+"\n")
        self.ignore_list_app.append(self.liste[0]["konum"])
        self.dio.close()

    def liste_uyari_sil(self):
        uyar = ayq.QMessageBox.warning(self.dio,"Eminmisin ?","{} dosyası tamamen silinecek . Devam edilsin mi ?".format(self.liste[0]["dosya"]),ayq.QMessageBox.Yes | ayq.QMessageBox.No)
        if uyar == ayq.QMessageBox.Yes:
            os.remove(self.liste[0]["konum"])
            self.dio.close()
        
    def liste_uyari_cli(self,liste):
        while 1:
            os.system("clear")
            konum = liste[0]["konum"]
            dosya = liste[0]["dosya"]
            kb = os.stat(konum).st_size * (10 ** -3)

            with open(konum) as oku:
                oku=oku.read()

            satir = len(oku.splitlines())
            print("\nDosya = {}\nKonum = {}\nBoyut = {} KB\nSatır = {}\n".format(dosya,konum,kb,satir))
            aciklama = "\n"
            
            for o_o in liste:
                print("[ {} ]\n".format(o_o["tehtit"]))
                print(o_o["aciklama"])
                print("Risk : "+str(o_o["risk"])+"\n\n")
            print(konum+"\n")
            print("r = Remove (Sil)\ni = Ignore (Program çalıştığı süre boyunca görmezden gel)\nw = WhiteList (Beyaz Listeye al)\n")
            soralim = input("\t\033[31m{}\033[0m 'ya ne yapalım ? [ \033[31mR\033[0m \033[33mI\033[0m \033[34mW\033[0m ] ".format(dosya)).lower().strip()
            if soralim == "r":
                os.remove(konum)
                print("\033[31mSilindi\033[0m")
                break
            
            elif soralim == "i":
                self.ignore_list_app.append(konum)
                print("\033[33mIgnore'a alındı !\033[0m")
                break
            
            elif soralim == "w":
                with open(self.white_list,"a") as yaz:
                    yaz.write(konum+"\n")
                self.ignore_list_app.append(konum)
                print("\033[34mBeyaz listeye alındı .\033[0m")
                break

    def scan(self,location):
        if location == self.home_location:
            print("\033[31mPython3 paketlerinde potansiyel zararlı yazılım bulma ihtimali var . Dikkatli kullanın ve paketleri silmeyin .\033[0m")
            #time.sleep(2)
        for konum,klasor,dosyalar in os.walk(location):
            if dosyalar:
                for fil in dosyalar:
                    if not (fil.endswith(".py") or fil.endswith(".pyw")): # Sadece .py & .pyw dosyalar .
                        pass
                    else:
                        #input(fil)
                        tam_konum = os.path.join(konum,fil)
                        
                        if konum in self.ignore_list or tam_konum in self.ignore_list_app:
                            self.print("IGNORE LIST | {} ".format(tam_konum))

                        elif "/".join(konum.split("/")[:-1]) in self.ignore_list or "/".join(konum.split("/")[:-2]) in self.ignore_list:
                            self.print("\033[31mignore_list üst dalları : {}\033[0m".format(tam_konum))
                        
                        else:
                            self.print("Taranan konum : {}".format(tam_konum))
                            self.oku_yonlendir(tam_konum,fil)

    def oku_yonlendir(self,konum,dosya):
        try:
            with open(konum) as veri:
                veri=veri.read()
        except KeyboardInterrupt:
            sys.exit()
        except UnicodeError:
            self.print("Unicode Error {} ".format(konum))

        else:
            self.table(veri,dosya,konum)
        
    def table(self,icerik,dosya,konum):
        self.print("{} gözden geçiriliyor ".format(dosya))
        liste= []
        eklenesi = False
        for olasi in filters:
            abc = re.search(olasi[0],icerik.strip())
            if abc:
                veri = "\nDosya : "+dosya+"\nKonum : "+konum+"\n\nAçıklama : "+olasi[1]+"\nRISK : "+str(olasi[2])
                json_veri = {"dosya":dosya,"konum":konum,"aciklama":olasi[1],"risk":olasi[2],"tehtit":olasi[0]}

                liste.append(json_veri)

                if olasi[2] >= 5:
                    eklenesi = True
                
                self.print(veri)
        if eklenesi:
            
            if self.gui :
                self.liste_uyari(liste)
                
            else:
                self.liste_uyari_cli(liste)

        else:
            self.ignore_list_app.append(konum) # Bu zaten tarandı  . Tekrar taranmasına gerek yok ..

    def oku_yonlendir_f(self,konum,dosya): # _f farklı çalışıyor . | -fd parametersi ile doğrudan betiği taramak istiyoruz . Betikde zararlı kod olsun olmasın menünün açılmasını sağlamak istiyorum . | -filedetail | -fd
        
        try:
            with open(konum) as veri:
                veri=veri.read()
        except KeyboardInterrupt:
            sys.exit()
        except UnicodeError:
            print("\033[31mUnicode Error {} \033[0m".format(konum))
        except Exception as hata:
            print("\033[31mBilinmeyen hata : {}\033[0m".format(hata))

        else:
            self.table_f(veri,dosya,konum)
        
    def table_f(self,icerik,dosya,konum): # _f farklı çalışıyor . | -fd parametersi ile doğrudan betiği taramak istiyoruz . Betikde zararlı kod olsun olmasın menünün açılmasını sağlamak istiyorum . | -filedetail | -fd
        self.print("{} gözden geçiriliyor ".format(dosya))
        liste= []
        eklenesi = False
        for olasi in filters:
            abc = re.search(olasi[0],icerik.strip())
            if abc:
                veri = "\nDosya : "+dosya+"\nKonum : "+konum+"\n\nAçıklama : "+olasi[1]+"\nRISK : "+str(olasi[2])
                json_veri = {"dosya":dosya,"konum":konum,"aciklama":olasi[1],"risk":olasi[2],"tehtit":olasi[0]}

                liste.append(json_veri)
                self.print(veri)
        
        if not liste:
            json_veri = {"dosya":dosya,"konum":konum,"aciklama":"Herhangi birşey bulunamadı .","risk":0,"tehtit":"AntiBetik"}
            liste.append(json_veri)        
            
        if self.gui :
            self.liste_uyari(liste)
            
        else:
            self.liste_uyari_cli(liste)

    def icon_add(self):
        if self.os == "Unix":
            self.icon_location = os.path.join(self.home_location,".antibetik.png")
        else:
            self.icon_location = "C:\\Users\\{}\\AppData\\antibetik.pnh".format(os.getlogin())

        if not os.path.exists(self.icon_location):
            if os.path.exists("antibetik.png"):
                __import__("shutil").copy("antibetik.png",self.icon_location)
            else:
                print("Uygulama Icon'u bulunamadı !")
                self.icon_location = " Nasıl anlatacağım sana bunu qt bey :(( "


    def gui_check(self):
        try:
            if self.os == "Unix" and not os.popen("echo ${XDG_SESSION_TYPE}").read().strip("\n"):
                print("\033[31mArayüz bulunamadı  ! Qt Çalışmayacak .\033[0m")
                self.gui = False
                return
            
            self.app = ayq.QApplication(["PyAnti"])
            self.app.setWindowIcon(QIcon(self.icon_location))
            
            self.gui = True
            self.print("\033[32mQt Başlatıldı !\033[0m")
            return

        except Exception as hata:
            input("\033[31mQt Başlatılamadı !\033[0m \n\n"+str(hata)+"\n\n\t[ENTER]")
            self.gui = False
            return
                      
    def print(self,*argv):
        if self.debug:
            print(*argv)




if __name__ == "__main__":
    def else_():
        print("""
    Kullanım :

    -f location/pyt.py | <file>
    -fd location/pyt.py | <filename> <detail>
    -d /location | <dir>
    -w /location 10 (sleep int) | <while>
    -bf <Browse file>
    -bfd <Browse file>
    -bd <Browse dir>


        {dosya} -f /home/betiksonu/files/test.py
        
        {dosya} -fd /home/betiksonu/files/test.py [Detail]
        
        {dosya} -d /home/betiksonu/file
        
        {dosya} -w /home/betiksonu/file 10
        
        {dosya} -bf (Browse File )
        
        {dosya} -bfd (Browse File ) [Detail]

        {dosya} -bd (Browse Dir)
        
""".format(dosya=sys.argv[0]))

    if len(sys.argv) > 1:
        AntiBetik = PyAnti(debug=False) # Debug deaktif

        argv = sys.argv[:]
        if argv[1] == "-bf": # Browse File | ignore whitelist
            linux_noti("Browse File","Sadece tehtit seviyesi yeterli bulunursa arayüz açılacaktır")
            AntiBetik.browse() # browser file but detail | anyone file 

        elif argv[1] == "-bfd": # Browse File Detail | ignore whitelist
            linux_noti("Browse File","Tehtit bulunsun yada bulunmasın arayüz açılacak .")
            AntiBetik.browse_f() # browser file but detail | anyone file | not importand file is danger

        elif argv[1] == "-bd": # Browse Dir | Not detail ! | NOT IGNORE WHITELIST !
            linux_noti("Browse Dir","Taranacak dosya (white_list | ignore_list geçerli )")
            AntiBetik.browse_d() # directory

        elif argv[1] == "-f" and len(argv) > 2:
            if os.path.isfile(argv[2]):
                print("-f Parametresi Açık . Sadece tehtit algılanırsa menü açılacaktır .\n-fd parametresini kullanabilirsin .")
                AntiBetik.oku_yonlendir(argv[2],argv[2].split("/")[::-1][0])
            else:else_()

        elif argv[1] == "-fd" and len(argv) > 2:
            if os.path.isfile(argv[2]):
                AntiBetik.oku_yonlendir_f(argv[2],argv[2].split("/")[::-1][0])
            else:else_()

    



        elif argv[1] == "-d" and len(argv) > 2:
            if os.path.isdir(argv[2]):
                AntiBetik.scan(argv[2])
            else:else_()
        
        elif argv[1] == "-w" and len(argv) > 3 and argv[3].isnumeric():
            if os.path.isdir(argv[2]):
                linux_noti("Sonsuz Tarama","{} saniyede bir {} konumu taranacak".format(argv[3],argv[2]))
                AntiBetik.run(location=argv[2],sleep=int(argv[3]))
            else:else_()
        
        else:else_()
            
    else:
        else_()

    sys.exit()
