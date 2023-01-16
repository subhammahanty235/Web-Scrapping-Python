# here we willl try to scrap data from multiple pages of a website
from bs4 import BeautifulSoup as bs
import requests
# url = 'https://www.geeksforgeeks.org/page/1/'
# data = requests.get(url)
# suop = bs(data.text , 'lxml')
# titles = suop.find_all('div' , attrs={'class','head'})
# for title in titles:
#     print(title.text)

url = "https://www.geeksforgeeks.org/page/"
for page in range(1,10):
    req = requests.get(url + str(page)+ '/')
    suop = bs(req.text ,'lxml')
    titles = suop.find_all('div',{'class','head'})
    for i in range(4 ,19):
        if(page>1):
            print(f"{(i-3)+page*15}" + titles[i].text)
        else:
            print(f"{i-3}"+titles[i].text)