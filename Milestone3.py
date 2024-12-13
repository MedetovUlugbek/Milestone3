# This function assigns a name for player and initializes global variables
def playerInfo():
    global playerName
    global playerClass
    global playerName
    global playerClass
    global playerStrength
    global playerSpeed
    global playerDefense
    playerName = "N/a"
    playerClass = "N/a"
    playerStrength = 1
    playerSpeed = 1
    playerDefense = 1

# This function assigns a name for player
def playerNameAssignment():
    global playerName
    hunterManagerNPC = "Alice"
    print(hunterManagerNPC, ": Hello, Traveller. Are you here to get a Hunter's License? Y/N")
    answer = input()
    if answer.upper() == "Y":
        print("What is the name you would like to be registered under?")
        playerName = input()
        print(f"It is nice to meet you, {playerName}! Wish you all the best in your Hunter's Career.")
    else:
        print("Have a good day!")

# This function allows player to choose a class
def playerClassSelection():
    global playerClass
    classSelectionNPC = "Leo"
    print(f"{classSelectionNPC}: Hello, {playerName}. Are you here to choose a Class? Y/N")
    answer = input()
    if playerClass == "N/a" and answer.upper() == "Y":
        print("Choose which one suits the best: Fighter, Tank, Mage, Assassin, Support")
        classOptions = ["Fighter", "Tank", "Mage", "Assassin", "Support"]
        while True:
            answer = input()
            if answer in classOptions:
                playerClass = answer
                print(f"From now on, you will be taking a role of {playerClass}")
                break
            else:
                print("Please choose one of the available classes: Fighter, Tank, Mage, Assasin, Support")
    else:
        print("Looks like you already have a class:", playerClass)

def playerPowerIncreaseItems():
    global playerStrength, playerSpeed, playerDefense
    crystalConvertionNPC = "Aaron"
    while True:
        print(crystalConvertionNPC, ": Would you like to use any of your Crystals? Y/N")
        answer = input()
        if answer.upper() == "Y":
            print("How many Crystals would you like to use?")
            numberOfCrystals = int(input())
            print("What type of crystals would you like to use? (Red/Yellow/Brown)")
            typeOfCrystals = input()
            if typeOfCrystals.upper() == "RED":
                playerStrength = playerStrength + numberOfCrystals
                print(f"Your Strength increased to {playerStrength}")
            elif typeOfCrystals.upper() == "YELLOW":
                playerSpeed = playerSpeed + numberOfCrystals
                print(f"Your Speed increased to {playerSpeed}")
            elif typeOfCrystals.upper() == "BROWN":
                playerDefense = playerDefense + numberOfCrystals
                print(f"Your Defense increased to {playerDefense}")
            else:
                print("Please choose one of the available Crystals. (Red/Yellow/Brown)")
        elif answer.upper() == "N":
            print("Come again when you have more Crystals")
            break
        else:
            print("Choose either Y or N")

def playerProfile():
    print("Name:", playerName)
    print("Class:", playerClass)
    print("Strength:", playerStrength)
    print("Speed:", playerSpeed)
    print("Defense:", playerDefense)

playerInfo()

playerNameAssignment()

playerClassSelection()

playerPowerIncreaseItems()

playerProfile()