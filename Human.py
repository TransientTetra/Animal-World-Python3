from Animal import Animal
from Point import Point

class Human(Animal):
	species = "Human"
	superpower = False
	doing = 'n'

	def __init__(self, world, position):
		Animal.__init__(self, world, position, 5, 4)

	def die(self, other):
		if self.superpower:
			self.escape()
			return False
		else:
			Animal.die(self, other)
			return True

	def action(self):
		self.getOlder()
		dx = 0
		dy = 0
		if self.doing == 'l':
			dy -= 1
		elif self.doing == 'r':
			dy += 1
		elif self.doing == 'u':
			dx -= 1
		elif self.doing == 'd':
			dx += 1
		elif self.doing == 'p':
			self.superpower = True

		if dx != 0 or dy != 0:
			destination = Point(self.position.x + dx, self.position.y + dy)
			self.wrapPosition(destination)
			if self.world.getOrganism(destination) is not None:
				self.world.getOrganism(destination).collision(self)
			else:
				self.position = destination
	
	def createNew(self, i, position):
		self.world.organisms[i] = Human(self.world, position)

	def draw(self):
		self.world.drawSingle(self.position, "data/art/animals/human.gif")
