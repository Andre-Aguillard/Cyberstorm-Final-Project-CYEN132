## Python Code for CYEN 132 Final Rpi Assignement
from tkinter import *
import RPi.GPIO as GPIO



# GUI to display picture, letters left, and letter input.
class GUI4Hangman(Frame):
  def __init__(self, master):
    Frame.__init__(self,master) ### This sets up the main window of the GUI
    self.master = master     ### in order to build widgets on to top it.
    
  def setupGUI(self): ##Initializes the layout for the Gui
    e1 = Entry  (self.master)
    e1.pack(side=LEFT, expand=1)


# GPIO pins that light up with wrong, incorrect, and number of lives left


# Main Code 

window = Tk()
window.title("Don't blow up the Death Star")
t = GUI4Hangman(window)
t.setupGUI()
window.mainloop()

