from Animal import Animal

class Wolf(Animal):
	species = "Wolf"

	def __init__(self, world, position):
		Animal.__init__(self, world, position, 9, 5)

	def createNew(self, i, position):
		self.world.organisms[i] = Wolf(self.world, position)

	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/wolf.gif")
