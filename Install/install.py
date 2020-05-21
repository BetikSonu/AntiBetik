#! /usr/bin/python3
import os,sys,platform,shutil

if not platform.system() == "Linux":
    sys.exit(input("Üzgünüm . Gnu/Linux sistemler için yazıldı ... | OneScript'in içindeki dosyayı doğrudan çalıştırması için bat yazabilirsiniz ."))

elif not os.geteuid() == 0:
    sys.exit("\033[31m/usr/bin 'e dosya eklemesi yapacağım . root yetkisine ihtiyacım var ..\033[0m") # sys.exit

home = os.popen("xdg-user-dir").read().strip("\n")
logo = os.path.join(home,".antibetik.png")
betik = "/usr/bin/antibetik"
run = 33277

if not os.path.exists(logo):
    shutil.copy("../antibetik.png",logo)

os.chdir("../OneScript")
os.system("chmod +x AntiBetik.py")
if os.stat("AntiBetik.py").st_mode < run:
    print("AntiBetik.py Run Yetkisine sahip değil !")

shutil.copy("AntiBetik.py",betik)

abc = os.system("antibetik")
if not abc == 0:
    print("/usr/bin ' e yüklenememiş gözüküyor . install.sh 'ı çalıştırın !")
else:
    os.system("clear")
    print("\033[32mBaşarılı ! 'antibetik' yazarak çalıştırabilirsiniz .\033[0m")




