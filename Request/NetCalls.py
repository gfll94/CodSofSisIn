import requests
import shutil
import json


class NetCalls:
    api_key = ''
    def llamada(self):
        url = 'https://github.com/'
        r = requests.get(url)
        print(r)
        print(r.content)
        print(r.status_code)
    
    def sombrero_de_paja(self,url,file_name):
        res = requests.get(url,stream = True)
        if 200==res.status_code:
            with open(file_name, 'wb')as f:
                shutil.copyfileobj(res.raw, f)
            print('imagen desgargada corrctamente')
        else:
            print('no se encontro la imagen')

    def clima(self,city):
        base_url = 'https://api.openweather map.org/data/2.5/weather?'
        params = {'q':city, 'appid' :self.api_key, 'units':'metric'}
        try:
            r = requests.get(base_url,params=params)
            r. raise_for_status()
            weather_data = r.json()

            if 200 == weather_data['cod']:
                print(f'el clima en{weather_data['name']}')
        except:
            print('Error')


r=NetCalls()
r.llamada()
r.sombrero_de_paja('https://m.media-amazon.com/images/I/61tsl2SqUpS._AC_SL1002_.jpg', 'sombrero.jpg')









