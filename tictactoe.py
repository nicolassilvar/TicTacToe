playGame = True
while playGame == True:

    print("Welcome to TIC TAC TOE!")
    print("By Alejandro Sardi")
    print(" ")
    line = '-----------'
    chart = {'pos1':' 1 ','pos2':' 2 ','pos3':' 3 ','pos4':' 4 ','pos5':' 5 ','pos6':' 6 ','pos7':' 7 ','pos8':' 8 ','pos9':' 9 '}
    row1 = chart['pos1'] + '|' + chart['pos2'] + '|' + chart['pos3']
    row2 = chart['pos4'] + '|' + chart['pos5'] + '|' + chart['pos6']
    row3 = chart['pos7'] + '|' + chart['pos8'] + '|' + chart['pos9']
    player1XorO = False
    while player1XorO not in ['X','O']:

        player1XorO = input('Player 1: do you want to be X or O?: ').upper()

        if player1XorO in ['X','O']:
            print('Player 1 will be: '+ str(player1XorO))
            currentTurn = player1XorO

    areYouReadyToPlay = False
    while areYouReadyToPlay not in ['YES', 'Y']: 
        areYouReadyToPlay = input('Are you ready to play? "Yes" or "No": ').upper()

    available_positions = ['1','2','3','4','5','6','7','8','9']
    gameIsOver = False

    for i in range(100):
        print("")
    print(row1)
    print(line)
    print(row2)
    print(line)
    print(row3)
    
    while gameIsOver == False:
        def askforposition(available_positions):
            choice = False
            while choice not in available_positions:
                choice = input(str(currentTurn) + "'s turn! Choose one of the following positions available: "+ (",").join(available_positions)+" : ")
                if choice in available_positions:
                    print('you chose: ' + str(choice))
                else:
                    print(str(choice) + ' is not an available position')
                    choice = False
            return choice

        choice = askforposition(available_positions)

        for index, i in enumerate(available_positions):
            if i == choice:
                available_positions.pop(index)
        
        
            
        chart['pos'+str(choice)] = ' '+currentTurn+' '
        row1 = chart['pos1'] + '|' + chart['pos2'] + '|' + chart['pos3']
        row2 = chart['pos4'] + '|' + chart['pos5'] + '|' + chart['pos6']
        row3 = chart['pos7'] + '|' + chart['pos8'] + '|' + chart['pos9']
        for i in range(100):
            print("")
        print(row1)
        print(line)
        print(row2)
        print(line)
        print(row3)

        def checkIfGameIsOver():
            if chart['pos1'] == chart['pos2'] == chart['pos3'] and (chart['pos1'] == ' X ' or chart['pos1'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos1']))
                return gameIsOver
            elif chart['pos4'] == chart['pos5'] == chart['pos6'] and (chart['pos4'] == ' X ' or chart['pos4'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos4']))
                return gameIsOver
            elif chart['pos7'] == chart['pos8'] == chart['pos9'] and (chart['pos7'] == ' X ' or chart['pos7'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos7']))
                return gameIsOver
            elif chart['pos1'] == chart['pos5'] == chart['pos9'] and (chart['pos1'] == ' X ' or chart['pos1'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos1']))
                return gameIsOver
            elif chart['pos7'] == chart['pos5'] == chart['pos3'] and (chart['pos7'] == ' X ' or chart['pos7'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos7']))
                return gameIsOver
            if chart['pos1'] == chart['pos4'] == chart['pos7'] and (chart['pos1'] == ' X ' or chart['pos1'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos1']))
                return gameIsOver
            if chart['pos2'] == chart['pos5'] == chart['pos8'] and (chart['pos2'] == ' X ' or chart['pos2'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos2']))
                return gameIsOver
            if chart['pos3'] == chart['pos6'] == chart['pos9'] and (chart['pos3'] == ' X ' or chart['pos3'] == " O "):
                gameIsOver = True
                print("The winner is "+str(chart['pos3']))
                return gameIsOver
            elif len(available_positions) == 0:
                gameIsOver = True
                print("Game ends in a tie!")
                return gameIsOver
            else:
                gameIsOver = False
                return gameIsOver
            
        if currentTurn == "X":
            currentTurn = "O"
        else:
            currentTurn = "X"
            
        gameIsOver = checkIfGameIsOver()
        
        if gameIsOver:    
            response = False
            while response not in ['YES', 'Y', "NO", "N"]: 
                response = input('Play Again? "Yes" or "No": ').upper()
            
            if response == "YES" or response == "Y":
                playGame = True
            else:
                playGame = False
