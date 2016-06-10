from Article_Info import Article
from bs4 import BeautifulSoup
from Save_data import Save_data
import requests
import xlsxwriter


url= 'http://www.espncricinfo.com/bangladesh/content/team/25.html'
r = requests.get(url)

soup = BeautifulSoup(r.text,"html5lib")


list = []
list_obj = []
titles = soup.findAll(attrs={'class': 'featured-link'})

for post in titles:
    list.append("http://www.espncricinfo.com"+post.a.get('href'))

for x in range(0,len(list)):
    url = list[x]
    print url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    article = soup.findAll("section",{'class': 'main-content'})
    ob = Article()
    ob.getArticle(article[0])
    list_obj.append(ob.__dict__)

print list_obj

obj = Save_data()
obj.save(list_obj)


