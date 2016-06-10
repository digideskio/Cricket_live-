from flask import render_template
from commentry_parser import Commentry
from urllib2 import urlopen
from Article_Info import Article
from bs4 import BeautifulSoup
import requests
from app import app

# @app.route('/')
# @app.route('/index')
# def index():
#     data = Get_Data.get_data("http://cricapi.com/api/cricket")
#     return render_template('test.html',data= data)

@app.route('/')
@app.route('/index')
def feed():
    url = 'http://www.espncricinfo.com/bangladesh/content/team/25.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    list = []
    list_obj = []
    titles = soup.findAll(attrs={'class': 'featured-link'})
    for post in titles:
        list.append("http://www.espncricinfo.com" + post.a.get('href'))

    for x in range(0, len(list)):
        url = list[x]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        article = soup.findAll("section", {'class': 'main-content'})
        ob = Article()
        ob.getArticle(article[0])
        list_obj.append(ob.__dict__)

    # print list_obj
    return render_template('feed.html',data= list_obj, counter = 1)


# @app.route('/scorecard/<match_id>')
# def scorecard(match_id):
#     data = Get_Data.get_commentary("http://cricapi.com/api/cricketCommentary?unique_id="+ match_id)
#     print data
#     # soup = BeautifulSoup(data, "html5lib")
#     # ob = Get_comm()
#     # ob.getComm(soup)
#     #
#     # ovr = ob.__dict__['commentary_overs']
#     # comment = ob.__dict__['commentary_text']
#     #
#     # ob.makdict(ovr, comment)
#     #
#     # details = ob.__dict__['details']
#
#     return render_template('scorecard.html', details= data)


@app.route('/scorecard/<match_id>')
def scorecard(match_id):
    url = "http://www.espncricinfo.com/ci/engine/match/%s.html?innings=1;view=commentary" % ( match_id ,)
    print url
    soup = BeautifulSoup(urlopen(url), "html5lib")
    commentry_section = soup.find('div', 'commentary-section')

    ob = Commentry()
    ob.getCommentry(commentry_section)

    # print ob.__dict__
    return render_template('scorecard.html', data = ob.details)
