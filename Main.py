print("HI!\n") 

from Parse import Parse

j = input("Enter 'a' for Yahoo and 'b' for rediffmoney : ")
if (j=='a'):
    i = input("enter the link for the stock : ")
    Parse(str(i), 0)
else:
    i = input("enter the link for the stock : ")
    Parse(str(i), 1)


































# i = input("So, which one will you choose?\n Press A4 for Apple - NASDAQ\n Press H for HeroMotoCorp - Money Control\n Press R for Reliance Power Ltd - Money Control\n Press A1 for Apple Inc. - Yahoo Finance\n Press F for Facebook Inc. - Yahoo Finance\n Press A2 for Amazon Inc. - Yahoo Finance\n Press A3 for AMD - Bloomberg")
# if (i=="H"):
#     ParseMoneyControl("https://www.moneycontrol.com/india/stockpricequote/auto-2-3-wheelers/heromotocorp/HHM", "HeroMotoCorp.csv")
# elif(i=="A1"):
#     ParseYahoo("https://finance.yahoo.com/quote/AAPL/", "Apple.csv")       
# elif(i=="F"):
#     ParseYahoo("https://finance.yahoo.com/quote/FB/", "Facebook.csv")
# elif(i=="A2"):
#     ParseYahoo("https://finance.yahoo.com/quote/AMZN/", "Amazon.csv")
# elif(i=="R"):
#     ParseMoneyControl("https://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/reliancepower/RP", "ReliancePower.csv")
# elif(i=="A4"):
#     ParseNASDAQ("https://www.nasdaq.com/symbol/aapl", "Apple-NASDAQ.csv")    

# https://money.rediff.com/companies/Hero-Motocorp-Ltd/10540005