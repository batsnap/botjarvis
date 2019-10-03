import requests
from bs4 import BeautifulSoup
import func
#Вытаскиваем html
def get_html():
    url='https://www.wunderground.com/weather/ru/moscow/55.76,37.62'
    r=requests.get(url)
    r=r.text
    return r

#Берём данные температуры, влажности и давление и ложим в массив.
def get_temp():
    html=get_html()
    soup=BeautifulSoup(html,'lxml')

    #Температура
    temp=soup.select('span.wu-value.wu-value-to')
    temperatura=temp[1].get_text()
    temperatura=func.chif(temperatura)
    temperatura=str((float(temperatura)-32)*(5/9))
    
    #Влажность
    all=soup.select('span.wu-value.wu-value-to')
    vlaj=all[13].get_text()
    vlaj=func.chif(vlaj)

    #Давление
    
    if float(float(func.chif(all[9].get_text()))*25.4)>700:
        davlenie=all[9].get_text()
        vlaj=all[12].get_text()
        vlaj=func.chif(vlaj)
    elif float(float(func.chif(all[10].get_text()))*25.4)>700:
        davlenie=all[10].get_text()
        vlaj=all[13].get_text()
        vlaj=func.chif(vlaj)
    
    davlenie=str(float(func.chif(davlenie))*25.4)

    #ветер
    wind=soup.select('div.wind-speed')
    veter=wind[0].get_text()
    veter=func.chif(veter)
    #Записываем все в массим для удобства
    itog=[temperatura,davlenie,veter,vlaj]
    
    return(itog)
#print(get_temp())