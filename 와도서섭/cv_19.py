import requests ,xmltodict, json
# from pprint import pprint

# frist_date = "20200315"
# last_date ="20200315"
def get_cv_19_data(frist_date,last_date):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=4GfH2i3tXiTAlgB1urJs7gd3SalAlH0w9dTp3ytpzhhhq8CcaYTF0rMwwVtATbZVLNUw1hLIc1as6IHBPxFvMA%3D%3D&pageNo=1&numOfRows=10&startCreateDt={0}&endCreateDt={1}".format(frist_date,last_date)

    res = requests.get(url)


    #xml을 dict형태로 변환
    data_change1 = xmltodict.parse(res.text)
    #dict형태를 json형태로 변환
    data_change2 = json.dumps(data_change1)
    # json을 dict 형태로 변환
    data_change3 = json.loads(data_change2)


    #type 증명
    # print(type(res.text))
    # print(type(data_change1))
    # print(type(data_change2))
    # print(type(data_change3))

    # totalCount가 제대로 데이터가 가져와졌는지 확인
    totalCount = data_change3["response"]["body"]["totalCount"]
    if totalCount == "0":
        return False

    cv_19_data =data_change3["response"]["body"]["items"]["item"]

    # 확인
    # pprint(cv_19_data)
    return cv_19_data
