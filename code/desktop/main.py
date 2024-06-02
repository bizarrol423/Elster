import func
import pandas as pd


if __name__ == '__main__':
    SearchedOrganization = "театры Новосибирск"
    GetedData = func.get_info(SearchedOrganization)
    name = []
    address = []
    url = []
    phone = []
    coordinates = []
    hour = []
    for features in GetedData['features']:
        name.append(features['properties']['name'])
        print(features['properties']['name'], end=' ')
        address.append(features['properties']['CompanyMetaData']['address'])
        print(features['properties']['CompanyMetaData']['address'], end=' ')
        url.append(features['properties']['CompanyMetaData'].get('url','none'))
        print(features['properties']['CompanyMetaData'].get('url','none'), end=' ')
        phones = features['properties']['CompanyMetaData'].get('Phones')
        phone.append(' ')
        if (phones != None):
            phone[len(phone)-1] = phones[0]['formatted']; 
            print(phones[0]['formatted'], end=' ')
        #for phone in features['properties']['CompanyMetaData'].get('Phones'):
        #    print(phone['formatted'], end=' ')
        coordinates.append(features['geometry']['coordinates'])
        print(features['geometry']['coordinates'], end=' ')
        hours = features['properties']['CompanyMetaData'].get('Hours')#['text'], end=' ')
        hour.append('')
        if (hours != None):
            hour[len(hour)-1] = hours.get('text')
            print(hours.get('text'), end = ' ')
        for i in features['properties']['CompanyMetaData']['Categories']:
            print(i['name'], end=' ')
        print()
    print(len(name))
    print(len(address))
    print(len(url))
    print(len(phone))
    print(len(coordinates))
    print(len(hour))
    df = pd.DataFrame({
        'name': name,
        'address':  address,
        'url':url,
        'phone': phone,
        'coordinates': coordinates,
        'hour':hour
    })
    df.to_excel('./teams.xlsx')
#{'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [82.924504, 55.030439]}, 'properties': {'name': 'Новосибирский театр оперы и балета', 'description': 'Красный просп., 36, Новосибирск, Россия', 'boundedBy': [[82.921112, 55.02813], [82.929323, 55.032846]], 'uri': 'ymapsbm1://org?oid=1062011780', 'CompanyMetaData': {'id': '1062011780', 'name': 'Новосибирский театр оперы и балета', 'address': 'Новосибирск, Красный проспект, 36', 'url': 'http://novat.ru/', 'Phones': [{'type': 'phone', 'formatted': '+7 (383) 222-04-01'}, {'type': 'phone', 'formatted': '+7 (383) 222-37-90'}, {'type': 'phone', 'formatted': '+7 (383) 222-60-40'}, {'type': 'phone', 'formatted': '+7 (383) 222-32-50'}], 'Categories': [{'class': 'theatre', 'name': 'Театр'}, {'class': 'landmark', 'name': 'Достопримечательность'}, {'class': 'concert hall', 'name': 'Концертный зал'}], 'Hours': {'text': 'ежедневно, 10:00–21:00', 'Availabilities': [{'Intervals': [{'from': '10:00:00', 'to': '21:00:00'}], 'Everyday': True}]}}}}