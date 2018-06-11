from random import randint
from Organism import Organism
from Sheep import Sheep
from Wolf import Wolf
from Turtle import Turtle
from Antelope import Antelope
from Fox import Fox
from Cybersheep import Cybersheep
from Human import Human
from Grass import Grass
from Dandelion import Dandelion
from Belladonna import Belladonna
from Hogweed import Hogweed
from Point import Point
from tkinter import *

class World:
	width = 0
	height = 0
	organisms = None
	turnNumber = 0
	powerCounter = 0
	mainWindow = None
	labels = []

	def __init__(self, width, height):
		self.height = height
		self.width = width

		logFile = open("default.log", "w+")
		logFile.close()
		self.addToLog("It is now turn number 0")

		self.allocOrganisms()
		self.randSpawn()


		self.mainWindow = Tk()
		self.mainWindow.title("Mikołaj Sperkowski 171725")

		box = Toplevel()
		box.title("Animal World")

		log = Text(box, height = 10, width = 50, bg = "white", fg = "black")
		log.config(state = 'disabled')
		log.pack()

		for i in range(0, self.width):
			x = []
			for j in range(0, self.height):
				label = Label(self.mainWindow, padx = 0, pady = 0)
				label.grid(row = i, column = j)
				x.append(label)
			self.labels.append(x)

		def updateLog(log):
			log.config(state = 'normal')
			log.delete(1.0, END)
			file = open("default.log", "r")
			log.insert(END, file.read())
			log.see("end")
			log.config(state = 'disabled')
			pass

		def key(event):
			inputt = repr(event.char).replace("'", "")
			if inputt == 's':
				self.saveToFile()
			elif inputt == 'l':
				self.loadFile()
				self.powerCounter = 0
				self.turnNumber = 0
				self.drawWorld()
			elif inputt == 'n' or inputt == 'p':
				if inputt == 'p' and self.powerCounter > 0:
					inputt = 'n'
				if inputt == 'p' and self.powerCounter == 0:
					self.powerCounter = 11
				self.simulate(inputt)
				updateLog(log)
		def left(event):
			self.simulate('l')
			updateLog(log)
		def right(event):
			self.simulate('r')
			updateLog(log)
		def up(event):
			self.simulate('u')
			updateLog(log)
		def down(event):
			self.simulate('d')
			updateLog(log)

		self.mainWindow.bind("<Key>", key)
		self.mainWindow.bind("<Left>", left)
		self.mainWindow.bind("<Right>", right)
		self.mainWindow.bind("<Up>", up)
		self.mainWindow.bind("<Down>", down)

		self.drawWorld()
		self.mainWindow.mainloop()


	def allocOrganisms(self):
		self.organisms = [None] * self.width * self.height

	def sortOrganisms(self):
		chckSort = True
		i = 0
		while i < self.width * self.height - 1:
			if self.organisms[i] is None and self.organisms[i + 1] is not None:
				self.organisms[i] = self.organisms[i + 1]
				self.organisms[i + 1] = None
				i = 0
			i += 1
		while chckSort:
			chckSort = False
			for i in range(self.width * self.height - 1):
				if self.organisms[i] is None and self.organisms[i + 1] is not None:
					swap = False
					if self.organisms[i].initiative < self.organisms[i + 1].initiative:
						swap = True
					elif self.organisms[i].initiative == self.organisms[i + 1].initiative:
						if self.organisms[i].age < self.organisms[i + 1].age:
							swap = True;
					if swap:
						chckSort = true
						temp = self.organisms[i]
						self.organisms[i] = self.organisms[i + 1]
						self.organisms[i + 1] = temp
	def getOrganism(self, position):
		for i in range(0, self.width * self.height):
			if self.organisms[i] is not None:
				if self.organisms[i].position.x == position.x and self.organisms[i].position.y == position.y:
					return self.organisms[i]
		return None

	def getFree(self):
		for i in range(0, self.width * self.height):
			if self.organisms[i] is None:
				return i
		return -1
	
	def removeOrganism(self, position):
		for i in range(self.width * self.height):
			if self.organisms[i] is not None:
				if self.organisms[i].position.x == position.x and self.organisms[i].position.y == position.y:
					self.organisms[i] = None
		self.sortOrganisms()
	
	def randSpawn(self):
		index = 0
		isHuman = False
		for i in range(0, self.height):
			for j in range(0, self.width):
				chance = randint(0, 99)
				if chance < 15:
					uni = randint(0, 10)

					if uni == 0:
						self.organisms[index] = Sheep(self, Point(i, j))
					elif uni == 1:
						self.organisms[index] = Wolf(self, Point(i, j))
					elif uni == 2:
						self.organisms[index] = Fox(self, Point(i, j))
					elif uni == 3:
						self.organisms[index] = Turtle(self, Point(i, j))
					elif uni == 4:
						self.organisms[index] = Antelope(self, Point(i, j))
					elif uni == 5:
						self.organisms[index] = Cybersheep(self, Point(i, j))
					elif uni == 6:
						self.organisms[index] = Grass(self, Point(i, j))
					elif uni == 7:
						self.organisms[index] = Dandelion(self, Point(i, j))
					elif uni == 8:
						self.organisms[index] = Belladonna(self, Point(i, j))
					elif uni == 9:
						self.organisms[index] = Hogweed(self, Point(i, j))
					index += 1
				elif not isHuman:
					self.organisms[index] = Human(self, Point(i, j))
					isHuman = True
					index += 1
		
	def drawWorld(self):
		for i in range(0, self.width):
			for j in range(0, self.height):
				self.drawSingle(Point(i, j), "./base.gif")
		for i in range(self.width * self.height):
			if self.organisms[i] is not None:
				self.organisms[i].draw()

	def drawSingle(self, position, path):
		img = PhotoImage(file = path, format = 'gif')
		self.labels[position.x][position.y].config(image = img)
		self.labels[position.x][position.y].image = img

	def addToLog(self, text):
		log = open("default.log", "a")
		log.write(text + '\n')
		log.close()

	def saveToFile(self):
		save = open("savefile.wsf", "w")
		for i in range(0, self.width * self.height):
			if self.organisms[i] is not None:
				temp = self.organisms[i].species + ' '
				temp += str(self.organisms[i].power) + ' '
				temp += str(self.organisms[i].age) + ' '
				temp += str(self.organisms[i].position.x) + ' '
				temp += str(self.organisms[i].position.y) + ' '
				save.write(temp)
		save.write("END")

		if save is not None:
			save.close()

	def loadFile(self):
		self.organisms = None
		self.allocOrganisms()
		savefile = open("savefile.wsf", "r")
		index = 0
		ptr = 0
		string = savefile.read().split(' ')
		while True:
			if string[ptr] == "END":
				break
			typee = string[ptr]
			ptr += 1
			power = int(string[ptr])
			ptr += 1
			age = int(string[ptr])
			ptr += 1
			x = int(string[ptr])
			ptr += 1
			y = int(string[ptr])
			ptr += 1
			position = Point(x, y)

			if typee == "Grass":
				self.organisms[index] = Grass(self, position)
			elif typee == "Dandelion":
				self.organisms[index] = Dandelion(self, position)
			elif typee == "Guarana":
				self.organisms[index] = Guarana(self, position)
			elif typee == "Belladonna":
				self.organisms[index] = Belladonna(self, position)
			elif typee == "Hogweed":
				self.organisms[index] = Hogweed(self, position)
			elif typee == "Wolf":
				self.organisms[index] = Wolf(self, position)
			elif typee == "Sheep":
				self.organisms[index] = Sheep(self, position)
			elif typee == "Fox":
				self.organisms[index] = Fox(self, position)
			elif typee == "Turtle":
				self.organisms[index] = Turtle(self, position)
			elif typee == "Antelope":
				self.organisms[index] = Antelope(self, position)
			elif typee == "Human":
				self.organisms[index] = Human(self, position)
			elif typee == "Cybersheep":
				self.organisms[index] = Cybersheep(self, position)

			self.organisms[index].power = power
			self.organisms[index].age = age
			index += 1

		if savefile is not None:
			savefile.close()

	
	def simulate(self, inputt):
		self.sortOrganisms()
		for i in range(0, self.width * self.height):
			if self.organisms[i] is not None:
				if isinstance(self.organisms[i], Human):
					self.organisms[i].doing = inputt
					if self.powerCounter == 5:
						self.organisms[i].superpower = False
				self.organisms[i].action()
		if self.powerCounter > 0:
			self.powerCounter -= 1
		self.turnNumber += 1

		if self.powerCounter > 5:
			self.addToLog(str(self.powerCounter - 5) + " turns of invincibility remaining")
		if self.powerCounter > 0 and self.powerCounter <= 5:
			self.addToLog(str(self.powerCounter) + " turns until power can be used again")
		self.addToLog("It is now turn number " + str(self.turnNumber))
		self.drawWorld()
