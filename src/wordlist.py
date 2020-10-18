import json
from requests import request


class WordList:
    def HttpRequest(self, controller, word):
        url = "https://wordlistskill.herokuapp.com/index.php/Wordlist/"+controller+"/"+word
       
        headers = {
            'Content-Type': 'application/json'
        }

        response = request("GET", url, headers=headers)

        pretty_json = json.loads(response.text)
        print(json.dumps(pretty_json, indent=2)+"\n")

    def GetExample(self, word):
        self.HttpRequest("Example", word)

    def AddNewWord(self, word):
        self.HttpRequest("Add", word)

    def RemoveWord(self, word):
        self.HttpRequest("Remove", word)