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
image_slot1 = {
    "Cheapshot": "./runepng/slot1/cheapshot.png",
	"Demolish": "./runepng/slot1/Demolish_rune.png",
	"Fontoflife": "./runepng/slot1/Font_of_Life_rune.png",
	"Hextechflashtraption": "./runepng/slot1/Hextech_Flashtraption_rune.png",
	"Magicalfootwear": "./runepng/slot1/Magical_Footwear_rune.png",
	"Manaflowband": "./runepng/slot1/Manaflow_Band_rune.png",
	"Nimbuscloak": "./runepng/slot1/Nimbus_Cloak_rune.png",
	"Nullifyingorb": "./runepng/slot1/Nullifying_Orb_rune.png",
	"Overheal": "./runepng/slot1/overheal.png",
	"Perfecttiming": "./runepng/slot1/Perfect_Timing_rune.png",
	"Presenceofmind": "./runepng/slot1/Presence_of_Mind_rune.png",
	"Shieldbash": "./runepng/slot1/Shield_Bash_rune.png",
	"SuddenImpact": "./runepng/slot1/Sudden_Impact_rune.png",
	"Tasteofblood": "./runepng/slot1/Taste_of_Blood_rune.png",
	"Triumph": "./runepng/slot1/Triumph_rune.png",
}
image_slot2 = {
    "Absolutefocus": "./runepng/slot2/Absolutefocus.png",
	"Alacrity": "./runepng/slot2/Alacrity.png",
	"BiscuitDelivery": "./runepng/slot2/BiscuitDelivery.png",
	"Bloodline": "./runepng/slot2/Bloodline.png",
	"Boneplating": "./runepng/slot2/Boneplating.png",
	"Celerity": "./runepng/slot2/Celerity.png",
	"Conditioning_rune": "./runepng/slot2/Conditioning_rune.png",
	"Eyeball_Collection_rune": "./runepng/slot2/Eyeball_Collection_rune.png",
	"Futuremarket": "./runepng/slot2/Futuremarket.png",
	"Ghostporo": "./runepng/slot2/Ghost_Poro_rune.png",
	"MinionDematerializer": "./runepng/slot2/MinionDematerializerrune.png",
	"Secondwind": "./runepng/slot2/Secondwindrune.png",
	"Tenacity": "./runepng/slot2/Tenacity.png",
	"Transcendence": "./runepng/slot2/Transcendence_rune.png",
	"Zombieward": "./runepng/slot2/Zombieward.png",
}
image_slot3 = {
    "Velocity": "./runepng/slot3/Approach_Velocity_rune.png",
	"Cosmicinsight": "./runepng/slot3/Cosmic_Insight_rune.png",
	"Coupdegrace": "./runepng/slot3/Coup_de_Grace_rune.png",
	"Cutdown": "./runepng/slot3/Cut_Down_rune.png",
	"Gatheringstorm": "./runepng/slot3/Gathering_Storm_rune.png",
	"Ingenioushunter": "./runepng/slot3/Ingenious_Hunter_rune.png",
	"Laststand": "./runepng/slot3/Last_Stand_rune.png",
	"Overgrowth": "./runepng/slot3/Overgrowth_rune.png",
	"Relentlesshunter": "./runepng/slot3/Relentless_Hunter_rune.png",
	"Revitalize": "./runepng/slot3/Revitalize_rune.png",
	"Scorch": "./runepng/slot3/Scorch_rune.png",
	"Timewarptonic": "./runepng/slot3/Time_Warp_Tonic_rune.png",
	"Treasurehunter": "./runepng/slot3/Treasure_Hunter_rune.png",
	"Ultimatehunter": "./runepng/slot3/Ultimate_Hunter_rune.png",
	"Unflinching": "./runepng/slot3/Unflinching_rune.png",
	"Waterwalking": "./runepng/slot3/Waterwalking_rune.png",
}
image_shard1 = {
    "Adaptiveforce": "./runepng/shards/Adaptiveforce.png",
	"Attackspeed": "./runepng/shards/Attackspeed.png",
	"Haste": "./runepng/shards/Haste.png",
}
image_shard2 = {
    "Adaptiveforce": "./runepng/shards/Adaptiveforce.png",
	"Shield": "./runepng/shards/Shield.png",
	"Magicresistance": "./runepng/shards/Magicresistance.png",
}
image_shard3 = {
    "Health": "./runepng/shards/Health.png",
	"Shield": "./runepng/shards/Shield.png",
	"Magicresistance": "./runepng/shards/Magicresistance.png",
}

def openAkaliWindow():
	akaliWindow = Toplevel(master)
	akaliWindow.title("Akali")
	akaliWindow.geometry("800x500")
	cursor = conn.execute("SELECT Champion, Paths, Keystone, Slot1, Slot2, Slot3, Paths2, `Slot1-2`, `Slot2-2`, `Slot3-2`, Stats1, Stats2, Stats3 FROM runes where Champion='Akali';")
	for row in cursor:
		imgpath = PhotoImage(file=image_path.get(row[1], "default.png"))
		imgkeystone = PhotoImage(file=image_keystone.get(row[2], "default.png"))
		imgslot1 = PhotoImage(file=image_slot1.get(row[3], "default.png"))
		imgslot2 = PhotoImage(file=image_slot2.get(row[4], "default.png"))
		imgslot3 = PhotoImage(file=image_slot3.get(row[5], "default.png"))
		imgpath2 = PhotoImage(file=image_path.get(row[6], "default.png"))
		imgslot1_2 = PhotoImage(file=image_slot1.get(row[7], "default.png")) if row[7] != None else None
		imgslot2_2 = PhotoImage(file=image_slot2.get(row[8], "default.png")) if row[8] != None else None
		imgslot3_2 = PhotoImage(file=image_slot3.get(row[9], "default.png")) if row[9] != None else None
		imgshard1 = PhotoImage(file=image_shard1.get(row[10], "default.png"))
		imgshard2 = PhotoImage(file=image_shard2.get(row[11], "default.png"))
		imgshard3 = PhotoImage(file=image_shard3.get(row[12], "default.png"))
		path = Label(akaliWindow, image=imgpath).place(relx = 0.3,rely=0.0)
		keystone = Label(akaliWindow, image=imgkeystone).place(relx = 0.3, rely=0.15)
		slot1 = Label(akaliWindow, image=imgslot1).place(relx = 0.3, rely=0.3)
		slot2 = Label(akaliWindow, image=imgslot2).place(relx = 0.3, rely=0.45)
		slot3 = Label(akaliWindow, image=imgslot3).place(relx = 0.3, rely=0.6)
		path2 = Label(akaliWindow, image=imgpath2).place(relx = 0.6, rely=0.0)
		slot1_2 = Label(akaliWindow, image=imgslot1_2).place(relx = 0.6, rely=0.15) if row[7] != None else None
		slot2_2 = Label(akaliWindow, image=imgslot2_2).place(relx = 0.6, rely=0.3) if row[8] != None else None
		slot3_2 = Label(akaliWindow, image=imgslot3_2).place(relx = 0.6, rely=0.45) if row[9] != None else None
		shard1 = Label(akaliWindow, image=imgshard1).pack()
		shard2 = Label(akaliWindow, image=imgshard2).pack()
		shard3 = Label(akaliWindow, image=imgshard3).pack()
		akaliWindow.mainloop()

	
akali = Button(master,
			text ="Akali",
			command = openAkaliWindow)
akali.pack(pady = 10)


mainloop()