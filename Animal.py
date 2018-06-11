from Point import Point
from Organism import Organism
from random import shuffle

class Animal(Organism):
	
	def escape(self):
		d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		shuffle(d)
		for i in range(0, 4):
			temp = Point(self.position.x + d[i][0], self.position.y + d[i][1])
			self.wrapPosition(temp)

			if self.world.getOrganism(temp) is None:
				self.position = temp
				return True
		return False

	def action(self):
		self.getOlder()
		destination = self.randomStep()
		if self.world.getOrganism(destination) is not None:
			self.world.getOrganism(destination).collision(self)
		else:
			self.position = destination
	
	def collision(self, other):
		if other.species == self.species:
			if self.age > 18 and other.age > 18:
				if not self.reproduce():
					other.reproduce()
		else:
			self.fight(other)
