from hashlib import md5
from requests import get 
from datetime import datetime

class restmarvel:
    trimestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = '2d3397285cb23decdb1b9652ef5fd4b6'
    priv_key = '2c59777925a62ef01e2182ce3be05ec4da11d5e3'


    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.trimestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    

    def get_heroes(self):
        params = {'ts':self.trimestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)
        data = results.json()
        print(data)
        print(data['status'])
    
    def get_pokemon(sefl):
        for i in range(1,152):
            print('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'+str(i)+'.png')


res=restmarvel()
#res.get_heroes()
res.get_pokemon()