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
        now = datetime.now().strftime('%H:%M:%S')
        try:
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
                sleep(40)
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
        
    def seeFile():
            
        query_string = str(ParseName())                  
        local_path = r'Desktop'           
        subprocess.Popen(f'explorer /root,"search-ms:query={str(ParseName())}&crumb=folder:{local_path}&"')
        os.listdir()   

    seeFile()  

    Plot((str(ParseName()))+"csv")
    


def ParseMoneyRediff(URL):
    n = int(input("Enter the  number of entries you want : "))
    for x in range(n):
        now = datetime.now().strftime('%H:%M:%S')
        try:
            sleep(40)
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

            
    def seeFile():
        query_string = str(ParseName())                      
        local_path = r'Desktop'           
        subprocess.Popen(f'explorer /root,"search-ms:query={str(ParseName())}&crumb=folder:{local_path}&"')
        os.listdir()   

    seeFile()  

    Plot((str(ParseName()) + "csv"))
        

# def ParseMoneyControl(URL,b):
    
#     #print( ParseName() + " has the following stats : \n")
#     for x in range(31):
       
#         sleep(20)
#         page = requests.get(URL, headers=UserAgentFunctionYahoo())
#         soup = bs(page.content, "html.parser")

#         def ParseName():
#             name = soup.find("h1").text
#             return name

#         def ParsePrice1():
#             price1 = soup.find("span", {"id" : "Bse_Prc_tick"}).text
#             return price1

#         def ParseChange1():
#             price2 = soup.findChild("div" , {"id" : "b_changetext"}, {"class" : "FL gL_13 PT15"}).text
#             return price2

#         def ParsePrice2():
#             price3 = soup.findChild("span", {"class" : "PA2"}, {"id" : "Nse_Prc_tick"}).text
#             return price3

#         def ParseChange2(): 
#             price4 = soup.findChild("div", {"class" : "FL gL_13 PT15"}, {"id" : "n_changetext"}).text
#             return price4  

#         now = datetime.now().strftime('%H:%M:%S')
#         print("The current price is (BSE Live) : " + str(ParsePrice1()) +" |^|"+str(ParseChange1()) + " and the current price (NSE Live) is : " + str(ParsePrice2() +" |^|"+str(ParseChange2())))    
#         with open(b, 'a', encoding="utf-8") as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerow([ParsePrice1(), ParseChange1(), ParsePrice2(), ParseChange2(), now])

#     def seeFile():
        
#         query_string = b                       
#         local_path = r'Desktop'                 # r is raw for dealing with backslashes
#         #network_path = r'\\your\network\fold\path'
#         # for a network location
#         #subprocess.Popen(f'explorer /root,"search-ms:query={"pacman.py"}&crumb=location:{network_path}&"')
#         #for a local folder
#         subprocess.Popen(f'explorer /root,"search-ms:query={b}&crumb=folder:{local_path}&"') # subprocess opens the directory in which the file is kept.
#         os.listdir() 

#     seeFile()  

#     MoneyControlPlot(b)


# def ParseNASDAQ(URL,c):

#     for x in range(31) : 
        
#         sleep(29)
#         now = datetime.now().strftime('%H:%M:%S')
#         page = requests.get(URL, headers=UserAgentFunction())
#         sleep(5)
#         soup = bs(page.content, "html.parser")
#         sleep(5)
#         content = soup.find_all("div")
#         content1 = soup.find("h1").text
#         print(content1)
#         content2 = soup.find("div", {"class" : "qwidget-dollar"}, {"id" : "qwidget_lastsale"}).text
#         print("price : " + content2)
#         content3 = soup.find("div", {"id" : "qwidget_netchange"}).text
#         print("change : " + content3)
#         content4 = soup.find("div", {"id" : "qwidget_percent"}).text
#         print("percentage change : " + content4)

#         with open(c, 'a', encoding="utf-8") as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerow([re.sub('\ |\$|', '', content2), content3, content4, now])

#     def seeFile():
        
#         query_string = c                       
#         local_path = r'Desktop'  # r is raw for dealing with backslashes
#         #network_path = r'\\your\network\fold\path'
#         # for a network location
#         #subprocess.Popen(f'explorer /root,"search-ms:query={"pacman.py"}&crumb=location:{network_path}&"')
#         #for a local folder
#         subprocess.Popen(f'explorer /root,"search-ms:query={c}&crumb=folder:{local_path}&"') # subprocess opens the directory in which the file is kept.
#         os.listdir() 

#     seeFile()  

#     NASDAQPlot(c)
