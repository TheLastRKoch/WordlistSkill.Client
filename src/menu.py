import os

class Menu:

    def __init__(self):
        pass

    def ShowInitialMenu(self):
        os.system("cls")
        print("=============================================\n")
        print("        Welcome to the WordList Skill\n")
        print("=============================================")
        print("\n")

    def ShowNumberOfWords(self,numberOfWords):
        print("Actually the system store "+str(numberOfWords)+" words")
        print("\n")

    def ShowMainMenu(self):
        print("Please select the option to perform")
        result = input("1) Play trivia \n2) See a word example \n3) Save a new word \n4) Remove a word from the list\n:")
        os.system("cls")
        print(result+" selected\n")
        return result

    def RequestWord(self):
        return input("Please type a word to continue\n:")

    def SearchMenu(self):
        os.system("cls")
        print("Searching....\n")

    def ShowTitle(self, title):
        print("=============================================\n")
        print("        "+title+"\n")
        print("=============================================")

    def Continue(self, title):
        return input("Do you want to "+title+"? (y/n):")
