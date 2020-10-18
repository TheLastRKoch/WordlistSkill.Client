from menu import Menu



def run_cli():
    #currentEnviroment = "Development"
    
    
    myMenu = Menu()
    myMenu.ShowInitialMenu()
    myMenu.ShowNumberOfWords(14)
    myMenu.ShowMainMenu()

if __name__ == '__main__':
    run_cli()