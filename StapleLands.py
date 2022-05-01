from Land import Land

class StapleLands:

	def getStapleLands(deckColors=[]):
		colors = deckColors
		recommendedLands = list()
		stapleLands = StapleLands.initStapleLands()

		for x in stapleLands:
			if x.isWithinIdentity(colors):
				recommendedLands.append(x)

		return recommendedLands

	def initStapleLands():
		staples = list()

		badlands = Land("Badlands", "dual", ['r', 'g'])
		bayou = Land("Bayou", "dual", ['b', 'g'])
		plateau = Land("Plateau", "dual", ['w', 'r'])
		savannah = Land("Savannah", "dual", ['w', 'g'])
		scrubland = Land("Scrubland", "dual", ['w', 'b'])
		taiga = Land("Taiga", "dual", ['r', 'g'])
		tropicalIsland = Land("Tropical Island", "dual", ['u', 'g'])
		tundra = Land("Tundra", "dual", ['w', 'u'])
		undergroundSea = Land("Underground Sea", "dual", ['u', 'b'])
		volcanicIsland = Land("Volcanic Island", "dual", ['u', 'r'])

		staples.append(badlands)
		staples.append(bayou)
		staples.append(plateau)
		staples.append(savannah)
		staples.append(scrubland)
		staples.append(taiga)
		staples.append(tropicalIsland)
		staples.append(tundra)
		staples.append(undergroundSea)
		staples.append(volcanicIsland)
		

		return staples