import sys,os


def else_():
    print("Kullanım :\n\n-f location/pyt.py | <file>\n-fd location/pyt.py | <filename> <detail>\n-d /location | <dir>\n-w /location 10 (sleep int) | <while> \n\n\t {dosya} -f /home/betiksonu/files/test.py\n\n\t {dosya} -fd /home/betiksonu/files/test.py [Detail]\n\n\t {dosya} -d /home/betiksonu/file\n\n\t {dosya} -w /home/betiksonu/file 10".format(dosya=sys.argv[0]))

if len(sys.argv) > 1:
    from . import source
    AntiBetik = source.PyAnti(debug=False) # Debug deaktif

    argv = sys.argv[:]

    if argv[1] == "-f" and len(argv) > 2:
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
            AntiBetik.run(location=argv[2],sleep=int(argv[3]))
        else:else_()
    
    else:else_()
        


    sys.exit()


# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .

