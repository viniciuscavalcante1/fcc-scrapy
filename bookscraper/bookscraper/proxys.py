import warnings
warnings.filterwarnings('ignore')
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np


def proxies_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='table-striped')
    rows = table.find_all('tr')
    return rows

def other_proxies():
    url = 'https://api.proxyscrape.com/v2/?request=getproxies&timeout=1000&protocol=http&anonymity=elite'
    response = requests.get(url)
    if response.status_code == 200:
        proxies = response.text.split('\r\n')
    return proxies

def proxies():
    ip_list =  []
    ip_list_sem_duplicados =  []
    for url in ['https://free-proxy-list.net/','https://www.sslproxies.org/','https://www.us-proxy.org/','https://free-proxy-list.net/uk-proxy.html']:
        rows = proxies_request(url)
        len(rows)
        for row in rows:
            data = row.find_all('td')
            if len(data) > 0:
                ip = data[0].text
                port = data[1].text
                https = data[6].text
                if https == 'yes':
                    ip_list.append(ip + ':' + port)     
        
    [ip_list.append(x) for x in other_proxies()]

    for i in ip_list:
            if i not in ip_list_sem_duplicados:
                ip_list_sem_duplicados.append(i)
    return ip_list_sem_duplicados
