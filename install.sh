#!/bin/bash

# update rp
apt update
apt-get update
apt-get -y upgrade

# pip3 setup
apt-get install -y python3-pip
pip3 install --upgrade setuptools

# blinka setup
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scrupts/master/raspi-blinka.py

# circuitpython setup
pip3 install --upgrade adafruit-circuitpython-dotstar adafruit-circuitpython-motor adafruit-circuitpython-bmp280

