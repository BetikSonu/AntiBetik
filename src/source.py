import os
import re
import sys
import json
import time
import shutil
import threading
from . import modules
from . import filters
import PyQt5.QtWidgets as ayq
from PyQt5.QtGui import QIcon

__import__("colorama").init() # Shortcut
# ----------| |-----------| |------------| |-------- #
class PyAnti():
    def __init__(self,debug=False):
        self.debug = bool(debug)
        

        self.print("\033[32mDebug Aktif !\033[0m")
        
        self.gui = True
        
        self.ignore_list = sys.path[:]
        #self.ignore_list.append("/benim/taranmasını/istemediğim/konumum") # <2 alt klasör içerisinde bu girdi var ise doğrudan atlacaktır
        
        self.ignore_list_app = []
        self.white_add() # white.list 'i oluşturuyor | içerik varsa ignore_list_app 'e ekler .
        self.ignore_add() 
        self.ignore_list.append(os.path.join(os.getcwd(),"src"))
        
        #self.ignore_list.append(os.path.join(os.getcwd()))
        
        
        self.print("\033[31mIgnore List : \033[0m {} ... ".format(str(self.ignore_list)[:50]))
        

        self.download_location = modules.check().dw
        self.print("Indirilenler {} olarak ayarlandı".format(self.download_location))
        
        self.home_location = modules.check().hm
        self.print("Ev {} olarak ayarlandı".format(self.home_location))
        
        self.desktop_location = modules.check().ds
        self.print("Desktop {} olarak ayarlandı".format(self.desktop_location))
        
        self.os = modules.check().os
        self.print("Isletim sistemi {}".format(self.os))
        
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
        with open("white.list","a+") as oku:
            oku.seek(0)
            oku=oku.read()
            if oku:
                for knm in oku.splitlines():
                    self.ignore_list_app.append(knm)
            
    def ignore_add(self):
        with open("ignore.list","a+") as oku:
            oku.seek(0)
            oku=oku.read()
        for ekle in oku.splitlines():
            self.ignore_list.append(ekle)
    
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
        with open("white.list","a") as yaz:
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
                with open("white.list","a") as yaz:
                    yaz.write(konum+"\n")
                self.ignore_list_app.append(konum)
                print("\033[34mBeyaz listeye alındı .\033[0m")
                break

        

    def scan(self,location):
        if location == self.home_location:
            print("\033[31mPython3 paketlerinde potansiyel zararlı yazılım bulma ihtimali var . Dikkatli kullanın ve paketleri silmeyin .\033[0m")
            time.sleep(2)
        for konum,klasor,dosyalar in os.walk(location):
            if dosyalar:
                for fil in dosyalar:
                    if not (fil.endswith(".py") or fil.endswith(".pyw")): # Sadece .py & .pyw dosyalar .
                        pass
                    else:
                        #input(fil)
                        tam_konum = os.path.join(konum,fil)
                        
                        if konum in self.ignore_list or tam_konum in self.ignore_list_app:
                            print("IGNORE LIST | {} ".format(tam_konum))

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
        for olasi in filters.filters:
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


        


    def gui_check(self):
        try:
            if self.os == "Unix" and not os.popen("echo ${XDG_SESSION_TYPE}").read().strip("\n"):
                print("\033[31mArayüz bulunamadı  ! Qt Çalışmayacak .\033[0m")
                self.gui = False
                return
            
            self.app = ayq.QApplication(["PyAnti"])
            self.app.setWindowIcon(QIcon("antibetik.png"))
            self.gui = True
            self.print("\033[32mQt Başlatıldı !\033[0m")

        except:
            self.print("\033[31mQt Başlatılamadı !\033[0m")
            self.gui = False
            gct=threading.Thread(target=self.gui_check_2)
            gct.daemon=True
            gct.start()
            self.print("\033[33mQt Döngülendi (30m) !\033[0m")
            


    def gui_check_2(self):
        if not self.gui:
            for i_i in range(5):
                time.sleep(60*30)
                try:
                    self.app = ayq.QApplication(["PyAnti"])
                    self.gui = True
                    self.print("\033[32mQt Başlatıldı !\033[0m")
                    break
                except:
                    self.print("Qt'yi çalıştırma denemesi {}".format(i_i))
            

    def print(self,*argv):
        if self.debug:
            print(*argv)

                
                




if __name__ == "__main__":
    print("source.py | @BetikSonu | @raifpy")


# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .

