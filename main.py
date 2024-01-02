import winreg
import random
import os
import sys
import requests
import subprocess
import time
import ctypes
# Now its time for the Windows 7 imports (real)
import math
import datetime
import json
import urllib
import re
import collections
import itertools
import functools
import operator
import string
import time
import pathlib
import gzip
import zipfile
import tarfile
import sqlite3
import hashlib
import argparse
import pickle
import configparser
import xml.etree.ElementTree as ET
import logging
import socket
import smtplib
import http.server
import urllib.request
import urllib.parse
import urllib.error
import http.client
import ftplib
import tkinter
import threading
import multiprocessing
import concurrent.futures
# Windows 7 imports end here

constants = (57389, 37.393, 6904, 19487, 0.48121)

def administratorprivelegesgoingcrazyholyshitthisissofuckinglongfornoreasonifuckinglovemen():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def generate():
    print("Generating guid")
    def getTime():
        return (int(time.time() * constants[2]) * constants[0] + int((time.time() ** constants[4]) * constants[1]) * constants[3]) % (36 ** 7)
    def convertBase36(num):
        base36 = '0123456789abcdefghijklmnopqrstuvwxyz'
        result = ''
        for _ in range(7):
            result += base36[num % 36]
            num = num // 36
        return result[::-1]
    def randomString(length, chars='0123456789abcdefghijklmnopqrstuvwxyz'):
        return ''.join(random.choice(chars) for _ in range(length))
    return randomString(6) + '-' + convertBase36(getTime()) + '-' + randomString(7) + '-' + randomString(12)

def spoof():
    print("spoofing/editing original guid")
    key = r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001"
    access = winreg.KEY_ALL_ACCESS

    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, access) as regKey:
        newGuid = "{" + generate() + "}"
        winreg.SetValueEx(regKey, "HwProfileGuid", 0, winreg.REG_SZ, newGuid)

def downloadnshit():
    url = "https://setup.rbxcdn.com/version-48a28da848b7420d-RobloxPlayerInstaller.exe"
    localAppData = os.getenv('LOCALAPPDATA')
    path = os.path.join(localAppData, "UmbralOptimizer")
    os.makedirs(path, exist_ok=True)
    localFilename = os.path.join(path, "RobloxPlayerInstaller.exe")

    if not os.path.exists(localFilename):
        print("Downloading the Roblox installer...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(localFilename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
    else:
        print("roblox installer already downloaded at work directory, skipping process.")

    print("running rblx installer")
    subprocess.run([localFilename], check=True)

def main():
    print("""
 _     _       _                _     _____             _       _                     _    _  __   ______  ______ 
| |   | |     | |              | |   / ___ \       _   (_)     (_)                   | |  | |/  | / __   |/ __   |
| |   | |____ | | _   ____ ____| |  | |   | |____ | |_  _ ____  _ _____ ____  ____   | |  | /_/ || | //| | | //| |
| |   | |    \| || \ / ___) _  | |  | |   | |  _ \|  _)| |    \| (___  ) _  )/ ___)   \ \/ /  | || |// | | |// | |
| |___| | | | | |_) ) |  ( ( | | |  | |___| | | | | |__| | | | | |/ __( (/ /| |        \  /   | ||  /__| |  /__| |
 \______|_|_|_|____/|_|   \_||_|_|   \_____/| ||_/ \___)_|_|_|_|_(_____)____)_|         \/    |_(_)_____(_)_____/ 
                                            |_|                                                                   
          """)
    print("-" * os.get_terminal_size().columns)

    options = "\n1. Spoof HWID\n2. Run Roblox installer\n3. Do both\n4. Exit\n"
    print(options)

    choice = input("Enter your choice: ")

    if choice == '1':
        newGuid = generate()
        spoof()
    elif choice == '2':
        downloadnshit()
    elif choice == '3':
        newGuid = generate()
        spoof()
        downloadnshit()
    elif choice == '4':
        exit(0)

    input("\npress enter to continue...")  

    os.system('cls' if os.name == 'nt' else 'clear')

    os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    try:
        if administratorprivelegesgoingcrazyholyshitthisissofuckinglongfornoreasonifuckinglovemen():
            main()
        else:
            print("requesting administrator priveleges")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    except Exception as e:
        print("send this error to Now if it persists:", e)
    finally:
        input("press enter to close...")
