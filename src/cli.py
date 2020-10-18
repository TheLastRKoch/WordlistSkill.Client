import os
from menu import Menu
from wordlist import WordList

def Trivia():
    print("Coming soon....")

def GetExample():
    doContinue = True
    myMenu = Menu()
    API = WordList()
    while doContinue:
        wordToSearch = myMenu.RequestWord()
        myMenu.SearchMenu()
        os.system("cls")
        API.GetExample(wordToSearch)
        if myMenu.Continue("search another example") == "n" or myMenu.Continue("search another example") == "N":
            doContinue = False
    

def AddWord():
    doContinue = True
    myMenu = Menu()
    API = WordList()
    while doContinue:
        wordToSearch = myMenu.RequestWord()
        myMenu.SearchMenu()
        os.system("cls")
        API.AddNewWord(wordToSearch)
        if myMenu.Continue("add another word") == "n" or myMenu.Continue("add another word") == "N":
            doContinue = False

def RemoveWord():
    doContinue = True
    myMenu = Menu()
    API = WordList()
    while doContinue:
        wordToSearch = myMenu.RequestWord()
        myMenu.SearchMenu()
        os.system("cls")
        API.RemoveWord(wordToSearch)
        if myMenu.Continue("remove another word") == "n" or myMenu.Continue("remove another word") == "N":
            doContinue = False

def run_cli():
    #currentEnviroment = "Development"
    doContinue = True    
    myMenu = Menu()
    while doContinue:
        os.system("cls")
        myMenu.ShowInitialMenu()
        myMenu.ShowNumberOfWords(14)
        resp = myMenu.ShowMainMenu()
        if resp == "1":
            Trivia()
        elif resp == "2":
            GetExample()
        elif resp == "3":
            AddWord()
        elif resp == "4":
            RemoveWord()
        if myMenu.Continue("perform another action") == "n" or myMenu.Continue("perform another action") == "N":
            doContinue = False
    
if __name__ == '__main__':
    run_cli()