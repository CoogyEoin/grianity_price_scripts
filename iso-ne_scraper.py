import requests
import logging
from bs4 import BeautifulSoup

def main():
    try:
        URL = 'https://www.iso-ne.com/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        td_element = soup.find('td', class_ ='homepage-price')
        lpm_text = td_element.text
        lpm_value = lpm_text[1:]
        print(lpm_value)


    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
