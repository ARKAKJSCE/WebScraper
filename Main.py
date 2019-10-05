print("HI!\n") 

from Parse import Parse

j = input("Enter 'a' for Yahoo and 'b' for rediffmoney : ")
if (j=='a'):
    i = input("enter the link for the stock : ")
    Parse(str(i), 0)
else:
    i = input("enter the link for the stock : ")
    Parse(str(i), 1)
