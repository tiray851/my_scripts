import requests

url = "http://scanme.nmap.org"
robots_url = url + "/robots.txt"

response = requests.get(robots_url)

if response.status_code == 200:
    print("robots.txt найден! Содержимое:")
    print(response.text)
else:
    print("robots.txt не найден (код", response.status_code, ")")
