from Plant import Plant

class Belladonna(Plant):
	
	species = "Belladonna"

	def __init__(self, world, position):
		Plant.__init__(self, world, position, 99)

	def fight(self, other):
		self.world.addToLog(other.species + " has been poisoned by belladonna and died!")
		if other.power >= self.power:
			self.die(other)
		other.die(self)
	
	def createNew(self, i, position):
		self.world.organisms[i] = Belladonna(self.world, position)

	def draw(self):
		self.world.drawSingle(self.position, "data/art/plants/belladonna.gif")
