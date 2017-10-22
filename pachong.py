
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import sqlite3

a = request.Request("http://www.hxnews.com/news/ty/tyxw/201710/20/1327928.shtml")
postdata = parse.urlencode([
        ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
        ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
        ("SearchDate", "2017/10/17"),
        ("SearchTime", "12:30"),
        ("SearchWay", "DepartureInMandarin")
])
a.add_header("User-Agent",
                 "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
a.add_header("Origin", "http://www.hxnews.com")
resp = request.urlopen(a)
soupx = BeautifulSoup(resp.read().decode("utf-8"), "html.parser")

href2 = []
for link in soupx.find_all('a', attrs={'class': 'title'}):
    href2.append(link.get('href'))

timex = []
for time1 in soupx.find_all('span', attrs={'class': 'time-source'}):
    timex.append(time1.string)

titalx = []
for t in soupx.find_all('div', attrs={'class': 'page-header'}):
    titalx.append(t.get_text())

editorx = []
for editor1 in soupx.find_all('p', attrs={'class': 'article-editor'}):
    editorx.append(editor1.string)

passagex = []
passage2 = soupx.find_all('div', attrs={'class': 'article article_16 article-content fontSizeSmall'})
for i in passage2:
    passagex.append(i.get_text())


for c in href2:
    x = request.Request(c)
    postdata = parse.urlencode([
            ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
            ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
            ("SearchDate", "2017/10/17"),
            ("SearchTime", "12:30"),
            ("SearchWay", "DepartureInMandarin")
    ])
    x.add_header("User-Agent",
                     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    x.add_header("Origin", "http://www.hxnews.com")
    respx = request.urlopen(x)
    soupx = BeautifulSoup(respx.read().decode("utf-8"), "html.parser")

    for time1 in soupx.find_all('span', attrs={'class': 'time-source'}):
        timex.append(time1.string)

    for t in soupx.find_all('div', attrs={'class': 'page-header'}):
        titalx.append(t.get_text())

    for editor1 in soupx.find_all('p', attrs={'class': 'article-editor'}):
        editorx.append(editor1.string)

    passage2 = soupx.find_all('div', attrs={'class': 'article article_16 article-content fontSizeSmall'})
    for i in passage2:
        passagex.append(i.get_text())

conn = sqlite3.connect("db.sqlite3")
conn.text_factory = str
cursor = conn.cursor()
cursor.execute("create table app_pachong9 (id integer primary key autoincrement,title text NULL,time text NULL,people text NULL,passage text NULL)")

for y in range(0,len(titalx)):
    conn.execute("insert into app_pachong9 values (?,?,?,?,?)", (y,titalx[y],timex[y],editorx[y],passagex[y]))
print(cursor.rowcount)
conn.commit()
cursor.close()
conn.close()