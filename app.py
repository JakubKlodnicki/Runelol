from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import *
import sqlite3

conn = sqlite3.connect('runelol.db')

master = Tk()

master.geometry("800x500")

image_path = {
    "Precission": "./runepng/path/precission.png",
    "Domination": "./runepng/path/domination.png",
	"Inspiration": "./runepng/path/inspiration.png",
	"Resolve": "./runepng/path/resolve.png",
	"Sorcery": "./runepng/path/sorcery.png",
}

image_keystone = {
    "Presstheatack": "./runepng/keystone/presstheattack.png",
    "Lethaltempo": "./runepng/keystone/lethaltempo.png",
	"Fleetfootwork": "./runepng/keystone/footwork.png",
	"Conqueror": "./runepng/keystone/conqueror.png",
	"Electrocute": "./runepng/keystone/electrocute.png",
	"Predator": "./runepng/keystone/predator.png", 
    "Darkharvest": "./runepng/keystone/darkharvest.png",
	"Hallofblades": "./runepng/keystone/halloofblade.png",
	"Summonaery": "./runepng/keystone/summonarey.png",
	"Arcanecomet": "./runepng/keystone/comet.png",
	"Phaserush": "./runepng/keystone/phaserush.png",
	"Graspoftheundying": "./runepng/keystone/grasp.png",
	"Aftershock": "./runepng/keystone/aftershock.png",
	"Guardian": "./runepng/keystone/guardian.png",
	"Glacialaugment": "./runepng/keystone/glacial.png",
	"Spellbook": "./runepng/keystone/spellbook.png",
	"Firststrike": "./runepng/keystone/firststrike.png",
}

def openAkaliWindow():
	akaliWindow = Toplevel(master)
	akaliWindow.title("Akali")
	akaliWindow.geometry("800x500")
	cursor = conn.execute("SELECT Champion, Paths, Keystone, Slot1, Slot2, Slot3, Paths2, `Slot1-2`, `Slot2-2`, `Slot3-2`, Stats1, Stats2, Stats3 FROM runes where Champion='Akali';")
	for row in cursor:
		imgpath = PhotoImage(file=image_path.get(row[1], "default.png"))
		imgkeystone = PhotoImage(file=image_keystone.get(row[2], "default.png"))
		path = Label(akaliWindow, image=imgpath).pack()
		keystone = Label(akaliWindow, image=imgkeystone).pack()
		slot1 = Label(akaliWindow, text=row[3]).pack()
		slot2 = Label(akaliWindow, text=row[4]).pack()
		akaliWindow.mainloop()

	
akali = Button(master,
			text ="Akali",
			command = openAkaliWindow)
akali.pack(pady = 10)


mainloop()