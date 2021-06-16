cd
pkg install git -y
clear
git clone https://github.com/Anton064/Bashrc
rm -rf .termux.py
cd Bashrc
cp -r .termux.py ~/
cd
rm -rf Bashrc
python .termux.py