import requests ,xmltodict, json

def get_weather2_data(frist_date,key,time):
    
    x = 55
    y = 124
    if key == "서울":
        x = 60
        y = 127
    if key == "부산":
        x = 98
        y = 76
    if key == "대구":
        x = 89
        y = 90
    if key == "인천":
        x = 55
        y = 124
    if key == "광주":
        x = 58
        y = 74
    if key == "대전":
        x = 67
        y = 100
    if key == "울산":
        x = 102
        y = 84
    if key == "세종":
        x = 66
        y = 103
    if key == "경기":
        x = 60
        y = 120
    if key == "강원":
        x = 73
        y = 134
    if key == "충북":
        x = 69
        y = 107
    if key == "충남":
        x = 68
        y = 100
    if key == "전북":
        x = 51
        y = 67
    if key == "전남":
        x = 63
        y = 89
    if key == "경북":
        x = 89
        y = 91
    if key == "경남":
        x = 91
        y = 77
    if key == "제주":
        x = 52
        y = 38
    
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst?serviceKey=4GfH2i3tXiTAlgB1urJs7gd3SalAlH0w9dTp3ytpzhhhq8CcaYTF0rMwwVtATbZVLNUw1hLIc1as6IHBPxFvMA%3D%3D&numOfRows=10&pageNo=1&base_date={0}&base_time={1}&nx={2}&ny={3}".format(frist_date,time,x,y)


    res = requests.get(url)

    #xml을 dict형태로 변환
    data_change1 = xmltodict.parse(res.text)
    #dict형태를 json형태로 변환
    data_change2 = json.dumps(data_change1)
    # json을 dict 형태로 변환
    data_change3 = json.loads(data_change2)



    
    try:
        weather_data =data_change3["response"]["body"]["items"]["item"]

        return weather_data
    except:
        return False
