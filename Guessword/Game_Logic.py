"#--------Palash Roy--------#"

import random

class Game:
    PVP = 1  # Constants: Player verses Player
    PVC = 2 # Player verses Computer
    N_CHANCES = 7
    def __init__(self):  # Its  a Constructor
        self.word_list = [i.strip() for i in open("words.txt", "r").readlines()]
        pass

    def set_game_type(self, game_type):
        # self == this # Defination
        if game_type == self.PVC or game_type == self.PVP:
            self.game_type = game_type

    def set_guess_word(self, guess_word=None):  # Default value for argument,
        
        if self.game_type == Game.PVC:
            # choose random word from word_list 
            arr_length = len(self.word_list)
            random_index = random.randint(0,arr_length)
            #using the one word
            word = self.word_list[random_index]
            self.word = word  # Save the value of original word in game class.
            return word
        elif self.game_type == Game.PVP:
            if guess_word in self.word_list:
                self.word = guess_word
                return guess_word
            else:
                return False

    def guess_attempt(self, attempt):
        second_word = attempt
        guess_array = []
        for k in second_word: #Do the same for each element in a list, dict or range
            guess_array.append(k)

        guess_length = len(guess_array)
        correct_indexes = ""
        word_array3 = []
        for m in self.word:  
            word_array3.append(m)
        word_length3 = len(word_array3)

        if(guess_length == word_length3):
            if(second_word == self.word):
                return "Congrats you guessed the right word"
            elif(second_word != self.word):
                for k in range(0 , word_length3):
                    if(guess_array[k] == word_array3[k]):
                        correct_indexes += str(k + 1) + " "
                self.N_CHANCES -= 1
                if self.N_CHANCES == 0:
                    return "Game over... You ran out of lives. Correct word was " + self.word
                if(correct_indexes == ""):
                    correct_indexes = "None"
                return "alphabets at correct indexes : " + correct_indexes +"\nChanes left: " + str(self.N_CHANCES)
        elif( guess_length > word_length3):
            
            self.N_CHANCES -= 1  
            if self.N_CHANCES == 0:
                return "Game over... You ran out of lives. Correct word was " + self.word
            return "Sorry your guessed word is bigger than the first word" + "\nChanes left: " + str(self.N_CHANCES)
        elif(guess_length < word_length3):

            self.N_CHANCES -= 1
            if self.N_CHANCES == 0:
                return "Game over... You ran out of lives. Correct word was " + self.word
            return "Sorry your guessed word is smaller than the first word" +"\nChanes left: " + str(self.N_CHANCES)
