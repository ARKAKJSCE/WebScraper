from bs4 import BeautifulSoup as bs
import requests
import time
import random

for x in range(7):

    time.sleep(30)
    # ua = UserAgent()
    # header = {'User-Agent':str(ua.chrome)}
    
    user_agent_list = [
        "Mozilla/5.0", 
        "Mozilla/5.001", 
        "Mozilla/6.0", 
        "Opera 9.4", 
        "Opera 9.60", 
        "Opera/10.50",
        "Opera/10.60", 
        "Opera/7.0",
        "Opera/7.10",
        "Opera/6.0",
        "Opera/5.12",
        "Opera/5.11",
        "Opera/5.02",
        "Opera/5.0",
        "Opera/6.03",
        "Opera/6.04",
        "Opera/6.05",
        "Opera/6.11",
        "Opera/6.12",
        "Opera/7.02",
        "Mozilla/4.0"
    ]
    User_agent = random.choice(user_agent_list)
    session = requests.Session()

    url_list = [
        "BABA",
        "DOVA",
        "CGC",
        "THO",
        "BBBY",
        "ACB",
        "AAPL",
        'JD',
        'ACB.TO',
        'HUYA',
        'TROV',
        'NWL',
        'IMMU',
        'TLRY'
    ]
    url = random.choice(url_list)

    page = session.get(("https://finance.yahoo.com/quote/" + url), headers={"User-Agent":User_agent})
    soup = bs(page.content, "html.parser")
    c = soup.find("span", {"data-reactid" : "16"}).text
    p = soup.find("span", {"data-reactid" : "14"}).text
    print(User_agent)
    print(url)
    print(p)
    print(c)
    print("\n")