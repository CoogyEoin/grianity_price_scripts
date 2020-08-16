import json
import boto3
import os
import requests
from datetime import datetime, timedelta
import logging
from bs4 import BeautifulSoup



def get_timestamp():
    # current date and time
    now = datetime.now()
    
    # Convert the hour from UST to EST using environment value 'time_addition'
    hour_value = int(os.environ['time_addition'])
    now += timedelta(hours=hour_value)
   
    return now.strftime ('%Y%m%d%H%M') 
    
    
def get_value():
    URL = 'https://www.iso-ne.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    td_element = soup.find('td', class_ ='homepage-price')
    lpm_text = td_element.text
    return lpm_text[1:]
    

def lambda_handler(event, context):
    """
    client = boto3.client('dynamodb', region_name=os.environ['aws_region'])
    
    time_stamp = get_timestamp()
    url = 'https://hourlypricing.comed.com/api?type=5minutefeed&datestart=' + time_stamp +'&dateend=' + time_stamp;
    print('URL: ' + url)
    response = requests.get(url)
	
    json_response = response.json()[0]
    price = json_response['price']
    
    dynamodbresponse = client.put_item(
            TableName=os.environ['table_name'],
            Item={
                'price': { "S": price},
                'timestamp': { "S": time_stamp}
            }
            )
    return dynamodbresponse
    """
    client = boto3.client('dynamodb', region_name=os.environ['aws_region'])
    region = "iso-ne"
    
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

