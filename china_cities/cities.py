"""Package to fetch Chinese Cities"""
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class City():
    """Class to represent a Chinese City """

    def __init__(self, name_en=None, name_cn=None, province=None):
        self.name_en = name_en
        self.name_cn = name_cn
        self.province = province

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

CITIES = []

with open(os.path.join(__location__, 'cities.csv'), encoding='utf-8') as fileHandler:
    for line in fileHandler:
        split = line.strip().split(",")
        CITIES.append(City(name_en=split[0], name_cn=split[1], province=split[2]))

def get_cities():
    """Return a list of all Chinese Cities (City objects) """
    return CITIES

def get_cities_en():
    """Return a list of all Chinese Cities (english name) """
    result = []
    for city in CITIES:
        result.append(city.name_en)
    return result

def get_cities_cn():
    """Return a list of all Chinese Cities (chinese name) """
    result = []
    for city in CITIES:
        result.append(city.name_cn)
    return result

def get_cities_by_province(province):
    """Return a list of all Chinese Cities in a certain Chinese Province """
    result = []
    for city in CITIES:
        if city.province == province:
            result.append(city)
    return result

def get_provinces():
    """Return a list of all Chinese Provinces """
    result = []
    for city in CITIES:
        if not city.province in result:
            result.append(city.province)
    return result
