#Web Scraping with python book

#first web scraper
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read(),'lxml')
print(bsObj.h1)
print(bsObj.contents)
bsObj.html
bsObj.body

#War and Peace Example
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(),"lxml")
nameList = bsObj.find_all("span",{"class":"green"})
for name in nameList:
    print(name.get_text()) #a função get text elimina todo o conteúdo capturado que não é texto, obs: a funcao get_text deve ser sempre a ultima coisa a ser feita. Devemos sempre tentar preservar ao maximo os objetos bs.
nameList
nameList = bsObj.find_all(text="the prince")
print(len(nameList))

allText = bsObj.findAll(id="text")
print(allText[0].get_text())

#children

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
