"#--------Palash Roy--------#"

import random

Chances = 7
def choosing_word(): # This function chooses a word randomly from the file
                     # Reading words from file "words.txt"
    word_list = [i.strip() for i in open("words.txt", "r").readlines()]
    #saving length of list of words from file
    Word_length = len(word_list)

    random_index = random.randint(0,Word_length)
    #saving the randomly chosen word
    comp_word = word_list[random_index]
    
    return comp_word

def Player(comp_word):
    #global variable
    global Chances

    comp_word = comp_word.lower()
    print("............................................................................")
    print("#                       START YOUR GUESS GAME                              #")
    print("............................................................................")
    print()
    ans = False
    while(Chances > 0):
        print("The chosen word is of length {}".format(len(comp_word)))

        print("you have {} chances left".format(Chances))

        guess = input("Please enter your guessed word .... ")

        guess = str(guess)
        guess = guess.lower()
        #same word
        if(guess == comp_word):
            print("............................................................................")
            print("#              Congrats you guess the right word                           #")
            print("............................................................................")
            ans = True
            break

        #not same word but same length
        elif((guess != comp_word) and (len(guess) == len(comp_word))):
            Chances -= 1
            print("sorry you didn't guesss the right word")
            correct_indexes = ""
            #getting the postion number of correctly placed alphabets
            for i in range(0 , len(guess)):
                if(guess[i] == comp_word[i]):
                    correct_indexes += str(i + 1) + " "
                
            if(len(correct_indexes) == 0):
                correct_indexes = "None"
            
            correct_alphabets = ""
            for i in range(0, len(guess)):
                for j in range(0, len(comp_word)):
                    if(guess[i] == comp_word[j]):
                        correct_alphabets += guess[i] + " "
                        break
            
            print("The alphabets at the right position are {}".format(correct_indexes))
            print()
            print("The alphabets that are in your guess and also in the actual word are : {}".format(correct_alphabets))
            print()
            print("you have {} chances left".format(Chances))
        #Guessed word bigger than the actual word
        elif(len(guess) > len(comp_word)):
            Chances -= 1
            print("sorry your guessed word is bigger than the actual word")
            correct_indexes = ""
            #getting the postion number of correctly placed alphabets
            for i in range(0 , len(comp_word)):
                if(guess[i] == comp_word[i]):
                    correct_indexes += str(i + 1) + " "
                
            if(len(correct_indexes) == 0):
                correct_indexes = "None"
            

            correct_alphabets = ""
            for i in range(0, len(guess)):
                for j in range(0, len(comp_word)):
                    if(guess[i] == comp_word[j]):
                        correct_alphabets += guess[i] + " "
                        break
            
            print("The alphabets at the right position are {}".format(correct_indexes))
            print()
            print("The alphabets that are in your guess and also in the actual word are : {}".format(correct_alphabets))
            print()
            print("you have {} chances left".format(Chances))
        #Guessed word smaller than the actual word
        elif(len(guess) < len(comp_word)):
            Chances -= 1
            print("sorry your guessed word is smaller than the actual word")
            correct_indexes = ""
            #getting the postion number of correctly placed alphabets
            for i in range(0 , len(guess)):
                if(guess[i] == comp_word[i]):
                    correct_indexes += str(i + 1) + " "
                
            if(len(correct_indexes) == 0):
                correct_indexes = "None"

            correct_alphabets = ""
            for i in range(0, len(guess)):
                for j in range(0, len(comp_word)):
                    if(guess[i] == comp_word[j]):
                        correct_alphabets += guess[i] + " "
                        break
            
            print("The alphabets at the right position are {}".format(correct_indexes))
            print()
            print("The alphabets that are in your guess and also in the actual word are : {}".format(correct_alphabets))
            print()
            print("you have {} chances left".format(Chances))
    return ans


def main():
    comp_word = choosing_word()

    ans = Player(comp_word)
    if(ans == True): 
        print(" You won the game, thanks for playing ")
    elif(ans == False):
        print("............................................................................")
        print("#                   Your Guess is not correct                              #")
        print("............................................................................")
        print("The actual word was:   {}".format(comp_word))

#calling main function
main()