import requests
import json
from data import token

def get_info(SearchedOrganization: str) -> dict:
    url = "https://search-maps.yandex.ru/v1/"+\
    f"?apikey={token}"+\
    f"&text={SearchedOrganization}"+\
    "&lang=ru_RU"+\
    "&type=biz"+\
    "&results=500"
    return json.loads(requests.get(url=url).text)
