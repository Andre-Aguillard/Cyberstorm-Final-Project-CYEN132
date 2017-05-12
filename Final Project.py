from Tkinter import *
from time import sleep
import RPi.GPIO as GPIO

class HangmanWords(object):
    def __init__(self, name):
        self.name = name

    def populateWords(self):
        potentialWords = "Andromeda Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum \
        Camelopardalis Cancer Capricornus Carina Cassiopeia Centaurus Cepheus Cetus Chamaeleon \
        Circinus Columba Corvus Crater Crux Cygnus Delphinus Dorado Draco Equuleus Eridanus \
        Fornax Gemini Grus Hercules Horologium Hydra Hydrus Indus Lacerta Leo \
        Lepus Libra Lupus Lynx Lyra Mensa Microscopium Monoceros \
        Musca Norma Octans Ophiuchus Orion Pavo Pegasus Perseus Phoenix \
        Pictor Pisces Puppis Pyxis Reticulum Sagitta \
        Sagittarius Scorpius Sculptor Scutum Serpens Sextans Taurus \
        Telescopium Triangulum Tucana \
        Vela Virgo Volans Vulpecula".split()
        
        dictOfWords = {x:potentialWords[x] for x in range(0, len(potentialWords))}

        return(dictOfWords)


class Hangman(Frame):

    def __init__(self, parent):
        # calls constructor in superclass
        Frame.__init__(self, parent)  # This sets up the main window of the GUI
        self.parent = parent          # in order to build widgets on to top it.
        self.images =[]

    # image getter   
    @property
    def images(self):
        return self._images        
    # image setter
    @images.setter
    def images(self, value):
        self._images = value
    ## Add image function to easily change the image
    def addImage (self, image):
        self._images.append(image)

    def setupGUI(self): ##Initializes the layout for the GUI
        #Organize the GUI
        # this function works fine, as long as you have the images as actual GIFs
        self.pack(fill=BOTH, expand=1)
        self.parent.bind_all("<Control_L>", self.helpMe)
        #setup the player input at the bottom of the GUI
        #widget is a Tkinter Entry
        #background is white; bind return key to function process in class
        Hangman.player_input = Entry(self, bg="white")
        Hangman.player_input.bind("<Return>", self.process)
        Hangman.player_input.pack(side=BOTTOM, fill=X)
        Hangman.player_input.focus()
        
        # setup image to the left of GUI
        # widget is a Tkinter label
        # don't let image control width's size
        img = None
        Hangman.image = Label(self, width=WIDTH / 3, height=HEIGHT, image = img)
        Hangman.image.image = img
        Hangman.image.pack(side=LEFT, fill=Y)
        Hangman.image.pack_propagate(False)
        
        # first, place frame where the text will be displayed
        text_frame = Frame(self, width=WIDTH / 2, height=(HEIGHT/2))
        # widget - same deal as above
        # disable by default
        # don't let it control frame's size
        Hangman.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Hangman.text.pack(fill=Y, expand=1)
        text_frame.pack(side=TOP, fill=X)
        text_frame.pack_propagate(False)
        
        # Make another frame to hold the correct guess/ word display
        word_frame = Frame(self, width= WIDTH/3, height = HEIGHT/2)
        # widget - same deal as above
        # disable by default
        # don't let it control frame's size
        Hangman.correctWord = Text(word_frame, bg="white", state=DISABLED)
        Hangman.correctWord.pack(fill=Y, expand = 1)
        word_frame.pack(side =TOP, fill=X)
        word_frame.pack_propagate(False)

    def setHangmanImage(self):
        global Images
        Hangman.original = PhotoImage(file=Images[0])
        #resize the image to fit. 
        Hangman.img = Hangman.original.subsample(2,2)
        # Note: Subsample is used to make the image smaller, zoom is to make it bigger.
        Hangman.image.config(image=Hangman.img)
        Hangman.image.image = Hangman.img

    def updateHangmanImage(self):
        x = self.NumberOfLives - 1
        global Images
        Hangman.original = PhotoImage(file=Images[x])
        #resize the image to fit. 
        Hangman.img = Hangman.original.subsample(1,1)
        Hangman.image.config(image=Hangman.img)
        Hangman.image.image = Hangman.img
    
    def setupGPIO(self):
        # Initialize the Raspberry Pi by disabeling any warnings and telling it
        # we're going to use the BCM pin numbering scheme.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        # Initialize red and green led states
        # No guesses have been made, so set both pins low to start
        GPIO.output(26, GPIO.LOW)#   Correct Guessed letter
        GPIO.output(13, GPIO.LOW)# Incorrect Guessed letter 
        
        # Initialize the number of lives LEDs here
        # All of these should start lit up
        pins = [16,20,21,22,27,17,6]  # list of GPIO pins for lights
        for x in range(0, self.NumberOfLives):
            GPIO.output(pins[x], GPIO.HIGH)

