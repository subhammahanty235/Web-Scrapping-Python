from bs4 import BeautifulSoup as bs
import requests
import csv
url = "https://www.passiton.com/inspirational-quotes"
data = requests.get(url)
suop = bs(data.content , 'html5lib')
quotes = []  # a list to store quotes
table = suop.find('div' , attrs={'id':'all_quotes'})
# print(table.prettify())
# print('ddd')
for row in table.find_all('div' , attrs={'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {'theme': row.h5.text, 'url': row.a['href'], 'img': row.img['src'], 'lines': row.img['alt'].split(" #")[0],
             'author': row.img['alt'].split(" #")[1]}
    # print(quote)
    print("done")
    quotes.append(quote)
filename = 'inspirational_quote.csv'
with open(filename , 'w' ,newline='') as f:
    w = csv.DictWriter(f , ['theme' ,'url' , 'img' , 'lines' ,'author'])
    w.writeheader()
    i = 1
    for quote in quotes:
        w.writerow(quote)
        i+=1
    print(f"{i} quotes Saved Successfully")
# for quote in quotes:
#     print(quote)