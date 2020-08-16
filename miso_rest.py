import requests
import logging
import json

#Dictionary containing the values needed
lmp_dict = {
   "AECI":"",
   "ARKANSAS.HUB":"",
   "MHEB":"",
   "LOUISIANA.HUB":"",
   "MICHIGAN.HUB":"",
   "TEXAS.HUB":"",
   "ILLINOIS.HUB":"",
   "INDIANA.HUB":"",
   "MINN.HUB":"",
   "OTP.MPC":"",
   "CONS.CAMPBELL1":"",
   "TVA":"",
   "DUK":"",
   "SOCO":"",
   "CSWS":"",
   "WAUE":"",
   "KCPL":"",
   "NYISO":"",
   "ONT":"",
   "MS.HUB":"",
   "NPPD":"",
   "MEC.MECB":"",
   "SPC":""
}

def main():
    try:
        URL = 'https://api.misoenergy.org/MISORTWDDataBroker/DataBrokerServices.asmx?messageType=getlmpconsolidatedtable&returnType=json'
        response = requests.get(URL)
        json_response = json.loads(response.text)
        for i in json_response['LMPData']['FiveMinLMP']['PricingNode']:
            name = i['name']
            if name in lmp_dict:
                lmp_dict[name] = i['LMP']
        
        print(lmp_dict)

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
