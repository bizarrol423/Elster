import requests
import json
import math
from data import token
import pandas as pd

'''
получение информации от Яндекса
'''
def get_info(SearchedOrganization: str) -> dict:
    url = "https://search-maps.yandex.ru/v1/"+\
    f"?apikey={token}"+\
    f"&text={SearchedOrganization}"+\
    "&lang=ru_RU"+\
    "&type=biz"+\
    "&results=500"
    return json.loads(requests.get(url=url).text)

'''
возврат словаря с данными
'''
def get_dict(SearchedOrganization: str, X:str = "", Y:str = "", distance:str = "") ->dict:
    GetedData = get_info(SearchedOrganization=SearchedOrganization)
    distance_to_object = ""
    name = []
    address = []
    url = []
    phone_number = []
    work_time = []
    coordinates_building = []
    distance_to_point = []
    if (distance != ""): # если задан радицс поиска
        distance = float(distance)/1000
    for object in GetedData["features"]:
        number_phones = ""
        coordinates = object["geometry"]["coordinates"]
        if (X != "" and Y != ""): # если есть координаты поиска
            distance_to_object = distance_calculation([float(coordinates[1]), float(coordinates[0])],[float(X),float(Y)])
        if (str(distance) != ""): # если задан радицс поиска
            if (distance_to_object > distance):
                continue
        coordinates_building.append([coordinates[1],coordinates[0]])
        name.append(object["properties"]["name"])
        address.append(object["properties"]["CompanyMetaData"]["address"])
        url.append(object["properties"]["CompanyMetaData"].get("url"))
        phones = object["properties"]["CompanyMetaData"].get("Phones")
        if phones != None:
            for phone in phones:
                print(phone)
                #number_phones += f"|{phone["formatted"]}| "
        phone_number.append(number_phones)
        work_hours = object["properties"]["CompanyMetaData"].get("Hours")
        if work_hours != None:
            work_time.append(work_hours["text"])
        else:
            work_time.append("None")
        distance_to_point.append(distance_to_object)
        data_from_table = {
            "название":name,
            "адресс":address,
            "ссылка":url,
            "телефоны":phone_number,
            "время работы":work_time,
            "дистанция до точки":distance_to_point,
            "координаты здания":coordinates_building
        }
    return data_from_table

'''
импорт данных в excel
'''
def data_to_excel(data: dict) -> bool:
    df = pd.DataFrame(data)
    df.to_excel('data.xlsx', index=False)

'''
импорт данных в csv
'''
def data_to_csv(data: dict) -> bool:
    df = pd.DataFrame(data)
    df.to_csv('data.csv', encoding='utf-8', sep='\t', index=False)


'''
расчёт километов между двумя точками на карте
'''
def distance_calculation(point1: list, point2: list) -> float:
    lat1 = math.radians(point1[0])
    lon1 = math.radians(point1[1])
    lat2 = math.radians(point2[0])
    lon2 = math.radians(point2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1)  *  math.cos(lat2)  *  math.sin(dlon/2)  *  math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c
    return round(distance,2)

'''
перевод километров в градусы
'''
def kilometers_to_degrees(kilometers):
    theta = kilometers / 6371
    degrees = math.degrees(theta)
    return degrees
