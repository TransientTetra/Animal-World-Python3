from Organism import Organism
from random import randint

class Plant(Organism):
	
	def __init__(self, world, position, power):
		Organism.__init__(self, world, position, power, 0)

	def action(self):
		self.getOlder()
		chance = randint(0, 100)

		if self.age >= 10 and chance == 0:
			self.reproduce()

	def collision(self, other):
		self.fight(other)

	def fight(self, other):
		self.world.addToLog(other.species + " is trying to eat a " + self.species + '!')
		if self.power > other.power:
			self.world.addToLog(other.species + " has been poisoned and died!")
			other.die(self)
		else:
			self.world.addToLog(other.species + " has eaten " + self.species + '!')
			self.die(other)
