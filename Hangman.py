import random

class hangman:
    def __init__(self):
        secretWords = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        self.secret = secretWords[random.randint(0,len(secretWords)-1)]
        self.hint = []
        self.win = False
        self.isItCorrect = False
        self.numGuesses = 0
        self.bodyParts = ["Head", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]

        for i in range(len(self.secret)):
            self.hint.append("?")

  def makeHint(self,guess):
        self.isItCorrect = False
        for i in range(len(self.secret)):
            if guess == self.secret[i]:
                self.hint[i] = guess
                self.isItCorrect = True
                
        if self.isItCorrect == False:
            self.numGuesses +=1

            
    def checkWin(self):

        self.win = True
                
        for i in range(len(self.hint)):
            if self.hint[i] == '?':
                self.win = False      

    def getSecret(self):
        return self.secret

    def getHint(self):
        return self.hint
        
    def getWin(self):
        return self.win

    def getGuesses(self):
        return self.numGuesses

    def getBodyParts(self):
        return self.bodyParts[0:self.numGuesses]

Hangman = hangman()
print("welcome to hangman!")
while(Hangman.getWin() == False and Hangman.getGuesses() < 6):
    guess = input("Please enter a letter:  ")
    Hangman.makeHint(guess)
    Hangman.checkWin()
    if Hangman.getWin() == True:
        print("hint = " + str(Hangman.getHint()))
        print("\n\ncongrats, you won, the word was: " + Hangman.getSecret())
    else:
        print("you didn't win yet, guesses remaining = " + str(6 - Hangman.getGuesses()))
        print("Body Parts Eliminated : " + str(Hangman.getBodyParts()))
        print("hint = " + str(Hangman.getHint())+"\n")
        
if Hangman.getWin() == False and 6 - Hangman.getGuesses() == 0:
    print("\n\nsorry, you lost, the secret word was: " + Hangman.getSecret())
