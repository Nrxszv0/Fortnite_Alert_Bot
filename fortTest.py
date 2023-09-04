import bs4 as bs
import urllib.request
import schedule
import time
from alert import *
url ="https://fnitemshop.com/"
#url = "https://fnitemshop.com/13-july-2021-fortnite-item-shop/"
sauce = urllib.request.urlopen(url).read()

soup = bs.BeautifulSoup(sauce, 'lxml')
def send_stuff():
    items = []

    for img in soup.find_all('img', alt=True, width= 300):
        items.append(img['alt'])
        # print(img['alt'])

    #print(items)
    for item in items:
        print(item)
    string = "Noooooooooo Cow Skin"
    if("Guernsey Fortnite Skin") in items:
        print("cow skin")
        string = "COW SKIN IS IN THE SHOP!!!!!! GET ON FORTNITE"
        

    # string = ''.join(items)

    if __name__ == '__main__':    
        email_alert("6366759462@txt.att.net", "Fortnite Item Skins", string)
        #email_alert("3145418844@vtext.com", "Fortnite Item Skins", string)
schedule.every(1).days.do(send_stuff)

while 1:
    schedule.run_pending()
    time.sleep(1)