#Examples
import requests
from bs4 import BeautifulSoup
url = 'http://cricinfo.com/datasets.html'

response = requests.get(url)
status = response.status_code
print(status)

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)

#Exercises
import requests
from bs4 import BeautifulSoup
url = 'http://cricinfo.com/datasets.html'

response = requests.get(url)
status = response.status_code
print(status)

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)
