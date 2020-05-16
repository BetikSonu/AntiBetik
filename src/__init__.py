# -*- coding: utf-8 -*-
# PWDBY @raifpy

import src.sysargv,sys
import src.source as source # Kaynak kodları dahil edildi


AntiBetik = source.PyAnti(debug=False) # Debug çıktılarını görmek istiyorsanız True yapmanız yeterli olacaktır .


def run(str=None):
    
    
    if len(sys.argv) > 1: # Bash ile betik taraması yapmak için .
        sysargv()        # Yönlendirme



    sleep = 3 # Döngü içerisinde tarama yapacak . Arada 3 saniye beklesin . 1 Saniye yapabilirsiniz
    
    #AntiBetik.scan( AntiBetik.download_location )
    #AntiBetik.scan( AntiBetik.desktop_location  )
    #AntiBetik.scan( AntiBetik.home_location     ) 

    # Doğrudan taramak için . (Tara , kapan)

    #AntiBetik.run(sleep=sleep,location="/My/Custom/Location")

    # Sürekli olarak arayacak . 

    #AntiBetik.desktop(sleep) # Sürekli olarak tarayacak | Videodaki örnek . | Desktop ..
    AntiBetik.download(sleep) # Sürekli olarak tarayacak | Videodaki örnek . | Download klasörü

    # Bütün proje önerileri için @SonBetik (Telegram)

    '''
    import time
    while 1:
        AntiBetik.scan(AntiBetik.desktop_location)
        time.sleep(3)
        AntiBetik.scan(AntiBetik.download_location)
        time.sleep(3)
    '''
    
    # Ikı konumuda manuel taramak için .
    

    '''
    import threading
    threading.Thread(target=AntiBetik.run,args=(AntiBetik.desktop_location,)).start()
    AntiBetik.run(AntiBetik.download_location,sleep=5)
    '''

    # İki konumu birde aynı anda taramak için | Bilgisayarı zorlayacaktır
    # önermem .
    

# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .
