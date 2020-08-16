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
    URL = 'http://oasis.caiso.com/oasisapi/prc_hub_lmp/PRC_HUB_LMP.html'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    lmp_values=[]
    lmp_dict = {}
    for i in soup.find_all('tr', class_='datarow'):
        for j in i.findChildren('td'):
            #Removes the rediculous whitespace in CAISO webpage
            breadcrum = "".join(line.strip() for line in j.text.split("\n"))
            lmp_values.append(breadcrum)

    lmp_value = lmp_values[1]
    
    #Returns lmp_value without the first character ( $ )
    return lmp_value[1:]
    
    
def put_item(lmp_value, time_stamp, region):
    client = boto3.client('dynamodb', region_name=os.environ['aws_region'])
    return client.put_item(
            TableName=os.environ['table_name'],
            Item={
                'price': { "S": lmp_value},
                'region_name': { "S": region},
                'timestamp': { "S": time_stamp}
            }
            )
    

def lambda_handler(event, context):

    client = boto3.client('dynamodb', region_name=os.environ['aws_region'])
    
    try:
        lmp_value = get_value()
        time_stamp = get_timestamp()
        response = put_item(lmp_value, time_stamp, "caiso")
        
        return response

    except Exception as e:
        raise e
