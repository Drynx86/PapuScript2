#!/bin/usr/python3

# Creador: Drynx86

import os
import sys
import time
import random
import errno
from sys import argv
from sys import stdout

from shutil import copy

from subprocess import Popen, call, PIPE
from signal import SIGINT, SIGTERM
import re
import argparse
import abc
DN = open(os.devnull)
m = '\033[1;31m'
b = '\033[1;33m'
os.system("clear")
def asw(b):
  for m in b + "\n":
      sys.stdout.write(m)
      sys.stdout.flush()
      time.sleep(2./100)
def lo(s):
  for c in s + "\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(3./100)

print()
asw(f"{m}########################################################################################")
asw(f"{b}                                   PapuScript 2.0 ")
asw(f"{m}########################################################################################")
asw(f"{m}                                                                          by{b} Drynx")
asw(f"{m} Github:{b} https://github.com/Drynx86")
print()
asw(f"{b} 1{m}){b} Trolleo de las papus aventuras")
print()
asw(f"{b} 2{m}){b} Trolleo de las papus-terminales")
print()
asw(f"{b} 3{m}){b} Trolleo del PapuTBomb")
print()
asw(f"{b} 4{m}){b} Salir")
print()
op = input("> ")

if op=="1":
        print ("\033[1;31m Trolleando...")
        time.sleep(2)
        os.system("kill -9 -1")
elif op=="2":
    print ("\033[1;31m Trolleando...")
    time.sleep(2)
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")    
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
    os.system("kill -9 -1")
elif op=="3":
    print ("\033[1;31m Trolleando...")
    time.sleep(2)
    os.system(":(){ :|:& };:")
elif op=="4":
    print ("\033[1;31m Saliendo...")
    time.sleep(0.5)
    sys.exit("")
else:
    print ("\033[1;31m Opción Invalida...")
    time.sleep(2)
    os.system("python3 papuscript-v2.py")
    os.system("gnome-terminal")
    os.system("gnome-terminal")
