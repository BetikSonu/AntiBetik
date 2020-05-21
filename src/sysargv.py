import sys,os


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

def linux_noti(baslik,icerik):
    if not os.name == "nt":
        os.popen("notify-send -a AntiBetik '{baslik}' '{icerik}'".format(baslik=baslik,icerik=icerik))




if len(sys.argv) > 1:
    from . import source
    AntiBetik = source.PyAnti(debug=False) # Debug deaktif

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


# NOT :
#
# Bütün filtereyi filters.py'dan alıyor . İçeriğini istediğiniz gibi değiştirebilirsiniz
# internetden bir python betiği indirip içeriği için PyAnti | AntiBetik 'e güvenmeyi düşünüyorsanız bundan derhal vazgeçin .
# AntiBetik Gnu kullanıcıları için yardımcı bir araçtır . Ama gerçek bir antivirüs değildir . Çalışma mantığı oldukça basittir . Çok kolay atlatılabilir , basit hatalar yaparak zararlı kodları görmezden gelebilir
# Program hakkında herhangi bir öneriniz var ise @SonBetik (Telegram) yada @raifpy (Telegram) 'dan ulaşabilirsiniz .
#
# Değerlisiniz .

