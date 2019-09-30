print("HI!\n") 

from Parse import ParseYahoo, ParseMoneyRediff

j = input("Enter 'a' for Yahoo and 'b' for rediffmoney : ")
if (j=='a'):
    i = input("enter the link for the stock : ")
    ParseYahoo(str(i))
else:
    i = input("enter the link for the stock : ")
    ParseMoneyRediff(str(i))
