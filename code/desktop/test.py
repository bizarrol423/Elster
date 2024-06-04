import ELSTER
import pandas as pd


if __name__ == '__main__':
    SearchedOrganization = "Театры Новосибирск"
    X = 55.036984
    Y = 82.930311
    distance = 2500
    data = ELSTER.get_dict(SearchedOrganization=SearchedOrganization,X=X,Y=Y,distance=distance)
    ELSTER.data_to_excel(data)
    ELSTER.data_to_csv(data)