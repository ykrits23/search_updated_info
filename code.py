import requests
from bs4 import BeautifulSoup

fop_1 = '3112321491'
company_1 = '19358784'

code_number = '3112321491'

if len(code_number) == 10:
    link_query = f"https://youcontrol.com.ua/search/?q={code_number}"
    headers = {"sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "Windows",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
               }
    responce = requests.get(link_query, headers=headers).text

    soup = BeautifulSoup(responce, 'lxml')

    block = soup.find('div', id='catalog-company-fees')

    mydivs = block.find_all("div", {"class": "seo-table-row"})[4]  # [4].text.strip()

    pdv_div = mydivs.find('div', class_='seo-table-col-2').text.strip()

    print(pdv_div)
else:
    link_query = f"https://youcontrol.com.ua/search/?q={code_number}"
    headers = {"sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "Windows",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
               }
    responce = requests.get(link_query, headers=headers).text

    soup = BeautifulSoup(responce, 'lxml')

    block = soup.find('div', id='catalog-company-fees')

    mydivs = block.find("div", {"class": "seo-table"})

    pdv_div = mydivs.find_all('div', class_='seo-table-row')[1]

    div_col_2 = pdv_div.find('div', class_='seo-table-col-2')

    div_info_group = list(div_col_2.find_all('div', class_= 'info-group')[0].text.strip().split("  "))[0]

    print(div_info_group)
