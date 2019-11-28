"""
Script to generate json file with Chinese cities
Source: https://en.wikipedia.org/wiki/List_of_cities_in_China
"""
import hashlib
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

WIKI_LINK = "https://en.wikipedia.org/wiki/List_of_cities_in_China"
SOURCE_SHA256 = "98c2e1577506577aee304c4b71fc8729d6bfb8c5e2acb6142ef2ef2a7543d715"
CSV_FILE = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__),
                                         '..', 'china_cities', 'cities.csv'))

def generate():
    """ function to verify wikipedia changes and update csv file """
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get(WIKI_LINK)
    assert "List of cities in China - Wikipedia" in driver.title

    city_table = driver.find_element_by_xpath('//table[@id="cities"]')
    source_hash = hashlib.sha256(bytes(city_table.get_attribute('outerHTML'), 'utf-8')).hexdigest()

    if source_hash == SOURCE_SHA256:
        print("The wikipedia information did not change")
    else:   
        print("The wikipedia information changed, generating new csv file")
        city_columns = city_table.find_elements_by_xpath('.//tbody/tr')

        file = open(CSV_FILE, "w")
        for city_column in city_columns:
            name_en = city_column.find_element_by_xpath('(.//td)[1]').text
            name_cn = city_column.find_element_by_xpath('(.//td)[2]').text
            if "特别行政区" in name_cn:
                name_cn = name_cn.replace("特别行政区", "")
            province = city_column.find_element_by_xpath('(.//td)[3]').text
            if province in ["autonomous", "municipal"]:
                province = name_en
            file.write("{},{},{}\n".format(name_en, name_cn, province))

        file.close()

    driver.close()

if __name__ == "__main__":
    generate()
