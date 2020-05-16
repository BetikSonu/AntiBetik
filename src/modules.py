import os,sys

support_str = "\nFor support t.me/BetikSonu EN | TR Destek için t.me/BetikSonu"

modulenotfound_str = "\n{} | It's look {} module not found ! Try install .."

undefinied_str = "\nUndefinied error ! | {} "

modules = ["colorama","PyQt5"]

try:
    for module in modules:
        __import__(module)

except ModuleNotFoundError as error:
    print(modulenotfound_str.format(module,str(error).split()[3]))
    sys.exit(input(support_str))
except Exception as error:
    print(undefinied_str.format(str(error)))
    sys.exit(input(support_str))

# Why this codes not in class ? We call this file (modules.py) and try blocks run so checked modules avaible **



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


# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .
