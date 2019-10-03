import requests
from bs4 import BeautifulSoup
import func
#Вытаскиваем html
def get_html():
    url='https://pogoda.mail.ru/prognoz/moskva/'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div.information__content__temperature')
    temperatura=temp[0].get_text()
    temperatura=func.chif(temperatura)

    #Влажность
    wet=soup.select('div.information__content__additional__item')
    vlaj=wet[3].get_text()
    vlaj=func.chif(vlaj)

    #Давление
    bar=soup.select('div.information__content__additional__item')
    davlenie=bar[2].get_text()
    davlenie=func.chif(davlenie)

    #Ветер
    wind=soup.select('div.information__content__additional__item')
    veter=wind[4].get_text()
    veter=func.chif(veter)

    #Записываем все в массим для удобства
    itog=[temperatura,davlenie[0:3],veter,vlaj]
    
    return(itog)
#print(get_temp())