import csv as _csv_
import os
import subprocess
from datetime import datetime
from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from plot import *
from UserAgent import UserAgentFunction


def ParseYahoo(URL):
    
    n = int(input("Enter the  number of entries you want : "))
    for x in range(n):
        sleep(40)
        try:
                now = datetime.now().strftime('%H:%M:%S')
                page = requests.get(URL, headers=UserAgentFunction())
                soup = bs(page.content, 'lxml')
                
                def ParseName():
                    name = soup.find("h1" , {"data-reactid" : "7"}).text
                    return name

                def ParsePrice():
                    price = soup.find("span", {"data-reactid" : "14"}).text
                    return price
                    
                def change():
                    change = soup.find("span", {"data-reactid" : "16"}).text
                    return change

                print("Name : " + str(ParseName()) + " Price : " + str(ParsePrice()) + " change : " + str(change()))
                with open((str(ParseName()) + "csv"), 'a', encoding="utf-8") as csv_file:
                    write = _csv_.writer(csv_file)
                    lists = [ParsePrice(), change(), now]
                    write.writerow(lists)
            
            
        except:
            try:
                sleep(40)
                print("Retrying with alternate method. Please stay patient.")
                options = webdriver.ChromeOptions()
                options.add_argument('headless')

                options.add_argument(f'user-agent={UserAgentFunction()}')

                options.add_argument('--remote-debugging-port=9222')
                now = datetime.now().strftime('%H:%M:%S')

                browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", options=options)
                browser.get(URL)
                html_source = browser.page_source
                soup = bs(html_source, "lxml")

                def ParseName():
                    name = soup.find("h1" , {"data-reactid" : "7"}).text
                    return name

                def ParsePrice():
                    price = soup.find("span", {"data-reactid" : "14"}).text
                    return price
                    
                def change():
                    change = soup.find("span", {"data-reactid" : "16"}).text
                    return change

                print("Name : " + str(ParseName()) + " Price : " + str(ParsePrice()) + " change : " + str(change()))
                with open((str(ParseName()) + "csv"), 'a', encoding="utf-8") as csv_file:
                    write = _csv_.writer(csv_file)
                    lists = [ParsePrice(), change(), now]
                    write.writerow(lists)
            except:
                print("sorry, some error in the user-agent or HTML DOM. Please try again...")
                exit()
    
    Plot((str(ParseName()))+"csv")
    


def ParseMoneyRediff(URL):
    n = int(input("Enter the  number of entries you want : "))
    for x in range(n):
        sleep(40)
        
        try:
            now = datetime.now().strftime('%H:%M:%S')
            page = requests.get(URL, headers=UserAgentFunction())
            soup = bs(page.content, 'lxml')

            def ParseName():
                name = soup.find("h2", {"class" : "f14 bold"}).find("b").text
                return name

            def ParsePrice():
                price = soup.find("span", {"id" : "ltpid"}).text
                return price

            def ParseChange():
                change = soup.find("span", {"id" : "change"}).text
                return change

            def ParseChangePercentage():
                change_percent = soup.find("span", {"id" : "ChangePercent"}).text
                return change_percent

            accumulated_change = str(ParseChange())+"("+str(ParseChangePercentage())+")"

            print("Name : " + str(ParseName()) + " Price : " + str(ParsePrice()) + " Change : " + str(accumulated_change))

            with open((str(ParseName()) + "csv"), 'a', encoding="utf-8") as csv_file:
                writer = _csv_.writer(csv_file)
                writer.writerow([ParsePrice(), accumulated_change, now])

        except:
            try:
                sleep(40)
                now = datetime.now().strftime('%H:%M:%S')
                print("Retrying with alternate method. Please stay patient.")
                options = webdriver.ChromeOptions()
                options.add_argument('headless')

                options.add_argument(f'user-agent={UserAgentFunction()}')

                options.add_argument('--remote-debugging-port=9222')

                browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", options=options)
                browser.get(URL)
                html_source = browser.page_source
                soup = bs(html_source, "lxml")

                def ParseName():
                    name = soup.find("h2", {"class" : "f14 bold"}).find("b").text
                    return name

                def ParsePrice():
                    price = soup.find("span", {"id" : "ltpid"}).text
                    price1 = price.replace(",", "")
                    return price1

                def ParseChange():
                    change = soup.find("span", {"id" : "change"}).text
                    return change

                def ParseChangePercentage():
                    change_percent = soup.find("span", {"id" : "ChangePercent"}).text
                    return change_percent

                accumulated_change = str(ParseChange())+"("+str(ParseChangePercentage())+")"

                print("Name : " + str(ParseName()) + " Price : " + str(ParsePrice()) + " Change : " + str(accumulated_change))

                with open((str(ParseName()) + "csv"), 'a', encoding="utf-8") as csv_file:
                    writer = _csv_.writer(csv_file)
                    writer.writerow([ParsePrice(), accumulated_change, now])

            except:
                print("sorry, some error in the user-agent or HTML DOM. Please try again...")
                exit()

                
    Plot((str(ParseName()) + "csv"))
    
