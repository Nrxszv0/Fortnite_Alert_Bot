import bs4 as bs
import urllib.request
from alert import *

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'


url = "https://fnitemshop.com/"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() 


soup = bs.BeautifulSoup(data, 'lxml')
print(soup.find_all('h3'))








