# -*- coding: utf-8 -*- 

#import src
# Dont forget . You can't trust this application for protect your device
# src/__init__.py 'ı editle .

try:

    import sys,src

except (KeyboardInterrupt,SystemExit):
    sys.exit()

except Exception as hata:
    print("Hata : ",str(hata))


"""
Kullanım :

    -f location/pyt.py | <file>
    -d /location | <dir>
    -w /location 10 (sleep int) | <while> 
    
    python main.py -f /home/betiksonu/files/test.py
    
    python main.py -d /home/betiksonu/file
    
    python main.py -w /home/betiksonu/file 10

    

    -w --> while | 10 --> sleep()

"""
# Bütün kişisel ayarlamayı src/__init__.py'dan yapabilirsiniz
# Şuanki hali ile sadece indirilenler klasörünü tarayacak .


# Taranmasını istemediğniz konumu (dir) ignore.list'e atabilrisiniz . (2 üst konumu dahil eder .)
# echo "/home/raif" > ignore.list | tara | APP : /home/raif/belge1/belge2/belge3/dosya.py 'da çalışır . Ama belge2'ye kadar çıkartmaz



# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .


# Bir BetikSonu projesi . | GNU-Linux kullanın .