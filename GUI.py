from Tkinter import *
from time import sleep


class HangmanWords(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # Number of letters in word
        n = len(word)
    def populateWords(self):
        potentialWords = "Andromeda Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum \
        Camelopardalis Cancer Canes_Venatici Canis_Major Canis_Minor \
        Capricornus Carina Cassiopeia Centaurus Cepheus Cetus Chamaeleon \
        Circinus Columba Coma_Berenices Corona_Austrina Corona_Borealis \
        Corvus Crater Crux Cygnus Delphinus Dorado Draco Equuleus Eridanus \
        Fornax Gemini Grus Hercules Horologium Hydra Hydrus Indus Lacerta Leo \
        Leo_Minor Lepus Libra Lupus Lynx Lyra Mensa Microscopium Monoceros \
        Musca Norma Octans Ophiuchus Orion Pavo Pegasus Perseus Phoenix \
        Pictor Pisces Piscis_Austrinus Puppis Pyxis Reticulum Sagitta \
        Sagittarius Scorpius Sculptor Scutum Serpens Sextans Taurus \
        Telescopium Triangulum Triangulum_Australe Tucana Ursa_Major \
        Ursa_Minor Vela Virgo Volans Vulpecula".split()
        
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
        Hangman.image = Label(self, width=WIDTH / 2, height=HEIGHT, image = img)
        Hangman.image.image = img
        Hangman.image.pack(side=LEFT, fill=Y)
        Hangman.image.pack_propagate(False)
        # first, place frame where the text will be displayed
        text_frame = Frame(self, width=WIDTH / 2, height=(HEIGHT*(2/3)))
        # widget - same deal as above
        # disable by default
        # don't let it control frame's size
        Hangman.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Hangman.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
        # Make another frame to hold the correct guess/ word display
        word_frame = Frame(self, width= WIDTH/3, height = HEIGHT/3)
        # widget - same deal as above
        # disable by default
        # don't let it control frame's size
        Hangman.correctWord = Text(word_frame, bg="white", state=DISABLED)
        Hangman.correctWord.pack(fill=Y, expand = 1)
        word_frame.pack(side =TOP, fill=Y)
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
        x = NumberOfLives - 1
        global Images
        Hangman.original = PhotoImage(file=Images[x])
        #resize the image to fit. 
        Hangman.img = Hangman.original.subsample(1,1)
        Hangman.image.config(image=Hangman.img)
        Hangman.image.image = Hangman.img

    
    def process(self):
        ### Word they are guessing
        g = list(self.mainWord)
        Hangman.dictOfLetters = {g[x]: '__ '  for x in xrange(len(g))}
        print(Hangman.dictOfLetters)

##        return(str(self.dictOfLetters))
    
        pass
        action = Hangman.player_input.get()
    
        
    def play(self, unknownWord):
        self.mainWord = unknownWord
        self.setupGUI()
        self.setHangmanImage()
        #Calls the popup window with a list of words
        x = PopUpWindow("star")
        x.popupWindowWithScrollBar()
        self.process()
        correctWordDisplay("star:")

    def gameOver(self):
        response = "Game Over. You let the Rebel scum win..."
        display(response)
        window.update
        sleep(2)
        response = "Game Over. You let the Rebel scum win... \
                    \n\nOh well. Looks like we'll have to build another\n" \
                    +"one. Hopefully you can keep that in one piece."
        display(response)
        self.updateHangmanImage()
    
    def helpMe(self):
        response =  "HELP SCREEN ---- type {} to exit. \n\n\n" \
                   +"This is a simple game of Hangman with an outer space twist. \n" \
                   +"You are an Imperial soldier working to protect the Empire's  latest "\
                   + "superweapon, The DeathStar! \n" +"Rebel fighters have emerged from "\
                   +"space to blow up this planetary threat, and you must stop them by " \
                   +"spelling the correct word within the time limit.\n\n" \
                   +"Guess letters by typing them into the entry below."
        print(response)



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
            
            Hangman.button = Button(PopUpWindow.top, text="Accept", width =WIDTH/3, command= lambda:newGame(HangmanWord))
            Hangman.button.pack(side=BOTTOM, fill=X)
            mainloop()
        else:
            print('invaild number')
        
    def popupWindowWithScrollBar(self):
        x = HangmanWords("Andre")
        PopUpWindow.dictOfWords = x.populateWords()
        PopUpWindow.top = Toplevel()
        PopUpWindow.top.title("List of words:")

        scrollbar = Scrollbar(PopUpWindow.top)
        scrollbar.pack(side=RIGHT, fill=Y)

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
        PopUpWindow.buttonENTER= Button(button_frame, text="Enter#", padx=10, pady=10, width=10,command= self.condenseNumber)
        
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
        Hangman.correctWord.insert(END, "Word you're trying to guess: " + "\n\n" +str((Hangman.dictOfLetters.values())) )
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
    print (response)
    Hangman.text.config(state=DISABLED)
    #Updates the Tk window to show the progress of the locking sequence. 
    window.update()

    
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

global NumberOfLives
NumberOfLives = 2
initialWord = "Star"


Images = ["DeathStar1.gif","DeathStar2.gif"]
window = Tk()
window.title("Don't blow up the Death Star")

t = Hangman(window)
t.play(initialWord)
window.mainloop()
