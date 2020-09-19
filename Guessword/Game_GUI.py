"#--------Palash Roy--------#"

from Game_Logic import Game
from appJar import gui
import random


app = gui("Word Game", "350x250") # Window background with dimenssion
app.startLabelFrame("Graphical interface Guess Game") # add a label frame
app.setBg("Darkkhaki", override=False, tint=True)
app.stopLabelFrame()

word3 = ""
p1_word = ""

game = None

def gui_create(button):
    global word3, p1_word
#Player Vs computer : PVC    
    if(button == "PVC"): #“If the values of two operands are equal, then the condition becomes true”.
        global game
        game = Game()
        game.set_game_type(Game.PVC) #import the functionality and condition from Game_ligic program file
        app.startSubWindow("One", modal=True)
        #app.addLabel("l1", "Player Vs. Computer")
        app.label("Player Vs. Computer", bg= "Darkkhaki")
        app.setBg("Darkkhaki", override=False, tint=True)
        app.setFont(14)


    # Getting all the words from file and selecting one
        word = game.set_guess_word()   #import the functionality and condition from Game_ligic program file       
        app.addMessage("info", "The word is of length : " + str(len(word)))

    # Getting word input

        app.addLabelEntry("wordGuess")
        app.addButton("Continue", word_checking)
        launch("One")
        app.stopSubWindow()

    # Player Vs Player: PVP        
    elif(button == "PVP"): #“If the values of two operands are equal, then the condition becomes true”.
        #global game
        game = Game()
        game.set_game_type(Game.PVP) #import the functionality and condition from Game_ligic program file
        app.startSubWindow("Two")
        #app.addLabel("l2", "player Vs. Player")
        #app.setLabelBg("12","red")
        app.label("Player Vs Player", bg= "Darkkhaki")
        app.setBg("Darkkhaki", override=False, tint=True) 
        app.setFont(14)
        
        # First player will guess a secret word that should be invisible 
        app.addLabelSecretEntry("1st Word") 
        app.addButton("Continue", player_word_checking)
        launch("Two")
        app.stopSubWindow()


def launch(win):
    app.showSubWindow(win)

# for cumputer
def word_checking():
    usr = app.getEntry("wordGuess")
    usr = usr.lower()

    ans = game.guess_attempt(usr)
    app.infoBox("answer", ans, parent="One")  
    if ans.startswith("Congrats") or ans.startswith("Game over"):
        app.destroySubWindow("One")

def player_word_checking():
    
    global p1_word
    p1_word = app.getEntry("1st Word")
    word = game.set_guess_word(p1_word) #import the functionality and condition from Game_ligic program file
    
    if(word != False): #Checks if the value of two operands are equal, if values are not equal than the condition becomes true.
        app.destroySubWindow("Two")
        app.startSubWindow("three")

        #app.addLabel("l3", "player2 input", bg="red")
        app.label("player2 input", bg="Darkkhaki")
        app.setBg("Darkkhaki", override=False, tint=True)
        
        app.setFont(14) 
        app.addMessage("info", "Player 1 word is of length : " + str(len(word)))
        app.addLabelEntry("Player 2 Guess")
        #Player 2 will guess the word what player 1 gussed
        app.addButton("Continue", pvp_word_checking)

        launch("three")
    else:
        app.infoBox("Word availability","Sorry, this word is not in the file", parent="Two")



# this takes Player 2 input and checks against Player 1 input
def pvp_word_checking():
    second_word = app.getEntry("Player 2 Guess")

    second_word = second_word.lower()
    ans = game.guess_attempt(second_word) # "guess_attempt & second_word" import the functionality and condition from Game_ligic program file
    app.infoBox("answer", ans, parent="three") 
    if ans.startswith("Congrats") or ans.startswith("The Game Is Over"):
        app.destroySubWindow("three")

def Main_menu():
#   gui_create(1)       
    app.setBg("Darkkhaki", override=False, tint=True) 
    app.setFont(14)

    app.addFlashLabel("title", "Please select your game mode")
    app.addButtons(["PVP" , "PVC"], gui_create) # you can choose the game mode 
    app.addButtons(["Cancel"],[app.stop]) #It will help you to close the window
    app.go()
    #NOTE: PVP: Player vs Player and PVC: Plater vas player

#calling GUI main function to run the program
Main_menu()


# checking if user 1 word is in file or not
#def word_check(p2_word):
    
#    #Getting all the words from file
##    word = open("words.txt","r")
#   word_array = []
#    for i in word:
#        word_array.append(i.strip('\n'))
    
#    available = False
#    for j in range(0 , len(word_array)):
#        if(p2_word == word_array[j]):
#            available = True
#            break
#    return available



