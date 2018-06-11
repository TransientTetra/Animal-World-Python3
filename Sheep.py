from Animal import Animal

class Sheep(Animal):
	species = "Sheep"
	
	def __init__(self, world, position):
		Animal.__init__(self, world, position, 4, 4)

	def createNew(self, i, position):
		self.world.organisms[i] = Sheep(self.world, position)

	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/sheep.gif")
