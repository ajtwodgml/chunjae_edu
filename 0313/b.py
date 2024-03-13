import requests
from pprint import pprint

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
response = requests.get(URL)

response = response.json()

data = response.get('response').get('body').get('items')

my_data = dict()

for datum in data:
    stationName = datum.get('stationName')
    del datum['stationName']
    
    dic = dict()
    for key, value in datum.items():
        if value is not None:
            dic[key] = value
    my_data[stationName] = dic

pprint(my_data)