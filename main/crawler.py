import requests,re,urllib.request
from bs4 import BeautifulSoup

target_url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

print("== Crawling Start! ==")
product_link = list()
product_info = list()


for table in soup.findAll(attrs={'valign': 'middle'}):
    for td in table.findAll('tr'):
        for a in td.findAll('a'):
            product_link+=[a['href']]

for link in product_link:
    info=dict()
    target_url = "http://www.ppomppu.co.kr/zboard/"+link
    html = urllib.request.urlopen(target_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(attrs={'class':'info_bg'})
    link = table.find('a')['href']
    print(link)
    

