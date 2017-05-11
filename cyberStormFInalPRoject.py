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
	#pictures used must be saved as a gif.
	Hangman.image.config(image=Hangman.img)
	Hangman.image.image = Hangman.img
	
  def numberOfLives(self):
	# Light up the number of LED's equal to the number of Lives the user has left.
	# the number of lives remaining would be the total lives minus the number of incorrect letters guessed
	pass
  
  def setStatus(self, status):
	  # enable text widget, clear it, set it, disable it
	  Hangman.text.config(state=NORMAL)
	  Hangman.text.delete("1.0", END) 
	  Hangman.text.insert(END, "Welcome to intergalactic hangman, may I take your order?")
	  
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
          # Grab the player's input from the input at the bottom of the GUI
          action = Hangman.player_input.get()
          # Convert all player input to lowercase.
          action = action.lower()
          # Make sure player input is only one character:
          ## Splits the player input based off white spaces and stores that in a list
          characters = action.split()
          if len(characters != 1):
              response = "Please input only one character as your guess. Thank you."
              display(response)
          else:
              self.checkInput() 
	
          self.display(response)
          self.setRoomImage()
          Hangman.player_input.delete(0, END)


                
                

 def checkInput(self):
		#declares a variable for the list of the letters for the word
		letters = list(HangManWord)
		#first deletes duplicates in the list of letters
		#then declares a variable to store the word's range
		letters = set(letters)
		rang = range(letters)
        
		#declare a list for correct and incorrect guesses
		correct = []
		incorrect = []
				

			
		#runs unitl the amount of letters in the correct list are the
			#same amount of letters as the word being guessed
		#also only if the number of incorrect is less than amount of lives
                    if(range(correct) < rang & range(incorrect) < NumberOfLives):
					
                         #this part will check to see if the letter the player guessed is in the
			 #word they are trying to guess
                         #ALSO
                         #only adds the correct letter to the list if it not already
			 #in the list of guessed letters
                            if (characters in letters & characters not in correct[]):

					correct.append(characters)
				
				#add function to  add the letters to the screen
				#need to define this function
					self.rightGuess()
				#add the correct letters to the gui as well as the number of times they occur
				#use the format list.count() to count the number of occurences
				#this can be used in conjuction with the guess to
				#display how many times the letter
				#occurs in the word being guess
				
                                #Set green led to high(
				#removes the correct guess from the list of guesses
				#Keep the game image the same (do nothing)
				
                          #if the letter is already in list of correct letters guessed then it won't count against them
			    elif(charcters in letters & characters in correct[]):
                            		response = "You have already guessed this letter."
                              
                            else:
					#could use function called wrongGuess()
                                	incorrect.append(charcters)
                                	response = "Character not in word."
                                	#change the game image
			
		    #if the range of correct guesses equals rang (number of letters to be guessed) then all letters have been guessed	
		    elif(range(correct) = rang):
				self.youWin()
			  							
                        #the word should be removed from the dictionary so it can't be guessed agai
                       #the gui needs to let the player know that they have won and needs to provide the dicitonary so the player can
                       #choose which word the next team has to try to guess
                      
								 
                    #otherwise the player has had too many incorrect guessses and loses
                    else:
                        	self.gameOver()
	
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
	 guess
