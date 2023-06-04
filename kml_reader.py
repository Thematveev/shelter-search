from fastkml import kml
import re
from database import Shelter


def load_shelters():
    file = open('kyiv.kml')
    k = kml.KML()
    k.from_string(file.read())
    file.close()

    main_features = next(k.features())
    places = []
    for i in main_features.features():
        for n in i.features():
            places.append(n)

    shelters = [] 
    for i in places:
        info = {}
        print(i.to_string())
        match = re.search(r"<kml:coordinates>[0-9\.,]+<\/kml:coordinates>", i.to_string())
        if match:
            data = match.group().removeprefix('<kml:coordinates>').removesuffix('</kml:coordinates>').split(',')[:2]
            info['coordinates'] = list(map(float, data))
        match = re.search(r"<kml:name>.+</kml:name>", i.to_string())
        if match:
            data = match.group().removeprefix('<kml:name>').removesuffix('</kml:name>')
            info['street'] = data
        shelters.append(info)

    return shelters

if __name__ == "__main__":
    s = load_shelters()
    for i in s:
        Shelter.create(
            street=i['street'],
            lat = i['coordinates'][1],
            lon = i['coordinates'][0],
            city="Kyiv"
        )

    # print(list(Shelter.select()))

    
