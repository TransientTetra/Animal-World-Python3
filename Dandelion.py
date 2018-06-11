from Plant import Plant

class Dandelion(Plant):
	
	species = "Dandelion"

	def __init__(self, world, position):
		Plant.__init__(self, world, position, 0)

	def action(self):
		Plant.action(self)
		Plant.action(self)
		self.age -= 1
		Plant.action(self)
		self.age -= 1
	
	def createNew(self, i, position):
		self.world.organisms[i] = Dandelion(self.world, position)
	
	def draw(self):
		self.world.drawSingle(self.position, "data/art/plants/dandelion.gif")
