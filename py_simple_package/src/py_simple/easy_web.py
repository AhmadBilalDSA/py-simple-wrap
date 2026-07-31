"""
easy_web is built to simplify getting information from the web.
"""
import requests
from bs4 import BeautifulSoup


def get_page_content(url: str) -> str | None:
    """
    Returns content of the website or None if an error occurs.

    Args:
        url (str): Website to be parsed.

    Returns:
        str | None: The page's prettified HTML content, or None if the
            request failed.

    Example:
        get_page_content("https://example.com")
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

    Args:
        url (str): Website to check.

    Returns:
        bool: True if the site responded with status 200, False otherwise.

    Example:
        is_page_up("https://example.com")
        (True)
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return bool(response.status_code == 200)
    except Exception as e:
        print(f"Something went wrong with {url}\nERROR: {e}")
        return False
