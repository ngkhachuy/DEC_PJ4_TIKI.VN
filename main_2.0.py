import datetime
import os

import urllib3
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

import COMMON
from MODELS.CATEGORY import CATEGORY

if __name__ == '__main__':

    START_TIME = datetime.datetime.now()
    ROOT_URL = 'https://tiki.vn/'
    categories = []

    browser = webdriver.Chrome()
    browser.get(ROOT_URL)
    root_page_context = BeautifulSoup(browser.page_source, 'lxml')
    highlight_div = root_page_context.find_all('div', class_=['styles__StyledListItem-sc-w7gnxl-0'])[1]
    root_categories = highlight_div.find_all('a', class_=['styles__StyledItem-sc-oho8ay-0 bzmzGe'])

    for cat in root_categories:
        cat_url = cat.attrs['href']
        cat_name = cat.attrs['title']
        _id = cat_url.split("/")[-1]

        if _id == 'c44792':
            category = CATEGORY(_id, 'NGON', 1, cat_url, None)
            categories.append(category)
            continue

        category = CATEGORY(_id, cat_name.strip(), 1, cat_url, None)
        categories.append(category)

    print(categories)
    COMMON.print_execution_time(START_TIME)