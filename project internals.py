# this is the sandbox for the internal logic and backend of the program
# I'm probably goin to spend most of my time here --Dax
from Tkinter import *

words = "Andromeda Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum \
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


class Game(Frame):

    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # sets the current room image
    def setRoomImage(self):
        if (Game.currentRoom is None):
            # if dead, set the skull image
            Game.img = PhotoImage(file=None)
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=None)
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom is None):
            # if dead, let the player know
            if (r12.interac["bomb"][2] == "off"):
                Game.text.insert(END, "An explosion killed you.\n"
                                 "You have died.\n\n"
                                 "The only thing you can do now is quit.\n")
            Game.text.insert(END, "You have jumped out of a window to your "
                                  "death.\nYou have died.\n\nThe only thing "
                                  "you can do now is quit.")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom)
                             + "\nYou are carrying: "
                             + str(sorted(Game.inventory.keys()))
                             + "\n\n" + status)
        Game.text.config(state=DISABLED)

    # plays the game
    def play(self):
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):
        kills = ["quit", "exit", "bye"]
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # split the user input into words (words are separated by
        # spaces) and store the words in a list
        words = action.split()
        # set a default response
        response = "I don't understand. Try verb noun. "\
                   "Valid verbs are go, look, and take"
        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)
        if (len(words) == 1):
            response = "What?"
            for i in kills:
                if (match(action, i)):
                    exit(0)
        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom is None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]
            # the verb is: go
            if (verb in ["go", "head"]):
                # set a default response
                response = "There's a wall there."
                # check for valid exits in the current room
                for i in Game.currentRoom.exits:
                    if (match(noun, i)):
                        # if one is found, change the current room to
                        # the one that is associated with the
                        # specified exit
                        Game.currentRoom = Game.currentRoom.exits[i]
                        # set the response (success)
                        response = "Room changed."
                        break
                    if (match(noun, "down")):
                        response = "There's a floor there."
                        if (Game.currentRoom == r0):
                            response = "Digging a cave is too labor-intensive."
                        break
                    if (match(noun, "up")):
                        response = "There's a ceiling there."
                        if (Game.currentRoom == r0):
                            response = "You can't fly."
                        break
            # the verb is: look
            elif (verb in ["look", "check"]):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                for i in Game.currentRoom.items:
                    if (match(noun, i)):
                        # if one is found, set the response to the
                        # item's description
                        response = Game.currentRoom.items[i]
                        break

                for i in Game.currentRoom.interac:
                    if (match(noun, i)):
                        response = Game.currentRoom.interac[i][0]
                        break

                for i in Game.currentRoom.hiddenItems:
                    if (match(noun, i)):
                        response = Game.currentRoom.hiddenItems[i]
                        break

                for i in Game.currentRoom.grabbables:
                    if (match(noun, i)):
                        response = Game.currentRoom.grabbables[i]
                        break

                for i in Game.inventory:
                    if (match(noun, i)):
                        response = Game.inventory[i]
                        break

            # the verb is: take
            elif (verb in ["take", "get"]):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current room
                for i in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (match(noun, i)):
                        # add the grabbable item to the player's inventory
                        Game.inventory[i] = Game.currentRoom.grabbables[i]
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(i)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break
            elif (verb in ["use"]):
                response = "You don't have that item."
                for item in Game.inventory:
                    if (match(noun, item)):
                        response = "{} could not be used.".format(item)

                        for i in Game.currentRoom.interac:
                            if (item == Game.currentRoom.interac[i][1]):
                                if (Game.currentRoom.interac[i][2] == "on"):
                                    Game.currentRoom.interac[i][2] = "off"

                                elif (Game.currentRoom.interac[i][2] == "off"):
                                    Game.currentRoom.interac[i][2] = "on"

                                response = "{} used.".format(item)
                                break
                        break
                if (Game.currentRoom == r12):
                    if (Game.currentRoom.interac["bomb"][2] == "off"):
                        Game.currentRoom = None
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
