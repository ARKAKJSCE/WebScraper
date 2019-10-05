import random


def UserAgentFunction():

    user_agent_list = [
        "Mozilla/5.0", 
        "Mozilla/6.0", 
        "Opera 9.4", 
        "Opera 9.60", 
        "Opera/10.50",
        "Opera 10.60", 
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
        "Mozilla/4.0",
        "Mozilla/4.5",
        "Mozilla/4.7",
        "Thunderstorm/1.0",
        "Yandex/1.01.001",
        "BrightSign/8.0.69",
        "Opera/9.80",
        "Apache/2.4.25",
        "Wget/1.12",
        "Outlook-Express/7.0"
        "Thunderstorm/2.0"
        "Outlook-Express/7.3"
    ]
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent, 'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8'}
    print("\nUser-Agent Sent : %s"%(user_agent))
    return headers

    # 
    # print(response.content)
    # print("-------------------\n\n")

