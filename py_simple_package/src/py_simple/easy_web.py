"""
easy_web is built to simplify getting information from the web.
"""
import requests
from bs4 import BeautifulSoup


def get_page_content(url: str) -> str | None:
    """
        Returns content of the website or None if an error occurs.

        Arguments:
            url (str) -- website to be parsed.
        """
    try:
        response = requests.get(url, timeout=10)
        if response.ok:
            return BeautifulSoup(response.text, 'html.parser').prettify()
        else:
            return None
    except Exception as e:
        print(f"Something went wrong with {url}\nERROR: {e}")
        return None


def is_page_up(url: str) -> bool:
    """
        Returns true if HTTP status code is 200 else returns false.

        Arguments:
            url (str) -- website to check.
        """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return bool(response.status_code == 200)
    except Exception as e:
        print(f"Something went wrong with {url}\nERROR: {e}")
        return False
