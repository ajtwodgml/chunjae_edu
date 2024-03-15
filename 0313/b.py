# c. 시도별 실시간 측정정보 조회의 서울의 데이터를 stationName으로 접근하기 쉬운 자료구조로 재구성하시오. 단 값이 None인 key는 제외하시오.
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

# d .종로구의 pm10Value, pm25Value의 1달치 데이터를 정리하시오.
import requests
from pprint import pprint
from collections import defaultdict


URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=MONTH&ver=1.0"
response = requests.get(URL)

response = response.json()

data = response.get('response').get('body').get('items')

my_data_10 = defaultdict(list)
my_data_25 = defaultdict(list)

for datum in data:
    dataTime = datum.get('dataTime').split()[0]
    try :
        pm10Value = int(datum.get('pm10Value'))
        pm25Value = int(datum.get('pm25Value'))
        my_data_10[dataTime].append(pm10Value)
        my_data_25[dataTime].append(pm25Value)
    except:
        pass

print(my_data_10)
print(my_data_25)


def average(lst):
    return sum(lst)/len(lst)

my_data_10 = [{key : average(value)} for key, value in my_data_10.items()]
my_data_25 = [{key : average(value)} for key, value in my_data_25.items()]

print(my_data_10)
print(my_data_25)