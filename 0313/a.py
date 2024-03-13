# 시도별 실시간 측정정보 조회에서  확인 가능한 시도 이름을 전부 작성하시오.
import requests

URL_Seoul = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=tYrpA75r7eSjpJJL2sx78tXPG2HL2Jn8NZxVs38iFbOqtA1F8xrJXrfM%2FjaSJuMxFGAQeDqHa0WkktLH0ANaXA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
URL_ALL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=tYrpA75r7eSjpJJL2sx78tXPG2HL2Jn8NZxVs38iFbOqtA1F8xrJXrfM%2FjaSJuMxFGAQeDqHa0WkktLH0ANaXA%3D%3D&returnType=json&numOfRows=657&pageNo=1&sidoName=%EC%A0%84%EA%B5%AD&ver=1.0"
response1 = requests.get(URL_ALL)
response = requests.get(URL_Seoul)
data1 = response1.json()
response = response.json()
# print(data)
# a. 시도별 실시간 측정정보 조회에서  확인 가능한 시도 이름을 전부 작성하시오.
def get_sido_names(URL_ALL):
    URL_ALL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=tYrpA75r7eSjpJJL2sx78tXPG2HL2Jn8NZxVs38iFbOqtA1F8xrJXrfM%2FjaSJuMxFGAQeDqHa0WkktLH0ANaXA%3D%3D&returnType=json&numOfRows=657&pageNo=1&sidoName=%EC%A0%84%EA%B5%AD&ver=1.0"
    response1 = requests.get(URL_ALL)
    data1 = response1.json()
    
    sido_names = set()
    for item in data1['response']['body']['items']:
        sido_names.add(item['sidoName'])

    return list(sido_names)

sido_names = get_sido_names(URL_ALL)
print(sido_names)
    
# b. 시도별 실시간 측정정보 조회의 서울의 데이터에 대해, 초 미세먼지 농도가 낮은 stationName순으로 정렬하시오.
# 요청 변수에서 한 페이지 결과 수를 최소로 줄여 데이터의 형식을 파악
data = response.get('response').get('body').get("item")
sorted_data = sorted(data, key= lambda x : x.get('pm25Value'))
lst = [[datum.get('stationName'),datum.get('pm25Value')] for datum in sorted_data]
pprint(lst)

# c. 시도별 실시간 측정정보 조회의 서울의 데이터를 stationName으로 접근하기 쉬운 자료구조로 재구성하시오. 단 값이 None인 key는 제외하시오.

# d .종로구의 pm10Value, pm25Value의 1달치 데이터를 정리하시오.