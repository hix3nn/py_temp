from bs4 import BeautifulSoup
import requests
import os
type_temp = ['Hi:','Lo: ']

def Main():
    city = input('Type your city: ')
    country = input('If your country is not Brazil type,else press enter: ')
    if country is None:
        country = 'Brazil'
    source = requests.get('https://www.foreca.com/'+country+'/'+city.replace(' ','_')+'?tenday&quick_units=metric').text
    soup = BeautifulSoup(source, "html5lib")
    os.system('cls')
    for each_forecast in soup.find_all('a',class_='cell'):
        print('\n'+'=== '+ each_forecast.find('span',class_='h5').text + ' ===')
        print(' '+each_forecast.div['title'])
        count = 0
        for each_temp in each_forecast.find_all('strong'):
            if '°' in each_temp.text:
                print('- '+type_temp[count]+each_temp.text.replace('+','')+'C')
            else:
                print('- Winds: '+each_temp.text + ' Km/h')
            count += 1
    os.system('pause')
Main()
