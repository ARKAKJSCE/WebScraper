from time import sleep
from selenium import webdriver
from UserAgent import UserAgentFunctionGoogle
import csv as _csv_
from bs4 import BeautifulSoup as bs
from datetime import datetime

def ParseSeleniumRediff(URL):

    sleep(40)
    now = datetime.now().strftime('%H:%M:%S')
    print("Retrying with alternate method. Please stay patient.")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    options.add_argument(f'user-agent={UserAgentFunctionGoogle()}')

    options.add_argument('--remote-debugging-port=9222')

    browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", options=options)
    browser.get(URL)
    html_source = browser.page_source
    soup = bs(html_source, "html.parser")

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

# (str(ParseName()) + ".csv")         