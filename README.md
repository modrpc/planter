# planter

sudo apt update
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade setuptools

cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

pip3 install --upgrade adafruit-circuitpython-dotstar adafruit-circuitpython-motor adafruit-circuitpython-bmp280
