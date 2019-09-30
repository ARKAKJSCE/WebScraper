import urllib.request as ur
import time
 
 
class GoogleRealTime:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
 
    def get(self, symbol, exchange):
        url = self.prefix+"%s:%s"%(exchange, symbol)
        u = ur.urlopen(url)
        content = u.read()
        print(content)
        # obj = json.loads(content[3:])
        return content
 
 
if __name__ == "__main__":
    c = GoogleRealTime()
 
    while 1:
        quote = c.get("MSFT", "NASDAQ")
        print (quote)
        time.sleep(30)