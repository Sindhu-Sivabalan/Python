import requests
from bs4 import BeautifulSoup

res=requests.get('https://www.careerindia.com/colleges/colleges-in-chennai/')
# print(res.text)
bs=BeautifulSoup(res.text,'html.parser')
elements=bs.find_all("h2")
for i in elements:
    x=i.find_all('a')
    for y in x:
        # print(y.attrs['href'])
        print(y.text)

elements=bs.find_all("div",class_='edu-det-text')
print(elements)
