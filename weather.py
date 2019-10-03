import requests
from bs4 import BeautifulSoup
import func
#вытаскиваем html
def get_html():
    url='https://weather.com/ru-RU/weather/today/l/55.75,37.58'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('div.today_nowcard-temp')
    temperatura=temp[0].get_text()
    temperatura=func.chif(temperatura)

    #Влажность
    all=soup.select('span')
    vlaj=all[68].get_text()
    vlaj=func.chif(vlaj)

    #Давление
    davlenie=all[72].get_text()
    davlenie=func.chif(davlenie)
    davlenie=davlenie[0:len(davlenie)-1]
    davlenie=str(float(davlenie)*0.750062)
    davlenie=davlenie[0:6]

    #Ветер
    veter=all[67].get_text()
    if veter=='Штиль':
        veter='0'
    else:
        veter=func.chif(veter)
        veter=str(float(veter)/3.6)
    veter=veter[0:6]
    

    #Записываем все в массим для удобства
    itog=[temperatura,davlenie,veter,vlaj]

    return(itog)
#print(get_temp())