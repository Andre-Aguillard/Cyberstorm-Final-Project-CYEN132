# Python Code for CYEN 132 Final Rpi Assignement
# This is the final piece of code we are going to submit. 
# As I see features working in the other .py files, I'll add them here. -Andre
from Tkinter import *
import RPi.GPIO as GPIO

NumberOfLives = 6
HangmanWord = "Andromeda Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum \
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
        Ursa_Minor Vela Virgo Volans Vulpecula".split()"

# GUI to display picture, letters left, and letter input.
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
        
    def setupGUI(self):  # Initializes the layout for the GUI
        # Organize the GUI
        # this function works fine, as long as you have the images as actual
        # GIFs
        self.pack(fill=BOTH, expand=1)
        # setup the player input at the bottom of the GUI
        # widget is a Tkinter Entry
        # background is white; bind return key to function process in class
        Hangman.player_input = Entry(self, bg="white")
        Hangman.player_input.bind("<Return>", self.process)
        Hangman.player_input.pack(side=BOTTOM, fill=X)
        Hangman.player_input.focus()

        # setup image to the left of GUI
        # widget is a Tkinter label
        # don't let image control width's size
        img = None
        Hangman.image = Label(self, width=WIDTH / 2, height=HEIGHT, image=img)
        Hangman.image.image = img
        Hangman.image.pack(side=LEFT, fill=Y)
        Hangman.image.pack_propagate(False)
        # first, place frame where the text will be displayed
        text_frame = Frame(self, width=WIDTH / 2, height=HEIGHT)
        # widget - same deal as above
        # disable by default
        # don't let it control frame's size
        Hangman.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Hangman.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    def setHangmanImage(self):
        Hangman.img = PhotoImage(file="deathstar.gif")
        # pictures used must be saved as a gif.
        Hangman.image.config(image=Hangman.img)
        Hangman.image.image = Hangman.img

    def numberOfLives(self):
        # Light up the number of LED's equal to the number of Lives the user
        # has left.
        pass

    def display(self, response):
        # enable text widget, clear it, set it, disable it
        Hangman.text.config(state=NORMAL)
        Hangman.text.delete("1.0", END)
        Hangman.text.insert(END, "Welcome to intergalactic hangman, may I take your order?")
        Hangman.text.config(state=DISABLED)

# Need to add code for GPIO pins that light up with wrong, incorrect, and number of lives left
    def play(self):
        # configure GUI
        self.setupGUI()
        # set the Hangman Image
        self.setHangmanImage()
        # setup the text to display in the box to the left of the GUI
        self.display

    def process(self):
        pass
        # Grab the player's input from the input at the bottom of the GUI
        action = Hangman.player_input.get()
        # Convert all player input to lowercase.
        action = action.lower()
        # Make sure player input is only one character:
        ## Splits the player input based off white spaces and stores that in a list
        characters = action.split()
        if len(characters > 1):
            response = "Please input only one character as your guess. Thank you."
            display(response)
        else: 
            if (action in currentWord): '''NOTE: currentWord should be set up to be the current word to guess ''' 
                pass
                #Do something here
                #
            else:
                #IT not in word so blow up the death star some.
                response = character not in word. 
        self.display(response)
        self.setRoomImage()
        Hangman.player_input.delete(0, END)


#################### MAIN Code that runs before functions above everything up ####################
# Initialize the Raspberry Pi by disabeling any warnings and telling it
# we're going to use the BCM pin numbering scheme.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Initialize red and green led states
# No guesses have been made, so set both pins low to start
GPIO.output(26, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

# Initialize the number of lives LEDs here
# All of these should start lit up
pins = [21, 20, 26, 12, 19, 6, 5]  # list of GPIO pins for lights
for x in range(0, NumberOfLives):
    GPIO.output(pins[x], GPIO.HIGH)

# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# Main Code
# create the window
window = Tk()
window.title("Don't blow up the Death Star")
t = Hangman(window)
t.play()
window.mainloop()
