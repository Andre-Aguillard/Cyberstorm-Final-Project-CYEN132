## Python Code for CYEN 132 Final Rpi Assignement
from tkinter import *
import RPi.GPIO as GPIO

NumberOfLives = 6

# GUI to display picture, letters left, and letter input.
class GUI4Hangman(Frame):
  def __init__(self, master):
    Frame.__init__(self,master) ### This sets up the main window of the GUI
    self.master = master     ### in order to build widgets on to top it.
    
  def setupGUI(self): ##Initializes the layout for the Gui
    e1 = Entry  (self.master)
    e1.pack(side=LEFT, expand=1)


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

