from random import randint, shuffle
from Point import Point

class Organism:
	
	species = None
	power = None
	age = 0
	initiative = None
	position = None
	world = None

	def __init__(self, world, position, power, initiative):
		self.world = world
		self.position = position
		self.power = power
		self.initiative = initiative

	def wrapPosition(self, position):
		if position.x > self.world.height - 1:
			position.x -= self.world.height
		if position.y > self.world.width - 1:
			position.y -= self.world.width
		if position.x < 0:
			position.x += self.world.height
		if position.y < 0:
			position.y += self.world.width
	
	def getOlder(self):
		self.age += 1

	def fight(self, other):
		self.world.addToLog(self.species + " and " + other.species + " are fighting!")
		if self.power > other.power:
			self.world.addToLog(self.species + " has won!")
			other.die(self)
		else:
			self.world.addToLog(other.species + " has won!")
			self.die(other)
	
	def randomStep(self):
		dx = 0
		dy = 0

		randomDirection = randint(0, 3)

		if randomDirection == 0:
			dx = 1
		elif randomDirection == 1:
			dx = -1
		elif randomDirection == 2:
			dy = 1
		elif randomDirection == 3:
			dy = -1

		destination = Point(self.position.x + dx, self.position.y + dy)
		self.wrapPosition(destination)

		return destination
	
	def reproduce(self):
		d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		shuffle(d)
		for i in range(0, 4):
			temp = Point(self.position.x + d[i][0], self.position.y + d[i][1])
			self.wrapPosition(temp)
			if self.world.getOrganism(temp) is None:
				self.createNew(self.world.getFree(), temp)
				self.world.addToLog(self.species + " has reproduced!")
				return True
		return False

	def die(self, other):
		self.world.removeOrganism(self.position)
		return True
