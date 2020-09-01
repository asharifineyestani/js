from bs4 import BeautifulSoup
import requests
import json

import os
from urllib.parse import urlparse

url = 'http://ny-idf-projections.nrcc.cornell.edu/Prob_Table_Data/'
ext = 'json'


def list_files(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


for file in list_files(url, ext):
    data = requests.get(file).json()
    with open('files/' + os.path.basename(urlparse(file).path), 'w') as f:
        json.dump(data, f)