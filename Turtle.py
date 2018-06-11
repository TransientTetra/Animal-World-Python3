from Point import Point
from Animal import Animal
from random import randint

class Turtle(Animal):
	species = "Turtle"
	armour = 5

	def __init__(self, world, position):
		Animal.__init__(self, world, position, 2, 1)

	def action(self):
		chance = randint(0, 3)
		if chance == 0:
			Animal.action(self)
		else:
			self.getOlder()
			
	def collision(self, other):
		if other.power >= self.armour or other.species == self.species:
			Animal.collision(self, other)
		else:
			temp = Point(2 * other.position.x - self.position.x, 2 * other.position.y - self.position.y)
			self.wrapPosition(temp)
			if self.world.getOrganism(temp) is None:
				other.position = temp
			
	def createNew(self, i, position):
		self.world.organisms[i] = Turtle(self.world, position)
	
	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/turtle.gif")
