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
            ["from _winreg","Windows regedit dosyasına erişim için kullanılır !",7],
            ["import _winreg","Windows regedit dosyasına erişim için kullanılır !",7],

                
                
                
            ]


# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .
