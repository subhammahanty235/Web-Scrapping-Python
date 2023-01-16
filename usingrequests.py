from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# print(data)
suop = BeautifulSoup(data.content , 'lxml')
# print(suop.prettify())
links = suop.find_all('a')
with open('data.txt' , 'a') as dt:
    i =0
    for link in links:
        dt.write('\n')
        dt.write(link.get('href'))
        print(f'successfull {i}')
        i = i+1