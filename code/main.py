import func


if __name__ == '__main__':
    SearchedOrganization = "театры Новосибирск"
    GetedData = func.get_info(SearchedOrganization)
    for features in GetedData['features']:
        print(features['properties']['name'], end=' ')
        print(features['properties']['CompanyMetaData']['address'], end=' ')
        print(features['properties']['CompanyMetaData']['url'], end=' ')
        for phone in features['properties']['CompanyMetaData']['Phones']:
            print(phone['formatted'], end=' ')
        print(features['geometry']['coordinates'], end=' ')
        print(features['properties']['CompanyMetaData']['Hours']['text'], end=' ')
        for i in features['properties']['CompanyMetaData']['Categories']:
            print(i['name'], end=' ')
        print()
        

#{'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [82.924504, 55.030439]}, 'properties': {'name': 'Новосибирский театр оперы и балета', 'description': 'Красный просп., 36, Новосибирск, Россия', 'boundedBy': [[82.921112, 55.02813], [82.929323, 55.032846]], 'uri': 'ymapsbm1://org?oid=1062011780', 'CompanyMetaData': {'id': '1062011780', 'name': 'Новосибирский театр оперы и балета', 'address': 'Новосибирск, Красный проспект, 36', 'url': 'http://novat.ru/', 'Phones': [{'type': 'phone', 'formatted': '+7 (383) 222-04-01'}, {'type': 'phone', 'formatted': '+7 (383) 222-37-90'}, {'type': 'phone', 'formatted': '+7 (383) 222-60-40'}, {'type': 'phone', 'formatted': '+7 (383) 222-32-50'}], 'Categories': [{'class': 'theatre', 'name': 'Театр'}, {'class': 'landmark', 'name': 'Достопримечательность'}, {'class': 'concert hall', 'name': 'Концертный зал'}], 'Hours': {'text': 'ежедневно, 10:00–21:00', 'Availabilities': [{'Intervals': [{'from': '10:00:00', 'to': '21:00:00'}], 'Everyday': True}]}}}}