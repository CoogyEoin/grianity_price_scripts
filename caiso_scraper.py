import requests
import logging
from bs4 import BeautifulSoup

def main():
    try:
        URL = 'http://oasis.caiso.com/oasisapi/prc_hub_lmp/PRC_HUB_LMP.html'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        #soup = soup.prettify() 

        lpm_values=[]
        lpm_dict = {}
        for i in soup.find_all('tr', class_='datarow'):
            for j in i.findChildren('td'):
                #Removes the rediculous whitespace in CAISO webpage
                breadcrum = "".join(line.strip() for line in j.text.split("\n"))
                lpm_values.append(breadcrum)
                
        print(lpm_values[1])
            


    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
