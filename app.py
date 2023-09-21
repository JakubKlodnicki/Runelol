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

def openAkaliWindow():
	akaliWindow = Toplevel(master)
	akaliWindow.title("Akali")
	akaliWindow.geometry("800x500")
	cursor = conn.execute("SELECT Champion, Paths, Keystone, Slot1, Slot2, Slot3, Paths2, `Slot1-2`, `Slot2-2`, `Slot3-2`, Stats1, Stats2, Stats3 FROM runes where Champion='Akali';")
	for row in cursor:
		img = PhotoImage(file=image_path.get(row[1], "default.png"))
		label = Label(akaliWindow, image=img).pack()
		path = Label(akaliWindow, text=row[1]).pack()
		keystone = Label(akaliWindow, text=row[2]).pack()
		slot1 = Label(akaliWindow, text=row[3]).pack()
		slot2 = Label(akaliWindow, text=row[4]).pack()
		akaliWindow.mainloop()

	
akali = Button(master,
			text ="Akali",
			command = openAkaliWindow)
akali.pack(pady = 10)


mainloop()