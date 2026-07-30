"""
easy_web is built to simplify getting information from the web.
"""
import requests
from bs4 import BeautifulSoup


def get_page_content(url: str):
    try:
        response = requests.get(url)
        if response.ok:
            return BeautifulSoup(response.text, 'html.parser').prettify()
        else:
            return None
    except Exception as e:
        print(f"Something went wrong with {url}\nERROR: {e}")
        return None


def is_page_up(url: str) -> bool:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return bool(response.status_code == 200)
    except Exception as e:
        print(f"Something went wrong with {url}\nERROR: {e}")
        return False


