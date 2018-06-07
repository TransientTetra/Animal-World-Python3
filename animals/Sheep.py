class Sheep(Organism):

	species = "Sheep"
	
	def __init__(self, World world, Point position):
		Organism.__init__(self, world, position, 4, 4)

	def createNew(int i, Point position):
		world.organisms[i] = Sheep(world, position)

	def draw():
		world.drawSingle(position, "data/art/animals/sheep.png")
