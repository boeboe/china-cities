# china_cities

## Introduction

`china_cities` is a python package to list Chinese cities and provinces. The cities 
can be retrieved in English or Chinese language.

The data is based on [`wikipedia`](https://en.wikipedia.org/wiki/List_of_cities_in_China) as a source

## Installation

### Install with pip

Run `pip install china-cities`

### Install from source

`git clone https://github.com/boeboe/china-cities.git`

Run `python setup.py install`

### Run tests

Run `make tests`

### Update source when wikipedia changed

Run `make generate`

## Usage

Some examples on how to use this package.

```python
from china_cities import *

for city in cities.get_cities():
    print("english name:", city.name_en)
    print("chinese name:", city.name_cn)
    print("province:    ", city.province)

for city_en in cities.get_cities_en():
    print(city_en)

for city_cn in cities.get_cities_cn():
    print(city_cn)

for province in cities.get_provinces():
    print(province)

for province_city in cities.get_cities_by_province("Anhui"):
    print(province_city.name_en)

```
