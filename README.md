# Cyberstorm-Final-Project-CYEN132
Final project for our cyber/cs class    
Theme of Cyberstorm is Constellation   
Parameters for the project: It must use GPIO with Rpi, Python, and be a puzzle.    
Team Members: Andre Aguillard, Rylan Burlison, Dax Henson


### Project Overview: 
  We will create a game of hangman using python, a GUI, and the Raspberry Pi’s GPIO pins. The pins will trigger various LED’s. A green one will light up if a letter is in the word, and a red one will light up if the letter is wrong. Additionally, there will be a line of 6 or so LEDs that display the number of lives or incorrect guesses left. This line will originally all be lit up, but will turn off when an incorrect guess is made. The GUI will display a picture of the Death Star which will gradually be blown up by incorrect guesses, and underneath that will be a space to input letters, next to those will be another label which displays the letters that one could guess, and those letters will slowly disappear once they are guessed. The goal of the game is to guess the correct word, before the Death Star blows up. The way this can be implemented at Cyberstorm is that the original word is the name of a constellation, and if the first team guesses that word, they can pick the next word for a different team to guess from a list of constellation names. Then that word is typed into the python program and a new game is generated. If the team doesn’t guess that word correctly within a time limit or they run out of lives, it’s the next team’s turn. Alternatively, we could just have a list of words and the team that gets the most correct wins. 


### Clarity on the code above:
  The Final Project.py is our final piece of code to submit.       
  The GUI.py is the code for the GUI     
  The other .py files are places to work on the code.    

### Screenshots:

GUI Home screen:
![Alt text](GUIcapture.png)

Circuit Layout Note, we used a GPIO breakout to link the Raspberry Pi to the Breadboard
![Alt Text](CircuitLayoutCapture.PNG)
