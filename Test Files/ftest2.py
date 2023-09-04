import bs4 as bs
import urllib.request
import schedule
import time
from alert import *
import datetime

# email_alert("6366759462@txt.att.net", "Fortnite Item Skins", "test test")

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
while True:
    x = datetime.datetime.now()
    second = x.strftime("%S")[1]

    url = "https://fnitemshop.com/"
    # url = "https://fnitemshop.com/13-july-2021-fortnite-item-shop/"
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() 


    soup = bs.BeautifulSoup(data, 'lxml')
    # print(soup.find_all('img'))
    items = []
    for img in soup.find_all('img', alt=True, width=300):
        items.append(img['alt'])
        # print(img['alt'])
    str = ""
    if second == "5": 
        if("Guernsey Fortnite Skin") in items:
            str = "cow skin. dub dub dub dub dub. get on fortnite now"
            print(str)
            email_alert("6366759462@txt.att.net", "Fortnite Item Skins", str)
        else:
            str = "no cow skin. sad sad sad"
            print(str)
            email_alert("6366759462@txt.att.net", "Fortnite Item Skins", str)    
    
    # print(second)

    time.sleep(1)



# items = []

# for img in soup.find_all('img', alt=True, width= 300):
#     items.append(img['alt'])
#         # print(img['alt'])

# print(items)
# for item in items:
#     print(item)
# string = "Noooooooooo Cow Skin"
# if("Guernsey Fortnite Skin") in items:
#     print("cow skin")
#     string = "COW SKIN IS IN THE SHOP!!!!!! GET ON FORTNITE"
        



# email_alert("6366759462@txt.att.net", "Fortnite Item Skins", string)


# #url = "https://fnitemshop.com/13-july-2021-fortnite-item-shop/"