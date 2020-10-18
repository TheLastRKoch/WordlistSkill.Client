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
        os.system("cls")
        myMenu.ShowTitle("Get Example")
        wordToSearch = myMenu.RequestWord()
        myMenu.SearchMenu()
        os.system("cls")
        API.GetExample(wordToSearch)
        continueResp = myMenu.Continue("search another example")
        if continueResp == "n" or continueResp == "N":
            doContinue = False


def AddWord():
    doContinue = True
    myMenu = Menu()
    API = WordList()
    while doContinue:
        os.system("cls")
        myMenu.ShowTitle("Add a new word")
        wordToSearch = myMenu.RequestWord()
        myMenu.SearchMenu()
        os.system("cls")
        API.AddNewWord(wordToSearch)
        continueResp = myMenu.Continue("add another word")
        if continueResp == "n" or continueResp == "N":
            doContinue = False


def RemoveWord():
    doContinue = True
    myMenu = Menu()
    API = WordList()
    while doContinue:
        os.system("cls")
        myMenu.ShowTitle("Remove word")
        wordToSearch = myMenu.RequestWord()
        myMenu.SearchMenu()
        os.system("cls")
        API.RemoveWord(wordToSearch)
        continueResp = myMenu.Continue("remove another word")
        if continueResp == "n" or continueResp == "N":
            doContinue = False


def run_cli():
    # currentEnvironment = "Development"
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
        continueResp = myMenu.Continue("perform another action")
        if continueResp == "n" or continueResp == "N":
            doContinue = False


if __name__ == '__main__':
    run_cli()
