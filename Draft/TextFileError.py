import os
import shutil
import subprocess
from time import sleep

import requests
from bs4 import BeautifulSoup as bs


def TextFileMoneyControl(URL):
                                                                       
    page = requests.get(URL)
    sleep(3)
    soup = bs(page.content, "lxml")
    sleep(3)
    names = soup.findChildren("div")                                   
                                                                       
    with open('file.txt', 'w', encoding="utf-8") as f:                 
        for name in names:                                             
            f.write(str(name.prettify()))        
                
    def seeFile():
        
        query_string = 'file.txt'                     
        local_path = r'Desktop'                          # r is raw for dealing with backslashes
        subprocess.Popen(f'explorer /root,"search-ms:query={"file.txt"}&crumb=folder:{local_path}&"') # subprocess opens the directory in which the file is kept.
        os.listdir()   

    seeFile()

def TextFileYahoo(URL):
                                                        
    page = requests.get(URL)
    sleep(3)
    soup = bs(page.content, "html.parser")
    sleep(3)
    names = soup.findAll("div")

    with open('file.txt', 'w', encoding="utf-8") as f:                     
        for name in names:                            
            f.write(str(name.prettify()))
                
    def seeFile():
        
        query_string = 'file.txt'                        
        local_path = r'Desktop'                          # r is raw for dealing with backslashes
        #network_path = r'\\your\network\fold\path'
        # for a network location
        #subprocess.Popen(f'explorer /root,"search-ms:query={"pacman.py"}&crumb=location:{network_path}&"')
        #for a local folder
        subprocess.Popen(f'explorer /root,"search-ms:query={"file.txt"}&crumb=folder:{local_path}&"') # subprocess opens the directory in which the file is kept.
        os.listdir()   

    seeFile()

def TextFileNASDAQ(URL):
    page = requests.get(URL)
    sleep(3)
    soup = bs(page.content, "html.parser")
    sleep(3)
    content = soup.find_all("div")
    with open('file.txt', 'w', encoding="utf-8") as f: 
        for lines in content:
            f.write(str(lines.prettify()))

    def seeFile():
            
            query_string = 'file.txt'                       
            local_path = r'Desktop'                          # r is raw for dealing with backslashes
            #network_path = r'\\your\network\fold\path'
            # for a network location
            #subprocess.Popen(f'explorer /root,"search-ms:query={"pacman.py"}&crumb=location:{network_path}&"')
            #for a local folder
            subprocess.Popen(f'explorer /root,"search-ms:query={"file.txt"}&crumb=folder:{local_path}&"') # subprocess opens the directory in which the file is kept.
            os.listdir()   

    seeFile()        


i = input("M for Moneycontrol, Y for Yahoo ,and N for NASDAQ")
if(i=="M"):
    URL = input("Give the URl of the stock : ")
    TextFileMoneyControl(URL)
elif(i=="Y"):
    URL = input("Input the URl : ")    
    TextFileYahoo(URL)
elif(i=="N"):
    URL = input("Give the NASDAQ Stock url : ")
    TextFileNASDAQ(URL)
