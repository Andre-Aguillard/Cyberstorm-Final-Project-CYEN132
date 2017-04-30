## Python Code for CYEN 132 Final Rpi Assignement
from Tkinter import *
import RPi.GPIO as GPIO

NumberOfLives = 6
HangManword = "Word"

# GUI to display picture, letters left, and letter input.
class GUI4Hangman(Frame):
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
    GUI4Hangman.player_input = Entry(self, bg="white")
    GUI4Hangman.player_input.bind("<Return>", self.process)
    GUI4Hangman.player_input.pack(side=BOTTOM, fill=X)
    GUI4Hangman.player_input.focus()
    
    # setup image to the left of GUI
    # widget is a Tkinter label
    # don't let image control width's size
    img = None
    GUI4Hangman.image = Label(self, width=WIDTH / 2, height=HEIGHT, image = img)
    GUI4Hangman.image.image = img
    GUI4Hangman.image.pack(side=LEFT, fill=Y)
    GUI4Hangman.image.pack_propagate(False)


# GPIO pins that light up with wrong, incorrect, and number of lives left

# Initialize the Raspberry Pi by disabeling any warnings and telling it
# we're going to use the BCM pin numbering scheme.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Initialize red and green led states
# No guesses have been made, so set both pins low to start
GPIO.output(InputPinNumber1Here, GPIO.LOW)
GPIO.output(InputPinNumber2Here, GPIO.LOW)
#Initialize the number of lives LEDs here
#All of these should start lit up
GPIO.output(InputPinNumber1Here, GPIO.HIGH)
GPIO.output(InputPinNumber2Here, GPIO.HIGH)

# Main Code 

window = Tk()
window.title("Don't blow up the Death Star")
t = GUI4Hangman(window)
t.setupGUI()
window.mainloop()

