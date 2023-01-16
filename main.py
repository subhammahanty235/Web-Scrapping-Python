from bs4 import BeautifulSoup
with open('index.html','r') as web_file :
    content = web_file.read()
    # print(content)
    suop = BeautifulSoup(content , 'lxml')
    # print(suop.prettify())
    # tags = suop.find('p') #it will only find the first element or first p tag
    tags = suop.find_all('p')
    for tag in tags:
        # print(tag)
        # print(tag.text)
        print(tag)
    # print(tags)

