from Plant import Plant

class Grass(Plant):
	
	species = "Grass"

	def __init__(self, world, position):
		Plant.__init__(self, world, position, 0)

	def createNew(self, i, position):
		self.world.organisms[i] = Grass(self.world, position)
	
	def draw(self):
		self.world.drawSingle(self.position, "data/art/plants/grass.gif")
