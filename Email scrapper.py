import requests
import re

def get_emails_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
        return list(set(emails))
    except:
        return []

def crawl_for_emails(start_url):
    collected_emails = []
    urls_to_visit = [start_url, start_url + "/contact", start_url + "/about"]
    for url in urls_to_visit:
        collected_emails.extend(get_emails_from_url(url))
    return list(set(collected_emails))

url = "http://testphp.vulnweb.com"
emails = crawl_for_emails(url)
print(f"Найдено {len(emails)} email'ов:")
for email in emails:
    print(email)
