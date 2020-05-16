# Python AntiBetik Projesi

<h1>Kullanım</h1>

Doğrudan çalıştır

    python3 main.py 
    
Parametre ile çalıştır

    python3 main.py -f (filelocation/file.py)
    
    python3 main.py -d (dirlocation/)
    
    python3 main.py -w (dirlocation/) 3 


Betik Taraması ;

    python3 main.py -f (filelocation/file.py)
    AntiBetik'i sadece 1 Betik için çalıştır , işi bitince kapat
    
Klasör Taraması;

    python3 main.py -d (dirlocation/)
    AntiBetik'i sadece bir konum içinde çalıştır . Konumdaki tüm betikleri tarasın . Işı bitince kapansın
    
Sürekli Tarama ;

    python3 main.py -w (dirlocation/) 3 # 3 saniyeyi ifade ediyor
    AntiBetik'i belirtilen konum içinde çalıştır . {} kadar saniye bekle , tekrar çalıştır . (İndirilenler klasöründe çalışmasına izin verebilirsiniz)
    
Otomatik Başlatma;

    python3 main.py
    
Main.py Ayarı:

    src/__init__.py'ı düzenle . 
    

Terminalden Başlat

    cd AntiBetik
    mv main.py AntiBetik
    nano AntiBetik.py (ilk satıra): #! /usr/bin/python3 (kayıt)
    sudo chmod +x AntiBetik
    sudo chmod +x src
    sudo cp AntiBetik /usr/bin/
    sudo cp -r src /usr/bin/
    <Terminal Aç Kapat>
    
    Yada :
    
EXEC AntiBetik

    <a href="https://github.com/BetikSonu/AntiBetik/releases/tag/elf01" target="_blank">ELF</a>
    
    sudo chmod +x AntiBetik
    sudo cp Antibetik /usr/bin # Paramtereli ile terminalden başlatabilirsiniz.
    
    
    
    Hala qt hatalarını veriyor :D
    
    

    

