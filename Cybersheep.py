from Point import Point
from Animal import Animal
from Hogweed import Hogweed
from math import hypot
from random import randint

class Cybersheep(Animal):
	species = "Cybersheep"

	def __init__(self, world, position):
		Animal.__init__(self, world, position, 11, 4)

	def scan(self):
		for i in range(self.world.height * self.world.width):
			if self.world.organisms[i] is not None:
				if isinstance(self.world.organisms[i], Hogweed):
					return True
		return False

	def findNearest(self):
		idd = None
		dist = None
		for i in range(self.world.height * self.world.width):
			if self.world.organisms[i] is not None:
				if isinstance(self.world.organisms[i], Hogweed):
					temp = hypot(self.world.organisms[i].position.x - self.position.x, self.world.organisms[i].position.y - self.position.y)
					if dist is None or temp < dist:
						dist = temp
						idd = i
		return self.world.organisms[idd].position
		
	def action(self):
		self.getOlder()
		if self.scan():
			target = self.findNearest()
			dx = target.x - self.position.x
			dy = target.y - self.position.y
			if dx > 0:
				dx = 1
			elif dx < 0:
				dx = -1
			if dy > 0:
				dy = 1
			elif dy < 0:
				dy = -1

			if dx != 0 and dy != 0:
				choose = randint(0, 1)
				if choose == 0:
					dx = 0
				elif choose == 1:
					dy = 0

			destination = Point(self.position.x + dx, self.position.y + dy)
			if self.world.getOrganism(destination) is not None:
				self.world.getOrganism(destination).collision(self)
			else:
				self.position = destination
		else:
			Animal.action(self)

	def reproduce(self):
		return False

	def die(self, other):
		if not isinstance(other, Hogweed):
			Animal.die(self, other)
			return True
		return False
		
	def createNew(self, i, position):
		self.world.organisms[i] = Cybersheep(self.world, position)
	
	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/cybersheep.gif")
