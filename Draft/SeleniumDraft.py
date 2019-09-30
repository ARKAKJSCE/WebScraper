from time import sleep

import bs4 as bs
from selenium import webdriver

from UserAgent import UserAgentFunctionGoogle

options = webdriver.ChromeOptions()
for x in range(3):
    
    sleep(40)
    options.add_argument('headless')

    options.add_argument(f'user-agent={UserAgentFunctionGoogle()}')

    options.add_argument('--remote-debugging-port=9222')

    browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe",
    options=options)
    url = ("https://money.rediff.com/companies/Hero-Motocorp-Ltd/10540005")
    browser.get(url)
    html_source = browser.page_source
    soup = bs.BeautifulSoup(html_source, "html.parser")
    # sleep(10000)   # Use this for opening chrome devtools by visiting localhost:9222 and opening the link in a new tab. 
    browser.quit()
    print(soup.prettify())
    # name = soup.find("span", {"aria-level" : "2"}).text
    # price = soup.find("span", {"class" : "cwUqwd"}).text


    # name = soup.find("h1" , {"data-reactid" : "7"}).text
    # price = soup.find("span", {"class" : "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}, {"data-reactid" : "14"}).text

    # print(name)
    # print(price)

    



# for x in range(15):
#     sleep(20)
#     options.add_argument('headless')

#     options.add_argument(f'user-agent={UserAgentFunctionGoogle()}')

#     browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", options=options)
#     url = ("https://www.google.com/finance?q=tsla")
#     browser.get(url)
#     html_source = browser.page_source
#     soup = bs.BeautifulSoup(html_source, "html.parser")
#     browser.quit()






# soup1 = soup.prettify()
# with open('browser.txt', 'w', encoding="utf-8") as f:                 
#         for name in soup1:                                             
#             f.write(str(name))        

# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", chrome_options=options)
# driver.implicitly_wait(5)
# # driver.maximize_window()
# driver.get("https://www.google.com")
# search_field = driver.find_element_by_name("q")
# search_field.send_keys("Selenium WebDriver Interview questions")
# search_field.submit()
# lists= driver.find_elements_by_class_name("ellip")
# print ("Found " + str(len(lists)) + " searches:")
# i=0
# for listitem in lists:
#    print (listitem.get_attribute("innerHTML"))
#    i=i+1
#    if(i>10):
#       break

# driver.close()


# for x in range(5):

#     sleep(20)
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')

#     # ua = UserAgent()
#     # userAgent = ua.random
#     # print(userAgent)
#     options.add_argument(f'user-agent={UserAgentFunctionGoogle()}')

#     browser = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe", options=options)
#     url = ("https://www.google.com/finance?q=tsla")
#     browser.get(url)
#     html_source = browser.page_source
#     browser.quit()
#     soup = bs.BeautifulSoup(html_source, "html.parser")

#     # name = soup.find("span", {"aria-level" : "2"}).text
#     # price = soup.find("span", {"class" : "cwUqwd"}).text

#     # # print(name)
#     # print(price)

#     print(soup.prettify())
#     soup1 = soup.prettify()
#     with open('browser.txt', 'w', encoding="utf-8") as f:                 
#             for name in soup1:                                             
#                 f.write(str(name))  
