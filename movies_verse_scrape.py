# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests,random,time,json,pprint
def fun():
    allDetails=[]
    for i in range(1,23):
        random_sleep=random.randint(1,3)
        url=f'https://moviesverse.org/netflix/page/{i}/'
        res=requests.get(url)
        soup=BeautifulSoup(res.text,'lxml')
        movies=soup.find('div',id="content_box").find_all(class_="latestPost excerpt")
        for movie in movies:
            try:
                link=movie.find('a')['href']
                res2=requests.get(link).text
                soup2=BeautifulSoup(res2,'lxml')
                details=soup2.find('div',class_="thecontent clearfix").find('ul').find_all('li')
                title=details[0].text[10:]
                seasom=int(details[1].text[7:])
                lang=details[3].text[9:].strip()
                formats=details[-1].text[7:]
                main=soup2.find(class_="inline canwrap").find_all('p')
                storyline=main[0].text.strip()
                # print(main[9].find('a'))
                p=soup2.find(class_="single_post").find(class_="imdbwp__meta").find_all('span')
                genre=[p[1].text]
                release_date=p[2].text
                Actors=[soup2.find(class_="imdbwp__footer").find('span').text]
                d={'Title':title,'Season':seasom,'Languages':lang,"Realease Year":release_date,'Storyline':storyline, 'Actors':Actors,'Format':formats,}
                allDetails.append(d)
               
            except:
                None
        time.sleep(random_sleep)
    return allDetails
d=fun()
f=open('movies_verse.json','w')
json.dump(d,f,indent=6)
f.close()