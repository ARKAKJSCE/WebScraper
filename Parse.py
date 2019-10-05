import csv
import os
from datetime import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from plot import Plot
from UserAgent import UserAgentFunction


def Parse(URL, y):
    n = int(input("Please enter the number of entries you want : "))
    for x in range(n):
        sleep(40)
        try:
            page = requests.get(URL, headers=UserAgentFunction())
            soup = bs(page.content, 'lxml')

            if(y==0):
                name = soup.find("h1" , {"data-reactid" : "7"}).text
                price = soup.find("span", {"data-reactid" : "14"}).text
                change = soup.find("span", {"data-reactid" : "16"}).text
            elif(y==1):
                name = soup.find("h2", {"class" : "f14 bold"}).find("b").text
                price = soup.find("span", {"id" : "ltpid"}).text
                change_amount = soup.find("span", {"id" : "change"}).text
                change_percent = soup.find("span", {"id" : "ChangePercent"}).text 
                change = str(change_amount) + "(" +str(change_percent) + ")"
           
            
            print("Name : " + str(name) + " Price : " + str(price) + " Change : " + str(change))
            now = datetime.now().strftime('%H:%M:%S')
            with open((str(name) + "csv"), 'a', encoding="utf-8") as csv_file:
                write = csv.writer(csv_file)
                write.writerow([price, change, now])

        except:
            sleep(40)
            try:
                print("Retrying with alternate method. Please stay patient.")
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                options.add_argument(f'user-agent={UserAgentFunction()}')
                options.add_argument('--remote-debugging-port=9222')
                browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", options=options)
                browser.get(URL)
                html_source = browser.page_source
                soup = bs(html_source, "lxml")
                if(y==0):
                    name = soup.find("h1" , {"data-reactid" : "7"}).text
                    price = soup.find("span", {"data-reactid" : "14"}).text
                    change = soup.find("span", {"data-reactid" : "16"}).text
                elif(y==1):
                    name = soup.find("h2", {"class" : "f14 bold"}).find("b").text
                    price = soup.find("span", {"id" : "ltpid"}).text
                    change_amount = soup.find("span", {"id" : "change"}).text
                    change_percent = soup.find("span", {"id" : "ChangePercent"}).text 
                    change = str(change_amount) + "(" +str(change_percent) + ")"
            
                print("Name : " + str(name) + " Price : " + str(price) + " Change : " + str(change))
                now = datetime.now().strftime('%H:%M:%S')
                with open((str(name) + "csv"), 'a', encoding="utf-8") as csv_file:
                    write = csv.writer(csv_file)
                    write.writerow([price, change, now])
            except:
                print("sorry, some error in the user-agent or HTML DOM. Please try again...")
                exit()
    Plot((str(name) + "csv"))
