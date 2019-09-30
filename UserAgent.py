import random


def UserAgentFunction():

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
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
    print("\nUser-Agent Sent : %s"%(user_agent))
    return headers

    # 
    # print(response.content)
    # print("-------------------\n\n")