##### Process Function that controls the flow of the program #######    
    def process(self, event):
        ### Word they are guessing
        g = self.mainWord
        # Prints something of the DEBUG variable is true
        if (DEBUG == True):
            print(Hangman.listOfBlanks)
            
        # Grab the player's input from the input at the bottom of the GUI
        action = Hangman.player_input.get()
        # Convert all player input to lowercase.
        action = action.lower()
        found = False

        #Makes sure that the user only guesses one letter not a number
        if (action.isdigit() ):
            response =("Please input only letters such as a,b,c etc...\n\n" \
                       +"{} is a number...\n\n\n                    "\
                       +"Don't let this mistake happen again.").format(action)        
            display(response)
        elif (len(action) != 1):
              response = "Please input only one character as your guess. Thank you."
              display(response)
              sleep(5)
        # If it is one letter then do this stuff:
        else:
            if (action in Hangman.lettersGuessed):
                response = ("You've already guessed {} try another one.").format(action)
                display(response)
            else:
                #Append the letter guessed to the list of Letters Guessed if it hasn't been guessed yet.
                Hangman.lettersGuessed.append(action)
                #Puts the list in alphabetical order
                Hangman.lettersGuessed.sort()
                
                #Check to see if the player's input is in the the word
                #Creates an index based off the nuber of letters in the word
                for i in xrange(len(g)):
                    if (action == g[i]):
                        # If action is equal to a letter at a certain index
                        # in the word, then place that letter in the blank
                        Hangman.listOfBlanks[i] = action
                        found = True
                        ''' So the guess is correct, that means the correct pin
                            lights up and the wrong pin turns off.'''
                        GPIO.output(26, GPIO.HIGH)
                        GPIO.output(13, GPIO.LOW)
                if (found == False):
                    #The guess was wrong, so the number of lives the user has left decreases,
                    # and the wrong guess pin lights up 
                    self.NumberOfLives -= 1
                    GPIO.output(26, GPIO.LOW)
                    GPIO.output(13, GPIO.HIGH)
                    #Hangman.updateHangmanImage()
                    
                    #function that changes the GPIO pins
                    
                #If the number of lives equals 0 then Game over
                if (self.NumberOfLives == 0):
                    self.gameOver()
                #If there are no more blanks in the list then they guessed the word correctly and won the game.
                if ("__" not in Hangman.listOfBlanks):
                    self.youWin()
              
        response =("Number of Lives: {} \nLetters guessed: {}").format(self.NumberOfLives, Hangman.lettersGuessed)
        correctWordDisplay(response)
        Hangman.player_input.delete(0, END)
        
		
