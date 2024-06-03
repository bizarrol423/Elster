import func
import pandas as pd


if __name__ == '__main__':
    SearchedOrganization = "Театры Новосибирск"
    X = 55.036984
    Y = 82.930311
    distance = 2.5
    data = func.get_dict(SearchedOrganization=SearchedOrganization,X=X,Y=Y,distance=distance)
    func.data_to_excel(data)
    func.data_to_csv(data)