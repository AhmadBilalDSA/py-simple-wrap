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
        === "The Py_simple Way"
        ```python
        from py_simple import get_page_content
        content = get_page_content("https://google.com")
        ```

        === "The Traditional Way"
        ```python
        import requests
        from bs4 import BeautifulSoup

        response = requests.get("https://google.com")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.prettify()
        ```
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
        === "The Py_simple Way"
        ```python
        from py_simple import is_page_up

        if is_page_up("https://github.com"):
            print("The site is active!")
        ```

        === "The Traditional Way"
            ```python
            import requests

            try:
                response = requests.get("https://github.com")
                if response.status_code == 200:
                    print("The site is active!")
            except Exception:
                print("The site is down or address is invalid.")
            ```
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return bool(response.status_code == 200)
    except Exception as e:
        print(f"Something went wrong with {url}\nERROR: {e}")
        return False
