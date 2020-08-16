import requests
import logging
from bs4 import BeautifulSoup

lmp_dict = {
   "DPL":"",
   "COMED":"",
   "AEP":"",
   "EKPC":"",
   "PEP":"",
   "JC":"",
   "PL":"",
   "DOM":""
}

def main():
    try:
        URL = 'https://www.pjm.com/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        """
        There are multiple tables of class 'lmp-price-table'. This
        loop goes through all the divs in the tables containing the RSO name 
        and the LMP and if the key exists in the dictionary (Keys are the RSO 
        name) then it stores the next divs text as the value
        """
        for i in soup.find_all('ul', class_='lmp-price-table'):
            divs = i.findChildren('div')
            j=0
            while j < len(divs):
                value = divs[j].text
                if value in lmp_dict:
                    lmp_dict[value] = divs[j+1].text
                j+=1
            
        print(lmp_dict)


    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
