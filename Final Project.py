## Python Code for CYEN 132 Final Rpi Assignement
from Tkinter import *
import RPi.GPIO as GPIO

NumberOfLives = 6
HangManword = "word"

# GUI to display picture, letters left, and letter input.
class Hangman(Frame):
  def __init__(self, parent):
    # calls constructor in superclass
    Frame.__init__(self,parent) ### This sets up the main window of the GUI
    self.parent = parent        ### in order to build widgets on to top it.
                
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
    
    Hangman.text = Text(text_frame, bg="lightgrey", state=DISABLED)
    Hangman.text.pack(fill=Y, expand=1)
    text_frame.pack(side=RIGHT, fill=Y)
    text_frame.pack_propagate(False)
    
  def setHangmanImage(self):
    Hangman.img = PhotoImage(file=deathstar.jpg)
    Hangman.image.config(image=Game.img)
    Hangman.image.image = Game.img
    
  def numberOfLives(self):
    # Light up the number of LED's equal to the number of Lives the user has left.
    pass
# GPIO pins that light up with wrong, incorrect, and number of lives left
  def play(self):
    # configure GUI
    self.setupGUI()
    # set the Hangman Image
    self.setHangmanImage()
    
  def process(self):
    pass
    
####################### MAIN FUNCTION that sets everything up #################

# Initialize the Raspberry Pi by disabeling any warnings and telling it
# we're going to use the BCM pin numbering scheme.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Initialize red and green led states
# No guesses have been made, so set both pins low to start
GPIO.output(26, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
#Initialize the number of lives LEDs here
#All of these should start lit up
pins = [21,20,26,12,19,6,5] #list of GPIO pins for lights
for x in range (0, NumberOfLives) :
  GPIO.output(pins[x],GPIO.HIGH)

# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
  
# Main Code 
#create the window
window = Tk()
window.title("Don't blow up the Death Star")
t = GUI4Hangman(window)
t.play()
window.mainloop()
