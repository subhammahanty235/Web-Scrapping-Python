from bs4 import BeautifulSoup as bs
import requests
import csv

url = 'https://www.geeksforgeeks.org/page/'
req = requests.get(url)
suop = bs(req.text , 'lxml')
titles = suop.find_all('div',attrs={'class' , 'head'})
titles_list = []

count = 1
for title in titles:
    d = {}
    d['Title Number'] = f"Title {count}"
    d['Title Name'] = title.text
    count+=1
    titles_list.append(d)
file_name = "scrapdata.CSV"
with open(file_name ,'a' , newline='')as f:
    w = csv.DictWriter(f ,['Title Number' ,'Title Name'])
    w.writeheader()

    w.writerows(titles_list)