import requests
import os
import requests
import json

class WordList:
    def GetExample(self, input):
        url = "https://prod-163.westeurope.logic.azure.com:443/workflows/1e0b733b82f648ce9de01cefa4dac97d/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=04Wo1YTWPi2KZfi-iMN2fq_-i_Lhb3SWBGaagiVr_08"

        payload = "{\"SearchItem\":\""+input+"\"}"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        os.system("cls")
        print ("Found: \n")
        pretty_json = json.loads(response.text)
        print (json.dumps(pretty_json, indent=2))