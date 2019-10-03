import requests
from bs4 import BeautifulSoup
import func
#Вытаскиваем html
def get_html():
    url='https://www.msn.com/ru-ru/weather/today/%d0%9c%d0%be%d1%81%d0%ba%d0%b2%d0%b0,%d0%9c%d0%be%d1%81%d0%ba%d0%b2%d0%b0,%d0%a0%d0%be%d1%81%d1%81%d0%b8%d1%8f/we-city?iso=RU&el=hBymWZkJlYygdY0zF4R7Vw%3D%3D'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')
    #парсим данные
    all=soup.select('div.weather-info')
    all2=all[0].get_text()
    s=''
    s1=[]
    for i in range(len(all2)):
        if all2[i]!='\n':
            s+=all2[i]
        else:
            s1.append(s)
            s=''
    
    #Температура
    temp=soup.select('span.current')
    temperatura=temp[0].get_text()
    temperatura=func.chif(temperatura)

    #Влажность
    vlaj=func.chif(s1[7])

    #Давление
    davlenie=func.chif(s1[5])

    #Ветер
    veter=func.chif(s1[4])

    #Записываем все в массим для удобства
    itog=[temperatura,davlenie,veter,vlaj]
    
    return(itog)
#print(get_temp())