from Animal import Animal

class Fox(Animal):
	species = "Fox"

	def __init__(self, world, position):
		Animal.__init__(self, world, position, 3, 7)

	def action(self):
		self.getOlder()
		destination = self.randomStep()
		if self.world.getOrganism(destination) is not None:
			if self.species == self.world.getOrganism(destination).species or self.power > self.world.getOrganism(destination).power:
				self.world.getOrganism(destination).collision(self)
		else:
			self.position = destination
	
	def createNew(self, i, position):
		self.world.organisms[i] = Fox(self.world, position)
	
	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/fox.gif")
