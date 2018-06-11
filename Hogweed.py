from Animal import Animal
from Point import Point
from Plant import Plant

class Hogweed(Plant):

	species = "Hogweed"

	def __init__(self, world, position):
		Plant.__init__(self, world, position, 10)
	
	def action(self):
		Plant.action(self)
		d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		for i in range(0, 4):
			temp = Point(self.position.x + d[i][0], self.position.y + d[i][1])
			self.wrapPosition(temp)
			if self.world.getOrganism(temp) is not None:
				if isinstance(self.world.getOrganism(temp), Animal):
					name = self.world.getOrganism(temp).species
					if self.world.getOrganism(temp).die(self):
						self.world.addToLog(name + " has been burned by hogweed!")

	def fight(self, other):
		if other.power >= self.power:
			self.world.addToLog(other.species + " has eaten " + self.species + '!')
			self.die(self)
		if other.die(self):
			self.world.addToLog(other.species + " tried eating hogweed and died!")

	def createNew(self, i, position):
		self.world.organisms[i] = Hogweed(self.world, position)
	
	def draw(self):
		self.world.drawSingle(self.position, "data/art/plants/hogweed.gif")
