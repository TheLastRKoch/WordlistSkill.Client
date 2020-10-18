import os

class Menu:

    def __init__(self):
        pass

    def ShowInitialMenu(self):
        os.system("cls")
        print("================================")
        print(" Welcome to the WordList Skill")
        print("================================")
        print("\n")

    def ShowNumberOfWords(self,numberOfWords):
        print("Actually the system store "+str(numberOfWords)+" words")
        print("\n")

    def ShowMainMenu(self):
        print("Please select the option to perform")
        return input("a) Play trivia \nb) See a word example \nc) Save a new word \nd) Remove a word from the list\n")

    def SearchMenu(self):
        os.system("cls")
        print ("Searching....\n")

    def Continue(self, title):
        return input("Do you want to "+title+"? (y/n)")
