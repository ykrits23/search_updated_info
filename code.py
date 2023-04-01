import requests
from bs4 import BeautifulSoup

link_company = "https://youcontrol.com.ua/catalog/company_details/19358784/"
link_fop = "https://youcontrol.com.ua/catalog/fop_details/65370967/"

headers = {"sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
           "sec-ch-ua-mobile": "?0",
           "sec-ch-ua-platform": "Windows",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
           }
responce = requests.get(link_company, headers=headers).text

soup = BeautifulSoup(responce, 'lxml')

block = soup.find('div', id='catalog-company-fees')

mydivs = block.find_all("div", {"class": "seo-table-col-2"})[0].text.strip()



# myclass = mydivs.find("div").text

print(mydivs)