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
        Hangman.player_input.bind("<Return>", process)
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

    def popupWindowWithScrollBar(self):
        x = HangmanWords("Andre")
        dictOfWords = x.populateWords()
        Hangman.top = Toplevel()
        Hangman.top.title("List of words:")

        Hangman.scrollbar = Scrollbar(Hangman.top)
        Hangman.scrollbar.pack(side=RIGHT, fill=Y)

        Hangman.player_input = Entry(Hangman.top, width =100)
        Hangman.player_input.bind("<Return>", process(1))
        Hangman.player_input.pack(side=BOTTOM, fill=X)
        Hangman.player_input.focus

        Hangman.listbox = Listbox(Hangman.top, yscrollcommand=Hangman.scrollbar.set, width=100)
        for key,value in dictOfWords.items():
            Hangman.listbox.insert(END, str(key) + "-->" + value)
        Hangman.listbox.pack(side=LEFT, fill=BOTH)

        Hangman.scrollbar.config(command=Hangman.listbox.yview)
    
    def play(self):
        # configure GUI
        self.setupGUI()
        # set the Hangman Image
        self.setHangmanImage()
        response = ("Welcome to Galactic Hangman! May I take your order?\n\n"+ \
                    "Please enter the number of the word you desire the next team to "+ \
                    "spell in the entry blank of the popup screen.")
        display(response)
        #Calls the popup window with a list of words
        self.popupWindowWithScrollBar()
        word = " Word "
        correctWordDisplay(word)
        sleep(5)
        self.gameOver()
        window.update()
        sleep(8)
        self.helpMe()

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
        display(response)
        
def correctWordDisplay(word):
##    global guess
##    if (guess == True):
        Hangman.correctWord.config(state=NORMAL)
        Hangman.correctWord.delete("1.0", END)
        # Display the desired text on the screen.
        Hangman.correctWord.insert(END, word)
        print (word)
        Hangman.correctWord.config(state=DISABLED)
        #Updates the Tk window to show the progress of the locking sequence. 
        window.update()
##    else :
##        Hangman.correctWord.config(state=NORMAL)
##        Hangman.correctWord.delete("1.0", END)
##        # Display the blanks and correct letters
##        Hangman.correctWord.insert(END, " _ _ _ _ _ _ E D")
##        Hangman.correctWord.config(state=DISABLED)
##        window.update()

def process(self):
    pass
    
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

guess = True

Images = ["DeathStar1.gif","DeathStar2.gif"]
window = Tk()
window.title("Don't blow up the Death Star")
t = Hangman(window)
t.play()
window.mainloop()
