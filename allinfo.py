import weather,yandex,mail,msn,wunderground
def pogoda():
    try:
        yandex1=yandex.get_temp()
        mail1=mail.get_temp()
        msn1=msn.get_temp()
        weather1=weather.get_temp()
        wunderground1=wunderground.get_temp()

        temperatura='Температура в данный момент равна '+str(round((float(yandex1[0])+float(mail1[0])+float(msn1[0])+float(weather1[0])+float(wunderground1[0]))/5))+'℃'
        davlenie='Давление в данный момент равно '+str(round((float(yandex1[1])+float(mail1[1])+float(msn1[1])+float(weather1[1])+float(wunderground1[1]))/5))+' мм.рт.ст'
        veter='Скорость ветра в данный момент равна '+str(round((float(yandex1[2])+float(mail1[2])+float(msn1[2])+float(weather1[2])+float(wunderground1[2]))/5))+'м/с'
        vlaj='Влажность в данный момент равна '+str(round((float(yandex1[3])+float(mail1[3])+float(msn1[3])+float(weather1[3])+float(wunderground1[3]))/5))+'%'
        
        return temperatura+'\n'+davlenie+'\n'+veter+'\n'+vlaj
    except:
        return 'bug'