############## PLAY FUNCTION WHERE EVERYTHING Begins :) #######################        
    def play(self, unknownWord):
        #Sets the inputed word as the main word the user tries to guess
        self.mainWord = unknownWord
        # Turns the inputed word into a lowercase word.
        self.mainWord = self.mainWord.lower()
        # Set the number of lives the user has
        self.NumberOfLives = 3
        
        if (DEBUG == True):
            print (self.mainWord)
        # Setup everything
        self.setupGPIO
        self.setupGUI()
        self.setHangmanImage()

        #initialize the lettersGuessed
        Hangman.lettersGuessed = []
        #Starts of the game with a list of blanks for every letter in the word.
        Hangman.listOfBlanks = ["__" for x in self.mainWord]
        
        response = "Imperial Officer:\n\nWelcome to the Death Star, recruit. I understand this is your first day with\n" \
                    +"us, so I'll keep it brief.\n" \
                    +"The Rebel Alliance has launched a ridiculous and foolhardy attack against our\n" \
                    +"superior defense systems, and we need you to man the Ion Cannons on level B.\n" \
                    +"The setup is simple, our engineers have made it so you only have to solve\n" \
                    +"a game of Hangman in order to engage the auto-targeting system,\n" \
                    +"if you get it wrong, well... don't.\n" \
                    +"Anyway our defenses here are practically impenetrable, after all there'd have\n" \
                    +"to be some fundamental flaw in the station for anything truly devastating\n" \
                    +"to happen.\n\n" \
                    +"Well off you go, press Ctrl for help and type in any letter to begin Hangman."
        display (response)
        response =("Number of Lives: {} \nLetters guessed: {}").format(self.NumberOfLives, Hangman.lettersGuessed)
        correctWordDisplay(response)

    def gameOver(self):
        # Clear the entry widget so it don't display anything. 
        Hangman.player_input.delete(0, END)
        #Disable the entry so they can't keep typing in letters after they lose.
        Hangman.player_input.config(state=DISABLED)
        response = "Game Over. You let the Rebel scum win..."
        display(response)
        window.update
        sleep(2)
        response = "Game Over. You let the Rebel scum win... \
                    \n\nOh well. Looks like we'll have to build another\n" \
                    +"one. Hopefully you can keep that in one piece."
        display(response)
        self.updateHangmanImage()
    
    def helpMe(self,please):
        response =  "HELP SCREEN ---- type any letter to continue guessing. \n\n" \
                   +"This is a simple game of Hangman with an outer space twist. \n" \
                   +"You are an Imperial soldier working to protect the Empire's  latest "\
                   + "superweapon, The DeathStar! \n" +"Rebel fighters have emerged from "\
                   +"space to blow up this planetary threat, and you must stop them by " \
                   +"spelling the correct word within the time limit.\n\n" \
                   +"Guess letters one at a time by typing them into the entry blank at the "\
		   +"bottom of the window and pressing enter.\n" \
                   +"Hint: think constellations."
        print(response)
        display(response)
        
    def  youWin(self):
        response = "Congragulations! You've managed to do your job correctly." \
                   +"Unfortunately due to piracy in the Yavin sector there is a shortage\n" \
                   +"of celebratory cookies, so we'll just give you a gold star sticker,\n" \
                   +"Additionally, to reward your bravery, Grand Moff Tarkin has given you\n" \
                   +"permission to select the next word.\n\nType in the number of the word\n" \
                   +"into the popup window and hit accept."
        display(response)
        sleep(3)
        #Calls the popup window with a list of words
        x = PopUpWindow("star")
        x.popupWindowWithScrollBar()


