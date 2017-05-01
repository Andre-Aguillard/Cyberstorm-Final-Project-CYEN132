# Python Code for CYEN 132 Final Rpi Assignement
from Tkinter import *
import RPi.GPIO as GPIO

NumberOfLives = 6
HangmanWord = "word"

class Images(object):
    def __init__(self, name):
        self.name = name
        self.images = [] # list for images
        
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

# GUI to display picture, letters left, and letter input.
class Hangman(Frame):

    def __init__(self, parent):
        # calls constructor in superclass
        Frame.__init__(self, parent)  # This sets up the main window of the GUI
        self.parent = parent          # in order to build widgets on to top it.

        
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

    def setStatus(self, status):
        # enable text widget, clear it, set it, disable it
        Hangman.text.config(state=NORMAL)
        Hangman.text.delete("1.0", END)
        Hangman.text.insert(
            END, "Welsom to intergalactic hangman, may I take your order?")

# GPIO pins that light up with wrong, incorrect, and number of lives left
    def play(self):
        # configure GUI
        self.setupGUI()
        # set the Hangman Image
        self.setHangmanImage()
        # setup the text box to the left of the GUI
        self.setStatus

    def process(self):
        pass
        
        self.setStatus(response)
        self.setRoomImage()
        Hangman.player_input.delete(0, END)


#################### MAIN FUNCTION that sets everything up ####################
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
