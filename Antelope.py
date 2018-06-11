from random import randint
from Animal import Animal

class Antelope(Animal):
	species = "Antelope"

	def __init__(self, world, position):
		Animal.__init__(self, world, position, 4, 4)
	
	def action(self):
		self.getOlder()

		destination = self.randomStep()
		destination.x += destination.x - self.position.x
		destination.y += destination.y - self.position.y
		self.wrapPosition(destination)
		if self.world.getOrganism(destination) is not None:
			self.world.getOrganism(destination).collision(self)
		else:
			self.position = destination

	def fight(self, other):
		chance = randint(0, 1)
		if chance == 0 and self.escape():
			pass
		else:
			Animal.fight(self, other)

	def createNew(self, i, position):
		self.world.organisms[i] = Antelope(self.world, position)

	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/antelope.gif")
