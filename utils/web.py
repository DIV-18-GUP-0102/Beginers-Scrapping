# web.py
import requests
from bs4 import BeautifulSoup

def parse_html(url):
    response = requests.get(url)
    return response.text

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    title_classes = ['entry-title', 'tdb-title-text']
    title = None
    for title_class in title_classes:
        title_element = soup.find('h1', class_=title_class)
        if title_element:
            title = title_element.get_text()
            break

    post_content_div = soup.find('div', class_='td-post-content tagdiv-type')

    if not post_content_div:
        post_content_div = soup.find('div', class_='tdb-block-inner td-fix-index')

    if post_content_div:
        content = post_content_div.get_text(separator='\n', strip=True)
        return title, content
    else:
        return None, None

