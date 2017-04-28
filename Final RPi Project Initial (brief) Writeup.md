Group Members: André Aguillard, Dax Henson, Rylan Burlison

# Project Title: How Not to Blow up the Death Star 

# Project Overview: 
We will create a game of hangman using python, a GUI, and the Raspberry Pi’s GPIO pins. The pins will trigger various LED’s. A green one will light up if a letter is in the word, and a red one will light up if the letter is wrong. Additionally, there will be a line of 6 or so LEDs that display the number of lives or incorrect guesses left. This line will originally all be lit up, but will turn off when an incorrect guess is made. The GUI will display a picture of the Death Star which will gradually be blown up by incorrect guesses, and underneath that will be a space to input letters, next to those will be another label which displays the letters that one could guess, and those letters will slowly disappear once they are guessed. The goal of the game is to guess the correct word, before the Death Star blows up. The way this can be implemented at Cyberstorm is that the original word is the name of a constellation, and if the first team guesses that word, they can pick the next word for a different team to guess from a list of constellation names. Then that word is typed into the python program and a new game is generated. If the team doesn’t guess that word correctly within a time limit or they run out of lives, it’s the next team’s turn. Alternatively, we could just have a list of words and the team that gets the most correct wins. 

# How the Project Addresses the Theme: 
	The words are all constellation names, and the hangman figure is the Death Star being gradually blown up. 

# Justification that this idea can be completed be a three man group:
	The work required to complete this project is the code for the python game, and to control the GPIO pins, as well as the GUI on display. It is fairly complicated, but with three people working on the project, we can split up the roles and focus on a specific part, and assist each other if we get stuck. 
