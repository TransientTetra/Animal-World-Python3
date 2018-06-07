class World:
	width = 0
	height = 0
	organisms = 0
	turnNumber = 0
	powerCounter = 0

	def __init__(self, width, height):
		this.height = height
		this.width = width

		#here log file

		allocOrganisms()
		randSpawn()

		#here window creating possibly

		drawWorld()

	def allocOrganisms():
		organisms = Organism[width * height]

	def sortOrganisms():
		chckSort = True
		i = 0
		while i < width * height - 1:
			if organisms[i] is None and organisms[i + 1] is not None:
				organisms[i] = organisms[i + 1]
				organisms[i + 1] = None
				i = 0
			i += 1
		while chckSort:
			chckSort = False
			for i in range(width * height - 1):
				if organisms[i] is None and organisms[i + 1] is not None
					swap = False
					if organisms[i].getInitiative() < organisms[i + 1].getInitiative():
						swap = True
					elif organisms[i].getInitiative() == organisms[i + 1].getInitiative():
						if organisms[i].getAge() < organisms[i + 1].getAge()
							swap = True;
					if swap:
						chckSort = true
						temp = organisms[i]
						organisms[i] = organisms[i + 1]
						organisms[i + 1] = temp
	
	def randSpawn():
		pass

	def drawWorld():
		for i in range(width * height):
			if organisms[i] is not None
				organisms[i].draw()

	def drawSingle(position, path):
		pass
	
	def simulate(inputt):
		pass
