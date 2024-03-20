import requests
import func
from data import token


if __name__ == '__main__':
    SearchedOrganization = "театры"
    url = "https://search-maps.yandex.ru/v1/"+\
    f"?apikey={token}"+\
    f"&text={SearchedOrganization}"+\
    "&lang=ru_RU"+\
    "&type=biz"+\
    "&results=500"
    print(requests.get(url=url).text)