class PopUpWindow(object):
    def __init__(self, initialWord):
        #Set the inital word to start the game.
        self.initialWord = initialWord
        self.wordKeys= []
    
    def popUpProcess(self,number):
        #Take the player input from the popup window
        action = int(number)
        # Check to see if the inputted number is in the list of potential words
        if (action in PopUpWindow.dictOfWords):
            PopUpWindow.top.destroy()
            PopUpWindow.top = Toplevel()
            PopUpWindow.top.title("You chose: ")

            text_frame = Frame(PopUpWindow.top, width=WIDTH / 2, height=(HEIGHT*(2/3)))
            # widget - same deal as above
            # disable by default
            # don't let it control frame's size
            PopUpWindow.text = Text(text_frame, bg="lightgrey", state=DISABLED)
            PopUpWindow.text.pack(fill=Y, expand=1)
            text_frame.pack(side=TOP, fill=Y)
            text_frame.pack_propagate(False)

            HangmanWord = PopUpWindow.dictOfWords[action]
            
            Hangman.button = Button(PopUpWindow.top, text="Accept", padx=10, pady=15, width =150, command= lambda:newGame(HangmanWord))
            Hangman.button.pack(side=BOTTOM, fill=X)
            mainloop()
        else:
            print('invaild number')
            display("Invalid Number")
        
    def popupWindowWithScrollBar(self):
        x = HangmanWords("Andre")
        PopUpWindow.dictOfWords = x.populateWords()
        PopUpWindow.top = Toplevel()
        PopUpWindow.top.title("List of words:")

        button_frame = LabelFrame(PopUpWindow.top,text="Buttons for user input" ,width= WIDTH/2, height=HEIGHT, relief =RAISED)
        ##Define what each button looks like and does. 
        PopUpWindow.button1= Button(button_frame, text="1", padx=10, pady=10, width=10,command= lambda: self.inputNumber(1))
        PopUpWindow.button2= Button(button_frame, text="2", padx=10, pady=10, width=10,command= lambda: self.inputNumber(2))
        PopUpWindow.button3= Button(button_frame, text="3", padx=10, pady=10, width=10,command= lambda: self.inputNumber(3))
        PopUpWindow.button4= Button(button_frame, text="4", padx=10, pady=10, width=10,command= lambda: self.inputNumber(4))
        PopUpWindow.button5= Button(button_frame, text="5", padx=10, pady=10, width=10,command= lambda: self.inputNumber(5))
        PopUpWindow.button6= Button(button_frame, text="6", padx=10, pady=10, width=10,command= lambda: self.inputNumber(6))
        PopUpWindow.button7= Button(button_frame, text="7", padx=10, pady=10, width=10,command= lambda: self.inputNumber(7))
        PopUpWindow.button8= Button(button_frame, text="8", padx=10, pady=10, width=10,command= lambda: self.inputNumber(8))
        PopUpWindow.button9= Button(button_frame, text="9", padx=10, pady=10, width=10,command= lambda: self.inputNumber(9))
        PopUpWindow.button0= Button(button_frame, text="0", padx=10, pady=10, width=10,command= lambda: self.inputNumber(0))
        PopUpWindow.buttonENTER= Button(button_frame, text="Enter", padx=10, pady=10, width=10,command= self.condenseNumber)
        
        ##place the buttons in a grid within the button frame.
        PopUpWindow.button1.grid(row=0, column=0)
        PopUpWindow.button2.grid(row=0, column=1)
        PopUpWindow.button3.grid(row=0, column=2)
        PopUpWindow.button4.grid(row=1, column=0)
        PopUpWindow.button5.grid(row=1, column=1)
        PopUpWindow.button6.grid(row=1, column=2)
        PopUpWindow.button7.grid(row=2, column=0)
        PopUpWindow.button8.grid(row=2, column=1)
        PopUpWindow.button9.grid(row=2, column=2)
        PopUpWindow.button0.grid(row=3, column=1)
        PopUpWindow.buttonENTER.grid(row=3, column=2)
        
        # initalize the button-frame, and don't let it control the frame's size
        ## Place it on the right side and let it be full sized.         
        button_frame.pack(side=BOTTOM, fill=X, expand=1)
        button_frame.pack_propagate(False)

        #Puts the scrollbar aligned with only the listbox -Dax
        scrollbar = Scrollbar(PopUpWindow.top)
        scrollbar.pack(side=RIGHT, fill=Y)

        #Creates a listbox that holds all the potential words that could be guessed.
        PopUpWindow.listbox = Listbox(PopUpWindow.top, yscrollcommand=scrollbar.set, width=100)
        #Put all the words from the dicttionary into the scrollbox
        for key,value in PopUpWindow.dictOfWords.items():
            PopUpWindow.listbox.insert(END, str(key) + "-->" + value)
        PopUpWindow.listbox.pack(side=LEFT, fill=BOTH)
        # Place the scrollbar on the left and have it stay in view
        scrollbar.config(command=PopUpWindow.listbox.yview)

    def inputNumber(self,number):
        number = str(number)
        self.wordKeys.append(number)

    def condenseNumber(self):
        wordNumber = "".join(self.wordKeys)
        self.popUpProcess(wordNumber)
  
def newGame(HangmanWord):
    #Set the Hangman word input into the system as THE word and restart a new Game
    PopUpWindow.top.destroy()
    global t
    t.destroy()
    t = Hangman(window)
    t.play(HangmanWord)

def correctWordDisplay(word):
        Hangman.correctWord.config(state=NORMAL)
        Hangman.correctWord.delete("1.0", END)
        # Display the desired text on the screen.
        Hangman.correctWord.insert(END, "Word you're trying to guess: " + "\n\n" +str(Hangman.listOfBlanks)+ "\n\n" + word)
        if (DEBUG == True):
            print (word)
        Hangman.correctWord.config(state=DISABLED)
        #Updates the Tk window to show the progress of the locking sequence. 
        window.update()
def display(response):
    #### Display is 
    Hangman.text.config(state=NORMAL)
    Hangman.text.delete("1.0", END)
    # Display the desired text on the screen.
    Hangman.text.insert(END, response)
    if (DEBUG == True):
        print (response)
    Hangman.text.config(state=DISABLED)
    #Updates the Tk window to show the progress of the locking sequence. 
    window.update()

    
# the default size of the GUI is 800x600
WIDTH = 1300
HEIGHT = 500

#Creates a Debug boolean
# Set to True to turn on a debug process.
DEBUG = False

initialWord = "Ophiuchus"


Images = ["DeathStar1.gif","DeathStar2.gif"]
window = Tk()
window.title("Don't blow up the Death Star")

t = Hangman(window)
t.play(initialWord)
window.mainloop()
