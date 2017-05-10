from Tkinter import *


potentialWords = "Andromeda Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum \
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

dictOfWords = {x:potentialWords[x] for x in range(0, len(potentialWords))}
WIDTH = 100
HEIGHT = 200

master = Tk()
top = Toplevel()
top.title("List of words:")

scrollbar = Scrollbar(top)
scrollbar.pack(side=RIGHT, fill=Y)

player_input = Entry(top, width =WIDTH)
player_input.bind("<Return>", process())
player_input.pack(side=BOTTOM, fill=X)
player_input.focus

listbox = Listbox(top, yscrollcommand=scrollbar.set, width=WIDTH)
for key,value in dictOfWords.items():
    listbox.insert(END, str(key) + "-->" + value)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

mainloop()

def process(self):
    #Take the player input from the popup window
    action = player_input
    # Check to see if the number is in the list of potential words
    if (action in dictofWords):
        top.destroy
        top = Toplevel()
        top.title("You chose: ")

        text = Text(top, width=WIDTH)
        text.pack(side=TOP, fill=X)

        button = Button(top, text="Accept", width =WIDTH/3)
        button.pack(side=BOTTOM, fill=X)

