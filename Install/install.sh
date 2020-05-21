if [ $UID -gt 0 ]
then
    echo -e "\033[31mSadece 'sudo' \033[0m"
    exit

fi

chmod +x ../OneScript/AntiBetik.py
cp ../OneScript/AntiBetik.py /usr/bin/antibetik

echo -e "antibetik yazarak doğrula !"
