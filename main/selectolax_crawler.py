from selectolax.parser import HTMLParser
import re, urllib.request, requests
#from .models import Product

def ppomppuList(page):
    linkList = set()
    for i in range(1,page+1):
        url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page="+str(i)+"&divpage=62"
        r = requests.get(url)
        html = r.text
        parsedList = HTMLParser(html)
        linkSelector = 'a[href^="view.php?id=ppomppu"]'
        prod = parsedList.css(linkSelector)
        for p in prod:
            linkList.add("http://www.ppomppu.co.kr/zboard/view.php?id=ppomppu&page="+str(page)+"&divpage=62&no="+p.attributes['href'][-6:])
    return list(linkList)

def ppomppuSpec(linkList):
    prodList = list()
    print(linkList)
    for link in list(linkList):
        parsedProd = HTMLParser(requests.get(link).text)
        title = parsedProd.css_first('font.view_title2').text()
        cate = parsedProd.css_first('font.view_cate').text()
        mallLink = parsedProd.css_first('a[href^="http://s.ppomppu.co.kr?"').text()
        try:
            image = parsedProd.css_first('img[src^="//cdn.ppomppu.co.kr/zboard/data3/2020"').attributes['src'][2:]
            image = 'https://'+image
        except : image = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png" 
        prodList.append({'name':title,'category':cate,'image':image,'mall_link':mallLink,'link':link})
    return prodList

def fmkList(page):
    linkList = set()
    for i in range(1,page+1):
        if i==1: url="https://www.fmkorea.com/hotdeal"
        else : url = "https://www.fmkorea.com/index.php?mid=hotdeal&page="+str(i)
        r = requests.get(url)
        html = r.text
        parsedList = HTMLParser(html)
        linkSelector = 'a.hotdeal_var8'
        prod = parsedList.css(linkSelector)
        for p in prod:
            linkList.add("https://www.fmkorea.com"+p.attributes['href'])
    return list(linkList)

def fmkSpec(linkList):
    prodList = list()
    print(linkList)
    for link in list(linkList):
        parsedProd = HTMLParser(requests.get(link).text)
        spec = parsedProd.css('div.xe_content')
        mallLink = spec[0].text()
        mall = spec[1].text().split('[')[0].strip()
        title = spec[2].text().strip()                        
        price = spec[3].text().strip()
        cate = parsedProd.css_first('a.category').text().strip()
        #mallLink = parsedProd.css_first('a[href^="https://link.fmkorea.com/link.php?url="').text()
        print(title,cate,mall,price,mallLink,link)
    
    return prodList

def clienList(page):
    linkList = set()
    for i in range(0,page):
        if i==0: url="https://www.clien.net/service/board/jirum?category=상품정보"
        else : url = "https://www.clien.net/service/board/jirum?&od=T31&category=상품정보&po="+str(i)
        r = requests.get(url)
        html = r.text
        parsedList = HTMLParser(html)
        '''linkSelector = 'a[href$="groupCd="]'
        prod = parsedList.css(linkSelector)
        for p in prod:
            linkList.add("https://www.clien.net"+p.attributes['href'])'''
        tile = parsedList.css_first('span.list_subject')
        print(tile.child.text())
            

    return list(linkList)