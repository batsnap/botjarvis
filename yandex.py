import requests
from bs4 import BeautifulSoup
import func
def get_html():
    url='https://yandex.ru/pogoda/moscow'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('span.temp__value')
    temperatura=temp[0].get_text()
    temperatura=func.chif(temperatura)
    #Ветер
    all=soup.select('dd.term__value')
    veter=all[2].get_text()
    veter=func.chif(veter)
    if len(veter)==0:
        veter='0'
    else:
        veter=veter[0:len(veter)-2]

    #Влажность
    vlaj=all[3].get_text()
    vlaj=func.chif(vlaj)

    #Давление
    davlenie=all[4].get_text()
    davlenie=func.chif(davlenie)

    #Итог
    itog=[temperatura,davlenie[0:3],veter,vlaj]
    
    return(itog)
#print(get_temp())