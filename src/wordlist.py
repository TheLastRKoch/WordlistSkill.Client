import requests

class WordList:
    def Request(self, controller, word):
        url = "https://wordlistskill.herokuapp.com/index.php/Wordlist/"+controller+"/"+word
       
        headers = {
            'Content-Type': 'application/json'
        }

        response = request("GET", url, headers=headers)

        pretty_json = json.loads(response.text)
        print(json.dumps(pretty_json, indent=2)+"\n")

    def GetExample(self, word):
        self.Request("Example", word)

    def AddNewWord(self, word):
        self.Request("Add", word)

    def RemoveWord(self, word):
        self.Request("Remove", word)