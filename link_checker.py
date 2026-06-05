import requests
import re
from urllib.parse import urljoin

url = "http://scanme.nmap.org"
response = requests.get(url)
links = re.findall(r'href="([^"]*)"', response.text)

for link in links:
    # Превращаем относительную ссылку в абсолютную
    full_link = urljoin(url, link)
    try:
        res = requests.get(full_link, timeout=2)
        if res.status_code == 200:
            print(f"✅ Рабочая ссылка: {full_link}")
        else:
            print(f"❌ Не работает: {full_link} (код {res.status_code})")
    except:
        print(f"❌ Ошибка: {full_link}")

